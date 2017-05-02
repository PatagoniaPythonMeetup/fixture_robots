import React from 'react';
import ReactDOM from 'react-dom';
import Relay from 'react-relay';
import "semantic-ui-css/semantic.css";

import App from './app/layout/App';
import AppRoute from './routes/AppRoute';

Relay.injectNetworkLayer(
  new Relay.DefaultNetworkLayer('http://localhost:5000/fixture', {
    credentials: 'same-origin',
  })
);

ReactDOM.render(
  <Relay.RootContainer
    Component={App}
    route={new AppRoute()}
  />,
  document.getElementById('root')
);
