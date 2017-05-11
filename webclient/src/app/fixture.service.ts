import { Observable } from 'rxjs/Rx';
import { IfObservable } from 'rxjs/observable/IfObservable';
import { Injectable } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import {
    EncuentrosActualesQuery,
    RobotsQuery,
    RobotsScoreQuery,
    RondaActualQuery,
    RondasQuery
} from '../graphql/schema';
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');
const EncuentrosActualesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/EncuentrosActuales.graphql');
const RobotsScoreQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RobotsScore.graphql');
const RondasQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Rondas.graphql');
const RondaActualQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RondaActual.graphql');

@Injectable()
export class FixtureService {

  constructor(private apollo: Apollo) { }

  robots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(result => result.data.fixture.robots) as Observable<any>;
  }

  rondas() {
    return this.apollo.watchQuery<RondasQuery>({ query: RondasQueryNode})
      .map(result => result.data.fixture.rondas) as Observable<any>;
  }

  rondaActual() {
    return this.apollo.watchQuery<RondaActualQuery>({ query: RondaActualQueryNode})
      .map(result => result.data.fixture.rondaActual) as Observable<any>;
  }

  encuentrosActuales() {
    return this.apollo.watchQuery<EncuentrosActualesQuery>({ query: EncuentrosActualesQueryNode})
      .map(result => result.data.fixture.encuentrosActuales) as Observable<any>;
  }

  robotsScore() {
    return this.apollo.watchQuery<RobotsScoreQuery>({ query: RobotsScoreQueryNode})
      .map(result => result.data.fixture.robots) as Observable<any>;
  }

}
