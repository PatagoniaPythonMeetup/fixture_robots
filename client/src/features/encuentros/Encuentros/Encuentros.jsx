import React, {Component} from "react";

import Encuentro from "./Encuentro";

const encuentros = [ {}, {} ];

export default class Encuentros extends Component {
  state = {
    encuentros
  }
  
  render() {
    const {encuentros} = this.state;

    const encuentroRows = encuentros.map(encuentro => (
      <Encuentro encuentro={encuentro}/>
    ));    

    return (
      <div>{encuentroRows}</div>
      );
  }
}