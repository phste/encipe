import {Recipe} from "./recipe"
import {Api} from "./api"

class Stores {
    constructor() {
        this.api = new Api()
        this.recipe = new Recipe(this)
    }
}

export const stores = new Stores()