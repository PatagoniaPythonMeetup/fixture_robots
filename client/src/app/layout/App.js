import React from 'react';
import logo from './logo.svg';
import {Header, Container} from "semantic-ui-react";
import Relay from 'react-relay';

import TabBarContainer from "features/tabs/TabBarContainer";
import Robots from "features/robots/Robots";
import Rondas from "features/rondas/Rondas";
import Encuentros from "features/encuentros/Encuentros"

import './App.css';

const Fixture = () => <div>Fixture</div>;

class App extends React.Component {
  render() {
    const tabs = [
      {name: "fixture", label: "Fixture", component: Fixture},
      {name: "robots", label: "Robots", component: Robots},
      {name: "rondas", label: "Rondas", component: Rondas},
      {name: "encuentros", label: "Encuentros", component: Encuentros}
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

export default Relay.createContainer(App, {
  fragments: {
    robots: () => Relay.QL`fragment on Robot {
        key
        nombre
        escuela
        encargado
        score
      }
    `,
  }
});
