import React, {Component} from "react";

import {
  Segment,
  Header,
} from "semantic-ui-react";

import RobotsList from "../RobotsList";

const robots = [
  {
  "nombre": "Ultron",
  "escuela": "Los Avengers",
  "encargado": "Nick Fury",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Wall-e",
  "escuela": "Pixar",
  "encargado": "Sr. Disney",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "EVA",
  "escuela": "Pixar",
  "encargado": "Sr. Disney",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Rodney",
  "escuela": "Robots",
  "encargado": "Sr. Ewan McGregor",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Sony",
  "escuela": "R&H Mecanicos",
  "encargado": "Dt. Spooner",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Robocop",
  "escuela": "O.C.P.",
  "encargado": "Bob Morthon",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "ED 209",
  "escuela": "O.C.P.",
  "encargado": "Bob Morthon",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Johnny 5",
  "escuela": "Cortocircuito",
  "encargado": "Ally Sheedy",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "T-800",
  "escuela": "Cyberdyne Systems",
  "encargado": "Jhon Connor",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "T-1000",
  "escuela": "Cyberdyne Systems",
  "encargado": "Arnie",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "R2-D2",
  "escuela": "La Republica",
  "encargado": "Obiwan Kenobi",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "3-CPO",
  "escuela": "La Republica",
  "encargado": "Anakin Skywalker",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "BB-8",
  "escuela": "La Republica",
  "encargado": "Poe Dameron",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Roy Batty",
  "escuela": "Blade Runner",
  "encargado": "Roy",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "HAL 9000",
  "escuela": "Discovery Uno",
  "encargado": "David Bowman",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Ash",
  "escuela": "Nostromo",
  "encargado": "Ellen Ripley",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Optimus Prime",
  "escuela": "Transformers",
  "encargado": "Ellen Ripley",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "David Swinton",
  "escuela": "IA",
  "encargado": "Ellen Ripley",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Teddy",
  "escuela": "IA",
  "encargado": "Haley Joel Osment",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Centinelas",
  "escuela": "Matrix",
  "encargado": "Neo",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  },
  {
  "nombre": "Bender",
  "escuela": "Futurama",
  "encargado": "Philip J. Fry",
  "score": [
      0, 0, 0, 0, 0, 0, 0, 0
  ]
  }
  ];

export default class Robots extends Component {
  state = {
    robots
  }
  render() {
    const {robots} = this.state;
    return (
      <Segment>
        <Header as="h3">Robots</Header>
        <RobotsList robots={robots}/>
      </Segment>
      );
  }
}