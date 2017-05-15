import { ApolloQueryObservable } from 'apollo-angular';
import { Injectable } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import {
    EncuentrosActualesQuery,
    RobotsQuery,
    RobotsScoreQuery,
    RondaActualQuery,
    RondasQuery,
    GenerarRondaMutation,
    GanaRobotMutation
} from '../graphql/schema';
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');
const EncuentrosActualesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/EncuentrosActuales.graphql');
const RobotsScoreQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RobotsScore.graphql');
const RondasQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Rondas.graphql');
const RondaActualQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RondaActual.graphql');
const GenerarRondaMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRonda.graphql');
const GanaRobotMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GanaRobot.graphql');

@Injectable()
export class FixtureService {

  constructor(private apollo: Apollo) { }

  robots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(result => result.data.fixture.robots);
  }

  rondas() {
    return this.apollo.watchQuery<RondasQuery>({ query: RondasQueryNode})
      .map(result => result.data.fixture.rondas as any) as ApolloQueryObservable<any>;
  }

  rondaActual() {
    return this.apollo.watchQuery<RondaActualQuery>({ query: RondaActualQueryNode})
      .map(result => result.data.fixture.rondaActual);
  }

  encuentrosActuales() {
    return this.apollo.watchQuery<EncuentrosActualesQuery>({ query: EncuentrosActualesQueryNode})
      .map(result => result.data.fixture.encuentrosActuales);
  }

  robotsScore() {
    return this.apollo.watchQuery<RobotsScoreQuery>({ query: RobotsScoreQueryNode})
      .map(result => result.data.fixture.robots);
  }

  generarRonda(tct: Boolean) {
    // Llamando a la mutacion generar ronda
    return this.apollo.mutate<GenerarRondaMutation>({
        mutation: GenerarRondaMutationNode,
        variables: { tct },
      })
      .map(({data}) => data.generarRonda.ronda );
  }

  ganaRonda(key: String, ronda: Number = null, encuentro: Number = null) {
    // Llamando a la mutacion generar ronda
    return this.apollo.mutate<GanaRobotMutation>({
        mutation: GanaRobotMutationNode,
        variables: { key },
      })
      .map(({data}) => data.ganaRobot.encuentro );
  }
}
