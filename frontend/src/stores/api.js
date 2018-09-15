import React from "react"
import {config} from "../config"

export class Api {
    
    constructor() {
        this.events = {
            "recipe_loaded": []
        }
    }

    receivedRecipe(data) {
        this.events["recipe_loaded"].forEach(function(cb) {
            cb(data)
        })
    }

    getRecipe(url) {
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