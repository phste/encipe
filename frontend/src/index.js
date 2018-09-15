import React from "react";
import ReactDOM from "react-dom";
import SearchBar from "./components/searchbar";
import "./css/main.less";

const Index = () => {
  return <div className="uk-container" style={{marginTop: "2rem"}}>
            <h1>RecipeCheck</h1>
            <span>
                <p>
                    Every meal we eat has an environmental cost associated to it.
                </p>
            </span>
            <SearchBar/>
        </div>
};

ReactDOM.render(<Index />, document.getElementById("index"));