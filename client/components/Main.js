import React, { Component } from 'react';
import { Container } from 'semantic-ui-react'
import PropTypes from 'prop-types';

import { Route, Router } from 'react-router'
import { Link } from 'react-router-dom';
import { Menu } from 'semantic-ui-react'
import createBrowserHistory from 'history/createBrowserHistory'

import IndexPage from './IndexPage';
import PosicionesPage from './PosicionesPage';

import { Provider } from 'react-redux';

const history = createBrowserHistory()

class Main extends Component {
  state = {}
  
  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state
    return (
      <Container>
        <Provider store={ this.props.store }>
            <Menu history={history}>
              <Menu.Item header>Hackathon</Menu.Item>
              <Menu.Item as={Link} to="/" name='index' active={activeItem === 'index'} onClick={this.handleItemClick} />
              <Menu.Item as={Link} to='/posiciones' name='posiciones' active={activeItem === 'posiciones'} onClick={this.handleItemClick} />
            </Menu>
        </Provider>
      </Container>
    );
  }
}

Main.propTypes = {
  store: PropTypes.object.isRequired,
}

export default Main;