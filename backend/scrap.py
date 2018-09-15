from bs4 import BeautifulSoup
import requests
import json
import predict_ingredients
from fooddata import FoodData
class Parser:
    predictor = 0
    def __init__(self):
        self.predictor = predict_ingredients.Predictor()
    def parse(self, url):
        recipe = dict()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if "allrecipes.com" in url:
            ingredients = soup.find_all("span", itemprop="recipeIngredient")
            recipe["title"] = soup.select("#recipe-main-content")[0].text
        elif "myrecipes" in url:
            ingredients = soup.find_all("div", class_="ingredients")
            ingredients = ingredients[0].find_all("li")
            recipe["title"] = soup.select(".headline")[0].text
        else:
            ingredients = soup.find_all("span", itemprop="recipeIngredient") #fallback allrecipes :D
            recipe["title"] = soup.select("#recipe-main-content")[0].text
        ingredientsArray = []


        for i in ingredients:
            ingredientsText = i.text
            offset = 0
            if "allrecipes" in url:
                dataId = int(i["data-id"])

                if dataId == 0:
                    continue
            if not ingredientsText.split(" ")[0].isnumeric():
                quantity = "1"
                if ingredientsText.split(" ")[1] in FoodData.unitConversionTable:
                    unit = ingredientsText.split(" ")[1]
                    name = " ".join(ingredientsText.split(" ")[2:])
                else:
                    unit = ""
                    name = " ".join(ingredientsText.split(" ")[1:])
            elif("(" in ingredientsText.split(" ")[1]):

                quantity = ingredientsText.split(" ")[1][1:]
                unit = ingredientsText.split(" ")[2][:-1]
                name = " ".join(ingredientsText.split(" ")[4:])
                #todo
            else:
                if("/" in ingredientsText.split(" ")[1]):
                    offset = offset + 1
                    quantity = " ".join(ingredientsText.split(" ")[0:2])
                    name = " ".join(ingredientsText.split(" ")[3:])
                else:
                    quantity = ingredientsText.split(" ")[0]
                    unit = None
                    name = ""
                    if ingredientsText.split(" ")[1+offset] in FoodData.unitConversionTable:
                        unit =  ingredientsText.split(" ")[1+offset]
                        offset = offset + 1
                    name = " ".join(ingredientsText.split(" ")[1+offset:])
            costs = self.classify(name, unit, quantity)
            ingredientsArray.append({"name": name, "unit":unit, "quantity":quantity, "costs": costs})

        recipe["ingredients"] = ingredientsArray


        return recipe

    def classify(self,ingredient, unit, quantity):
        ingredient = ingredient.lower()
        co2Footprint = 10
        waterFootprint = 0
        energyFootprint = 0
        predictedIngredient = self.predictor.predict([ingredient])[0]

        if "/" in quantity:
            quantitySplit = quantity.split(" ")
            offset = 0
            if len(quantitySplit) > 1:
                offset = 1
            fracture = quantitySplit[offset].split("/")
            quantity = float(fracture[0])/float(fracture[1])
            if offset >0:
                quantity = quantity + float(quantitySplit[0])
        else:
            quantity = float(quantity)


        if predictedIngredient in FoodData.co2footprintTable:
            mass = -1;
            if unit in FoodData.unitConversionTable:
                mass = quantity*FoodData.unitConversionTable[unit]

            #calculate footprint
            if mass <= 0:
                mass = 0.2 #just a 200g for not known unit
            co2Footprint = FoodData.co2footprintTable[predictedIngredient]*mass
            waterFootprint = FoodData.waterfootprintTable[predictedIngredient]*mass
            energyFootprint = FoodData.energyfootprintTable[predictedIngredient]*mass


        else:
            co2Footprint = 0.12356*quantity
            waterFootprint = 0.12356*quantity
            energyFootprint = 0.12356*quantity


        return dict(
                co2=co2Footprint,
                water=waterFootprint,
                energy=energyFootprint
        )
