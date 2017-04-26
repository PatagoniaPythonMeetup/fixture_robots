import React, { Component } from 'react';
import logo from './logo.svg';
import {
  Header,
  Container
} from "semantic-ui-react";

import TabBarContainer from "features/tabs/TabBarContainer";
import Robots from "features/robots/Robots";

import './App.css';

const Fixture = () => <div>Fixture</div>;
const Rondas = () => <div>Rondas</div>;

class App extends Component {
  render() {
    const tabs = [
      {name: "fixture", label: "Fixture", component: Fixture},
      {name: "robots", label: "Robots", component: Robots},
      {name: "rondas", label: "Rondas", component: Rondas}
    ];
    return (
      <div className="App">
        <div className="App-header">
          <Header inverted as="h1">Campeonato de Robótica y Hackathon</Header>
          <img src={logo} className="App-logo" alt="logo" />
        </div>
        <Container>
          <TabBarContainer tabs={tabs} size="massive" />
        </Container>
      </div>
    );
  }
}

export default App;