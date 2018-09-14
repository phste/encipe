from bs4 import BeautifulSoup
import requests
import json
def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    ingredients = soup.find_all("span",itemprop="recipeIngredient")
    ingredientsDict = {}
    for i in ingredients:
        ingredientsText = i.text
        quantity = ingredientsText.split(" ")[0]
        unit = None
        name = ""
        possibleUnits = ["cup", "teaspoon", "tablespoon","cups", "teaspoons", "tablespoons", "quart", "quarts" ]
        if ingredientsText.split(" ")[1] in possibleUnits:
            unit =  ingredientsText.split(" ")[1]
            name = " ".join(ingredientsText.split(" ")[2:])
        else:
            name = " ".join(ingredientsText.split(" ")[1:])
        ingredientsDict[name] = {"unit":unit, "quantity":quantity}
    jsonDump = json.loads(json.dumps(ingredientsDict))
    print(type(jsonDump))
    return jsonDump

def classify(ingredients):
    jsonIngredients = json.loads(json.dumps(ingredients))
    for ingredient in jsonIngredients:
        print(ingredient)
