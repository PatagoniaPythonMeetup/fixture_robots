import React, { Component } from 'react';
import { Button, Container, Header } from 'semantic-ui-react'

class App extends Component {
  render() {
    return (<Container>
      <Header as='h1'>Hola Mundo</Header>
      <div>
        { this.props.children }
      </div>
    </Container>);
  }
}

export default App;
