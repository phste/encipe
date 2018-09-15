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
            <p>cooking this meal is equal to</p>
            <div className={this.state.classes}>
                <div className="clouds">
                    <span>driving <br/>{this.props.stores.recipe.drivableCarKm.toFixed(2)} km</span>
                    <img src="http://localhost:8000/cloud.svg"/>
                </div>
                <div className="car">
                    <img src="http://localhost:8000/car.svg"/>
                </div>
            </div>
            <div className="water">
                <span>
                    drink <b>2.5l</b> for <br/> <b>{this.props.stores.recipe.trinkingDays.toFixed(0)} days 
                    ({(this.props.stores.recipe.trinkingDays / 356).toFixed(2)} years)</b>
                </span>
                <img src="http://localhost:8000/water.svg"/>
            </div>
            <div className="energy">
                <span>
                    or power a <br/><b>family home</b> for <br/><b>{this.props.stores.recipe.houseElectricDays.toFixed(0)} days</b>
                </span>
                <img src="http://localhost:8000/house.svg"/>
            </div>
        </div>;
    }
})

export default Visualization