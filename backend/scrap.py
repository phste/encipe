from bs4 import BeautifulSoup
import requests
import json
import predict_ingredients
class Parser:
    unitConversionTable = {"cup": 0.24, #liter
        "cups":0.24,
        "tablespoon": 0.0143, #kilogramm
        "tablespoons": 0.0143,
        "teaspoon": 0.0048, #kilogramm
        "teaspoon": 0.0048,
        "quart": 1.0, #liter
        "quarts": 1.0,
        "ounce": 0.03, #kilogramm
        "ounces": 0.03,
        "slice": 0.05,
        "slices": 0.05,
        "gramms": 0.001,
        "gramm": 0.001,
        "kilogramm": 1.0,
        "kilogramms": 1.0,
        "gramms": 0.001,
        "gramm": 0.001,
        "millilitres": 0.001,
        "milliliters": 0.001,
        "l": 1.0,
        "ml": 0.001,
        "g": 0.001,
        "kg": 1.0,
        "pounds": 0.5,
        "pounds": 0.5,
        "pounds": 0.5,
        "pound": 0.5}

    energyfootprintTable = {"Almond milk":1.09,
        "Almonds":26.31,
        "Beef":164.22,
        "Cheese slices":35.50,
        "Cheese spread":26.71,
        "Chicken":64.14,
        "Chocolate":90.25,
        "Chocolate milk":26.92,
        "Corn":1.88,
        "Dried Beef": 164.22,
        "Dry Pasta":17.23,
        "Fresh ravioli with meat":66.22,
        "Fresh ravioli with spinach and ricotta":20.38,
        "Gruyére":35.50,
        "Ham":91.40,
        "Lentils":5.67,
        "Low fat organic milk":1.39,
        "Non-free range eggs":36.10,
        "Pancetta":91.40,
        "Pork":91.40,
        "Pork sausages":91.40,
        "Quorn":1.88,
        "Red kidney beans":5.67,
        "Rice milk":0.26,
        "Risotto rice":5.43,
        "Sliced beef":164.22,
        "Sliced chicken":64,
        "Smoked cheese":26.71,
        "Spaghetti Carbonara pre-made meal":28.52,
        "Tofu":14.37,
        "UHT milk":5.82,
        "Vegetarian salami":1.88,
        "Wholegrain dry pasta":17.23,
        "Lamb":56.28,
        "Butter":5.21,
        "Turkey":60.14,
        "Rabbit":40.13,
        "Cod":3.49,
        "Eggs":3.85,
        "Insect":2.3,
        "Whole Milk":1.4,
        "Wheat":0.51,
        "Peas":0.6,
        "Barley":0.52,
        "Chickpeas":64.14}

    waterfootprintTable = {"Almond milk":1.09,
        "Almonds":1.90,
        "Beef":0.47,
        "Cheese slices":0.15,
        "Cheese spread":0.11,
        "Chicken":0.34,
        "Chocolate":0.38,
        "Chocolate milk":0.11,
        "Corn":0.06,
        "Dried Beef": 0.47,
        "Dry Pasta":0.01,
        "Fresh ravioli with meat":0.16,
        "Fresh ravioli with spinach and ricotta":0.04,
        "Gruyére":0.15,
        "Ham":0.52,
        "Lentils":0.14,
        "Low fat organic milk":0.00,
        "Non-free range eggs":0.18,
        "Pancetta":0.52,
        "Pork":0.52,
        "Pork sausages":0.52,
        "Quorn":0.06,
        "Red kidney beans":0.14,
        "Rice milk":0.26,
        "Risotto rice":0.35,
        "Sliced beef":0.47,
        "Sliced chicken":0.34,
        "Smoked cheese":0.11,
        "Spaghetti Carbonara pre-made meal":0.11,
        "Tofu":0.00,
        "UHT milk":0.02,
        "Vegetarian salami":0.06,
        "Wholegrain dry pasta":0.01,
        "Lamb":0.85,
        "Butter":0.19,
        "Turkey":0.49,
        "Rabbit":0.29,
        "Cod":1.24,
        "Eggs":0.78,
        "Insect":0.17,
        "Whole Milk":0.44,
        "Wheat":0.18,
        "Peas":0.19,
        "Barley":0.13,
        "Chickpeas":0.41}

    co2footprintTable = {"Almond milk":1.09,
        "Almonds":2.18,
        "Beef":27.76,
        "Cheese slices":8.29,
        "Cheese spread":6.20,
        "Chicken":6.82,
        "Chocolate":14.67,
        "Chocolate milk":4.65,
        "Corn":0.19,
        "Dried Beef": 27.76,
        "Dry Pasta":1.49,
        "Fresh ravioli with meat":10.25,
        "Fresh ravioli with spinach and ricotta":3.06,
        "Gruyére":8.29,
        "Ham":10.76,
        "Lentils":0.78,
        "Low fat organic milk":1.11,
        "Non-free range eggs":3.94,
        "Pancetta":10.76,
        "Pork":10.76,
        "Pork sausages":10.76,
        "Quorn":0.19,
        "Red kidney beans":0.78,
        "Rice milk":0.26,
        "Risotto rice":1.03,
        "Sliced beef":27.76,
        "Sliced chicken":6.8,
        "Smoked cheese":6.20,
        "Spaghetti Carbonara pre-made meal":3.44,
        "Tofu":3.23,
        "UHT milk":1.31,
        "Vegetarian salami":0.19,
        "Wholegrain dry pasta":1.49,
        "Lamb":25.44,
        "Butter":11.52,
        "Turkey":5.9,
        "Rabbit":3.61,
        "Cod":3.49,
        "Eggs":3.4,
        "Insect":2.3,
        "Whole Milk":1.4,
        "Wheat":0.51,
        "Peas":0.6,
        "Barley":0.52,
        "Chickpeas":0.67}
    predictor = 0
    def __init__(self):
        self.predictor = predict_ingredients.Predictor()
    def parse(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        ingredients = soup.find_all("span", itemprop="recipeIngredient")
        ingredientsArray = []
        recipe = dict()
        for i in ingredients:
            ingredientsText = i.text
            offset = 0

            dataId = int(i["data-id"])

            if dataId == 0:
                continue
            if("(" in ingredientsText.split(" ")[1]):

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
                    if ingredientsText.split(" ")[1+offset] in self.unitConversionTable:
                        unit =  ingredientsText.split(" ")[1+offset]
                        offset = offset + 1
                    name = " ".join(ingredientsText.split(" ")[1+offset:])
            costs = self.classify(name, unit, quantity)
            ingredientsArray.append({"name": name, "unit":unit, "quantity":quantity, "costs": costs})

        recipe["ingredients"] = ingredientsArray
        recipe["title"] = soup.select("#recipe-main-content")[0].text

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


        if predictedIngredient in self.co2footprintTable:
            mass = -1;
            if unit in self.unitConversionTable:
                mass = quantity*self.unitConversionTable[unit]

            #calculate footprint
            if mass > 0:
                co2Footprint = self.co2footprintTable[predictedIngredient]*mass
                waterFootprint = self.waterfootprintTable[predictedIngredient]*mass
                energyFootprint = self.energyfootprintTable[predictedIngredient]*mass
            else:
                co2Footprint = 0.123456789
        else:
            co2Footprint = 0.123456789


        return dict(
                co2=co2Footprint,
                water=waterFootprint,
                energy=energyFootprint
        )
