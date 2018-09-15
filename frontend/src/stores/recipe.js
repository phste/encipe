import {observable, computed, asStructure, decorate} from 'mobx';

export class Recipe {

    constructor(root) {
        this.rootStore = root
        this.rootStore.api.subscribe("recipe_loaded", this.recipeLoaded.bind(this))

        this.recipe = {
            title: "",
            ingredients: [],
        }
    }

    recipeLoaded(recipe) {
        this.recipe = recipe
    }

    get totalCosts() {
        return this.recipe.ingredients.reduce(
            function(acc, ingredient) {
                return {
                    "co2": acc.co2 + ingredient.costs.co2,
                    "water": acc.water + ingredient.costs.water,
                    "energy": acc.energy + ingredient.costs.energy
                }
            }, {"co2": 0, "water": 0, "energy": 0}
        )
    }
}

decorate(Recipe, {
    recipe: observable,
    totalCosts: computed
})