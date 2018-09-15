import React from "react";
import {observer} from "mobx-react"
import Visualization from "./visualization"

class IngredientEntry extends React.Component {
    render() {
        return <div className="uk-grid-small" uk-grid="true">
            <div className="uk-width-expand" uk-leader="fill: .">{this.props.ingredient.quantity} {this.props.ingredient.unit} {this.props.ingredient.name}</div>
            <div> {this.props.ingredient.costs["co2"].toFixed(2)} kg CO<sub>2</sub> </div>
        </div>
    }
}

const IngredientsList = observer(class IngredientsList extends React.Component {

    constructor(props) {
        super(props);
    }

    createItems() {
        let ingredients = this.props.stores.recipe.recipe.ingredients
        return ingredients.map((i) => <IngredientEntry key={i.name} ingredient={i}/>)
    }

    render() {
        return  <div>
                    <h3>Environmental Bill for {this.props.stores.recipe.recipe.title}</h3>
                    <div className="ingredients-list">
                        {this.createItems()}
                    </div>
                    <div className="uk-grid-small" uk-grid="true">
                        <div className="uk-width-expand" uk-leader="fill:  "></div>
                        <div><b>{this.props.stores.recipe.totalCosts.co2.toFixed(2)} kg CO<sub>2</sub></b></div>
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
                    <div className="ui-grid-divider" uk-grid="true">
                        <div className="uk-width-1-2@m"><Visualization stores={this.props.stores}/></div>
                        <div className="uk-width-1-2@m"><IngredientsList stores={this.props.stores}/></div>
                    </div>
                </div>
    }
})

export default Bill