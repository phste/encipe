import {observable, computed, asStructure, decorate} from 'mobx';

export class Recipe {

    constructor(root) {
        this.rootStore = root
        this.rootStore.api.subscribe("recipe_loaded", this.recipeLoaded.bind(this))
        this.rootStore.api.subscribe("recipe_cleared", this.recipeCleared.bind(this))

        this.recipe = {
            title: "",
            ingredients: [],
        }
    }

    recipeLoaded(recipe) {
        this.recipe = recipe
    }

    recipeCleared() {
        this.recipe = {
            title: "",
            ingredients: [],
        }
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

    get drivableCarKm() {
        let lphk = 9 // Liters per 100km
        let kgco2 = 3.09 // 2.5 for petrol driven car https://www.co2online.de/klima-schuetzen/mobilitaet/auto-co2-ausstoss/
        let co2cost = this.totalCosts["co2"]

        return (co2cost / kgco2) / lphk * 100;
    }

    get trinkingDays() {
        let liters_per_day = 2.5
        let water_cost = this.totalCosts["water"] * 1000

        return (water_cost / liters_per_day);
    }
}

decorate(Recipe, {
    recipe: observable,
    totalCosts: computed,
    drivableCarKm: computed,
    trinkingDays: computed
})