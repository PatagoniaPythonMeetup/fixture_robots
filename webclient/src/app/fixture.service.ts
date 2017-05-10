import { Observable } from 'rxjs/Rx';
import { IfObservable } from 'rxjs/observable/IfObservable';
import { Injectable } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import { RobotsQuery, EncuentrosActualesQuery } from '../graphql/schema';
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');
const EncuentrosActualesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/EncuentrosActuales.graphql');

@Injectable()
export class FixtureService {

  constructor(private apollo: Apollo) { }

  getRobots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(result => result.data.fixture.robots) as Observable<any>;
  }

  encuentrosActuales() {
    return this.apollo.watchQuery<EncuentrosActualesQuery>({ query: EncuentrosActualesQueryNode})
      .map(result => result.data.fixture.encuentrosActuales) as Observable<any>;
  }

}
