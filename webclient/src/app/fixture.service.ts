import { Observable } from 'rxjs/Rx';
import { ApolloQueryObservable } from 'apollo-angular';
import { Injectable, EventEmitter } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import {
    RobotsQuery,
    RobotsScoreQuery,
    RondasQuery,
    EncuentroQuery,
    GenerarRondaMutation,
    GanaRobotMutation,
    RobotQuery,
    RondaQuery,
    FixtureQuery
} from '../graphql/schema';
const FixtureQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Fixture.graphql');
const RobotQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robot.graphql');
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');
const RondaQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Ronda.graphql');
const RobotsScoreQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RobotsScore.graphql');
const RondasQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Rondas.graphql');
const EncuentroQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Encuentro.graphql');

const GenerarRondaMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRonda.graphql');
const GanaRobotMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GanaRobot.graphql');

export interface Estado {
  iniciado: Boolean
  compitiendo: Boolean
  finalizado: Boolean
  vuelta: Number
  jugadas: Number
  encuentros: Array<Number>
  ronda: Number
}

let ESTADO_INICIAL: Estado = {
  iniciado: false, compitiendo: false, finalizado: false, vuelta: 0, jugadas: 0, encuentros: [], ronda: 0
}

@Injectable()
export class FixtureService {
  
  constructor(private apollo: Apollo) {
  }
  
  getEstado() {
    return this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
      .map(({data}) => data.fixture.estado)
  }

  robots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(({data}) => data.fixture.robots);
  }

  robot(key: String) {
    return this.apollo.watchQuery<RobotQuery>({ 
      query: RobotQueryNode,
      variables: { key }
    })
      .map(({data}) => data.fixture.robot as any) as ApolloQueryObservable<any>;
  }

  ronda(numero: Number) {
    return this.apollo.watchQuery<RondaQuery>({ 
      query: RondaQueryNode,
      variables: { numero }
    })
      .map(({data}) => data.fixture.ronda as any) as ApolloQueryObservable<any>;
  }

  rondas() {
    return this.apollo.watchQuery<RondasQuery>({ query: RondasQueryNode})
      .map(({data}) => data.fixture.rondas as any) as ApolloQueryObservable<any>;
  }

  encuentro(numero: Number) {
    return this.apollo.watchQuery<EncuentroQuery>({ 
      query: EncuentroQueryNode,
      variables: { numero }
    })
      .map(({data}) => data.fixture.encuentro as any) as ApolloQueryObservable<any>;
  }

  robotsScore() {
    return this.apollo.watchQuery<RobotsScoreQuery>({ query: RobotsScoreQueryNode})
      .map(({data}) => data.fixture.robots);
  }

  generarRonda(tct: Boolean) {
    // Llamando a la mutacion generar ronda
    return this.apollo.mutate<GenerarRondaMutation>({
      mutation: GenerarRondaMutationNode,
      variables: { tct },
    })
    .map(({data}) => data.generarRonda.ronda);
  }

  ganaRobot(key: String, ronda: Number = null, encuentro: Number = null) {
    // Llamando a la mutacion generar ronda
    return this.apollo.mutate<GanaRobotMutation>({
      mutation: GanaRobotMutationNode,
      variables: { key },
    })
    .map(({data}) => data.ganaRobot.encuentro );
  }
}
