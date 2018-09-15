import React from "react";
import {observer} from "mobx-react"

const Visualization = observer(class Visualization extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            classes: 'co2'
        }
    }

    componentWillUpdate() {
        setTimeout(
            function() {
                if (this.props.stores.recipe.recipe.ingredients.length > 0) {
                    this.setState({classes: 'co2 show'})
                } else {
                    this.setState({classes: 'co2'})
                }
            }
            .bind(this),
            1000
        );
    }

    render() {

        return <div>
            <h3>Imagine...</h3>
            <p>cooking this food is equal to the use or production of</p>
            <div className={this.state.classes}>
                <div className="clouds">
                    <span>{this.props.stores.recipe.drivableCarKm.toFixed(2)} km</span>
                    <img src="http://localhost:8000/cloud.svg"/>
                </div>
                <div className="car">
                    <img src="http://localhost:8000/car.svg"/>
                </div>
            </div>
        </div>;
    }
})

export default Visualization