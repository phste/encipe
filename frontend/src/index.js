import React from "react";
import ReactDOM from "react-dom";
import SearchBar from "./components/searchbar";
import IngredientsList from "./components/ingredients";
import UIKit from "../node_modules/uikit/dist/js/uikit";
import "./css/main.less";
import {stores} from "./stores"


class Encipe extends React.Component {

    render() {
        return <div className="encipe">
                <SearchBar stores={stores}/>
                <IngredientsList stores={stores}/>
            </div>
    }
}

const Index = () => {
  return <div className="uk-container" style={{marginTop: "2rem"}}>
            <Encipe/>
        </div>
};

ReactDOM.render(<Index />, document.getElementById("index"));