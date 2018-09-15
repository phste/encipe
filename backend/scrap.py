from bs4 import BeautifulSoup
import requests
import json
def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    recipe = dict()
    ingredients = soup.find_all("span", itemprop="recipeIngredient")
    ingredientsArray = []
    for i in ingredients:
        ingredientsText = i.text
        offset = 0

        dataId = int(i["data-id"])

        if dataId == 0:
            continue
        if("(" in ingredientsText.split(" ")[1]):
            offset = offset + 1
            #todo
        elif("/" in ingredientsText.split(" ")[1]):
            offset = offset + 1
            quantity = " ".join(ingredientsText.split(" ")[0:2])
        else:
            quantity = ingredientsText.split(" ")[0]
        unit = None
        name = ""
        possibleUnits = ["cup", "teaspoon", "tablespoon","cups", "teaspoons", "tablespoons", "quart", "quarts", "ounce", "ounces", "slice", "slices"  ]
        if ingredientsText.split(" ")[1+offset] in possibleUnits:
            unit =  ingredientsText.split(" ")[1+offset]
            offset = offset + 1
        name = " ".join(ingredientsText.split(" ")[1+offset:])
        costs = dict(
                co2=10,
                water=0,
                energy=0
        )
        ingredientsArray.append({"name": name, "unit":unit, "quantity":quantity, "costs": costs})
    
    recipe["ingredients"] = ingredientsArray
    recipe["title"] = soup.select("#recipe-main-content")[0].text

    return recipe

def classify(ingredients):

    unitConversionTable = {"cup": 0.24, #liter
         "cups":0.24,
         "tablespoon": 0.0143, #kilogramm
         "tablespoons": 0.0143,
         "teaspoon": 0.0048, #kilogramm
         "teaspoon": 0.0048,
         "quart": 1.0, #liter
         "quarts": 1.0,
         "ounce": 0.03, #kilogramm
         "ounces": 0.03;
         "slice": 0.05,
         "slices": 0.05}
    co2footprintTable : {"Beef":27.76,
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

    jsonIngredients = json.loads(json.dumps(ingredients))
    co2footprint = 0
    ingredientsCO2Footprint = {}
    for ingredient in jsonIngredients:
        ingredientCO2Footprint = 0

        quantity = jsonIngredients[ingredient]["quantity"]
        unit = jsonIngredients[ingredient]["unit"]
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


        mass = -1;

        if unit in unitConversionTable:
            mass = quantity*unitConversionTable[unit]
        #calculate footprint
        ingredientsCO2Footprint[ingredient] = CO2Footprint

    return json.dumps(ingredientsCO2Footprint)
