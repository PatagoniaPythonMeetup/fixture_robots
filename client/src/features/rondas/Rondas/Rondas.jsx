import React, {Component} from "react";

import {
  Segment,
  Header,
} from "semantic-ui-react";

import {Ronda} from "features/rondas/Ronda";

const rondas = [];

export default class Rondas extends Component {
  state = {
    rondas
  }
  
  render() {
    const {rondas} = this.state;

    const rondaRows = rondas.map(ronda => (
      <Ronda ronda={ronda}/>
    ));

    return (
      <Segment>
        <Header as="h3">Rondas</Header>
        {rondaRows}
      </Segment>
      );
  }
}