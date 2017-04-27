import React, {Component} from "react";

import {
  Container,
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
      <Container>
        <Header as="h3">Rondas</Header>
        {rondaRows}
      </Container>
      );
  }
}