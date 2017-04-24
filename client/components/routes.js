import React from 'react';

import FirstPage from './FirstPage';
import SecondPage from './SecondPage';
import PosicionesPage from './PosicionesPage';
import App from './App';

import {
  Route,
} from 'react-router'

const routes = (
  <App>
    <Route path="/" component={FirstPage}/>
    <Route path="/second" component={SecondPage}/>
    <Route path="/posiciones" component={PosicionesPage}/>
  </App>
);

export { routes };