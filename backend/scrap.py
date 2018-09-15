from bs4 import BeautifulSoup
import requests
import json
import predict_ingredients

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

co2footprintTable = {"Beef":27.76,
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
                if ingredientsText.split(" ")[1+offset] in unitConversionTable:
                    unit =  ingredientsText.split(" ")[1+offset]
                    offset = offset + 1
                name = " ".join(ingredientsText.split(" ")[1+offset:])
        costs = classify(name, unit, quantity)
        ingredientsArray.append({"name": name, "unit":unit, "quantity":quantity, "costs": costs})

    recipe["ingredients"] = ingredientsArray
    recipe["title"] = soup.select("#recipe-main-content")[0].text

    return recipe

def classify(ingredient, unit, quantity):
    ingredient = ingredient.lower()
    co2Footprint = 10
    waterFootprint = 0
    energyFootprint = 0
    predictedIngredient = predict_ingredients.predict([ingredient])[0]

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


    if predictedIngredient in co2footprintTable:
        mass = -1;
        if unit in unitConversionTable:
            mass = quantity*unitConversionTable[unit]

        #calculate footprint
        if mass > 0:
            co2Footprint = co2footprintTable[predictedIngredient]*mass
        else:
            co2Footprint = 0.123456789
    else:
        co2Footprint = 0.123456789


    return dict(
            co2=co2Footprint,
            water=waterFootprint,
            energy=energyFootprint
    )