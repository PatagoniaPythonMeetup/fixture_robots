import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { Router } from 'react-router'
import { Menu } from 'semantic-ui-react'
import createBrowserHistory from 'history/createBrowserHistory'

import { routes } from './routes';

import { Provider } from 'react-redux';

const history = createBrowserHistory()

class Main extends Component {
  state = {}
  
  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state
    return (
      <Provider store={ this.props.store }>
        <Router history={history}>
          <Menu>
            <Menu.Item header>Hackathon</Menu.Item>
            <Menu.Item name='aboutUs' active={activeItem === 'aboutUs'} onClick={this.handleItemClick} />
            <Menu.Item name='jobs' active={activeItem === 'jobs'} onClick={this.handleItemClick} />
            <Menu.Item name='locations' active={activeItem === 'locations'} onClick={this.handleItemClick} />
            { routes }
          </Menu>
        </Router>
      </Provider>
    );
  }
}

Main.propTypes = {
  store: PropTypes.object.isRequired,
}

export default Main;