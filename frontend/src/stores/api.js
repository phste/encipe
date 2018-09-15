import React from "react"
import {config} from "../config"

export class Api {
    
    constructor() {
        this.events = {
            "recipe_loaded": [],
            "recipe_cleared": []
        }
    }

    fireEvent(event, data) {
        this.events[event].forEach(function(cb) {
            cb(data)
        })
    }

    receivedRecipe(data) {
       this.fireEvent("recipe_loaded", data)
    }

    getRecipe(url) {
        this.fireEvent("recipe_cleared", null)
        var formData = new FormData()
        formData.append('url', url)
        fetch(config.apiServer + "recipe", {
            method: 'POST', // or 'PUT'
            body: formData,
        })
        .then((resp) => resp.json())
        .then(this.receivedRecipe.bind(this))
        .catch(error => console.error('Error:', error))
    }

    subscribe(event, callback) {
        this.events[event].push(callback);
    }

}