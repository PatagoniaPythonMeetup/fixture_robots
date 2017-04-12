import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { Router } from 'react-router'
import createBrowserHistory from 'history/createBrowserHistory'

import { routes } from './routes';

import { Provider } from 'react-redux';

const history = createBrowserHistory()

class Main extends Component {
  render() {
    return (
      <Provider store={ this.props.store }>
        <Router history={history}>
          { routes }
        </Router>
      </Provider>
    );
  }
}

Main.propTypes = {
  store: PropTypes.object.isRequired,
}

export default Main;