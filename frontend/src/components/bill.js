import React from "react";
import {observer} from "mobx-react"
import Visualization from "./visualization"

class IngredientEntry extends React.Component {
    render() {
        return <div className="uk-grid-small" uk-grid="true">
            <div className="uk-width-expand" uk-leader="fill: .">{this.props.ingredient.quantity} {this.props.ingredient.unit} {this.props.ingredient.name}</div>
            <div>{(this.props.ingredient.costs[this.props.type.key] * this.props.type.multiplier).toFixed(2)} {this.props.type.unit}</div>
        </div>
    }
}

class DataSelector extends React.Component {
    constructor(props) {
        super(props)
        this.co2 = this.co2.bind(this)
        this.water = this.water.bind(this)
        this.energy = this.energy.bind(this)
    }

    co2() {
        this.props.onTypeChange("co2")
    }

    water() {
        this.props.onTypeChange("water")
    }

    energy() {
        this.props.onTypeChange("energy")
    }


    render() {
        return <div className="data-selector">
            <a href="#" onClick={this.co2}>CO<sub>2</sub></a> | <a href="#" onClick={this.water}>Water</a> | <a href="#" onClick={this.energy}>Energy</a>
        </div>
    }
}

const IngredientsList = observer(class IngredientsList extends React.Component {

    constructor(props) {
        super(props);

        this.types = {
            co2: {
                name: <span>CO<sub>2</sub></span>,
                key: "co2",
                unit: <span>kg CO<sub>2</sub></span>,
                multiplier: 1
            },
            water: {
                name: "Water",
                key: "water",
                unit: "l",
                multiplier: 1000
            },
            energy: {
                name: "Energy",
                key: "energy",
                unit: "MJ",
                multiplier: 1
            }
        }

        this.state = {
            type: "co2"
        }

        this.handleTypeChange = this.handleTypeChange.bind(this)
    }

    handleTypeChange(type) {
        console.log(type)
        this.setState({"type": type})
    }

    createItems() {
        let ingredients = this.props.stores.recipe.recipe.ingredients
        return ingredients.map((i) => <IngredientEntry key={i.name} ingredient={i} type={this.types[this.state.type]}/>)
    }

    render() {
        return  <div>
                    <h3>Environmental Bill for {this.props.stores.recipe.recipe.title}</h3>
                    <DataSelector onTypeChange={this.handleTypeChange}/>
                    <div className="ingredients-list">
                        {this.createItems()}
                    </div>
                    <div className="uk-grid-small" uk-grid="true">
                        <div className="uk-width-expand" uk-leader="fill:  "></div>
                        <div><b>{(this.props.stores.recipe.totalCosts[this.types[this.state.type].key] * this.types[this.state.type].multiplier).toFixed(2)} {this.types[this.state.type].unit}</b></div>
                    </div>
                </div>;
    }
})

const Bill = observer(class Bill extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        let classes = 'ingredients'

        if (this.props.stores.recipe.recipe.ingredients.length > 0) {
            classes += ' show'
        }

        return  <div className={classes}>
                    <div uk-grid="true">
                        <div className="uk-width-1-2@m"><Visualization stores={this.props.stores}/></div>
                        <div className="uk-width-1-2@m"><IngredientsList stores={this.props.stores}/></div>
                    </div>
                </div>
    }
})

export default Bill