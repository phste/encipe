from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin

from scrap import Parser



app = Sanic()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
parser = Parser()

@app.post('/api/recipe')
def parse_recipe(request):
    url = request.form['url'][0]
    recipe = Parser.parse(url)

    return json(recipe)

if __name__ == '__main__':
    app.static('/', '../frontend/dist')
    app.run(host='0.0.0.0', port=8000)
