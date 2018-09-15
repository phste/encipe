from sanic import Sanic
from sanic.response import json

from scrap import parse

app = Sanic()

@app.post('/api/recipe')
def parse_recipe(request):
    url = request.form['url'][0]
    recipe = parse(url)
    
    return json(recipe)

if __name__ == '__main__':
    app.static('/', '../frontend/dist')
    app.run(host='0.0.0.0', port=8000)