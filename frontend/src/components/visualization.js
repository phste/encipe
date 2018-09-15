import React from "react";
import {observer} from "mobx-react"

const Visualization = observer(class Visualization extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return <div>
            <h3>Imagine...</h3>
            <p>cooking this food is equal to the use or production of</p>
            <div class="co2">
                <div class="clouds">
                    <span>{this.props.stores.recipe.drivableCarKm.toFixed(2)} km</span>
                    <img src="http://localhost:8000/cloud.svg"/>
                </div>
                <div class="car">
                    <img src="http://localhost:8000/car.svg"/>
                </div>
            </div>
        </div>;
    }
})

export default Visualization