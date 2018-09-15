import React from "react";

export default class SearchBar extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      url: ''
    }

    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(event) {

    this.setState({url: event.target.value});

    let pattern = /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;

    if(pattern.test(event.target.value)) {
      this.props.stores.api.getRecipe(event.target.value)
    }
  }

  render() {
    return <div className="searchbar">
            <h2>encipe <span>check the environmental impact of a recipe</span></h2>
            <input className="uk-input" type="text" value={this.state.url} onChange={this.handleChange} placeholder="Paste in the recipe url..."/>
          </div>;
  }
}