import { ApolloQueryObservable } from 'apollo-angular';
import { Injectable, EventEmitter } from '@angular/core';
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
const EncuentrosActualesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/EncuentrosActuales.graphql');
const RondasQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Rondas.graphql');
const RondaActualQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/RondaActual.graphql');

const GenerarRondaMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRonda.graphql');
const GanaRobotMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GanaRobot.graphql');

@Injectable()
export class FixtureService {
  estado: EventEmitter<any> = new EventEmitter()

  constructor(private apollo: Apollo) { }
  
  actualizarEstado() {
    return this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
      .subscribe(result => this.estado.emit(this.estado));
  }

  robots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode})
      .map(result => result.data.fixture.robots);
  }

  robot(key: String) {
    return this.apollo.watchQuery<RobotQuery>({ 
      query: RobotQueryNode,
      variables: { key }
    })
      .map(result => result.data.fixture.robot as any) as ApolloQueryObservable<any>;
  }

  ronda(numero: Number) {
    return this.apollo.watchQuery<RondaQuery>({ 
      query: RondaQueryNode,
      variables: { numero }
    })
      .map(result => result.data.fixture.ronda as any) as ApolloQueryObservable<any>;
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
    let obs$ = this.apollo.mutate<GenerarRondaMutation>({
      mutation: GenerarRondaMutationNode,
      variables: { tct },
    })
    obs$.subscribe(({data}) => this.estado.emit(data.generarRonda.estado));
    return obs$.map(({data}) => data.generarRonda.ronda );
  }

  ganaRobot(key: String, ronda: Number = null, encuentro: Number = null) {
    // Llamando a la mutacion generar ronda
    let obs$ = this.apollo.mutate<GanaRobotMutation>({
      mutation: GanaRobotMutationNode,
      variables: { key },
    })
    obs$.subscribe(({data}) => this.estado.emit(data.ganaRobot.estado));
    return obs$.map(({data}) => data.ganaRobot.encuentro );
  }
}
