import React, { Component } from 'react';
import { Button, Container, Header } from 'semantic-ui-react'

class App extends Component {
  render() {
    return (<Container>
        { this.props.children }
    </Container>);
  }
}

export default App;
