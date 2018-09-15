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
        </div>;
    }
})

export default Visualization