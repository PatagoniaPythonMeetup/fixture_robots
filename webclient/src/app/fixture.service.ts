import { Observable } from 'rxjs/Rx';
import { IfObservable } from 'rxjs/observable/IfObservable';
import { Injectable } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import { RobotsQuery } from '../graphql/schema';
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');

@Injectable()
export class FixtureService {

  constructor(private apollo: Apollo) { }

  getRobots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(result => result.data.fixture.robots) as Observable<any>;
  }

}
