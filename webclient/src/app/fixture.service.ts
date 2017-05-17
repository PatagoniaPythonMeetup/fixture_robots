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

export interface Estado {
  iniciado: Boolean
  compitiendo: Boolean
  finalizado: Boolean
  vuelta: Number
  jugadas: Number
}

let ESTADO_INICIAL: Estado = {
  iniciado: false, compitiendo: false, finalizado: false, vuelta: 0, jugadas: 0
}

@Injectable()
export class FixtureService {
  estado: EventEmitter<any> = new EventEmitter()
  _estado: Estado = ESTADO_INICIAL

  constructor(private apollo: Apollo) {
    this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
      .subscribe(({data}) => this.actualizarEstado(data.fixture.estado));
  }
  
  getEstado() {
    return this._estado;
  }

  actualizarEstado(estado) {
    this._estado = estado;
    this.estado.emit(this._estado);
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

  rondaActual() {
    return this.apollo.watchQuery<RondaActualQuery>({ query: RondaActualQueryNode})
      .map(({data}) => data.fixture.rondaActual);
  }

  encuentrosActuales() {
    return this.apollo.watchQuery<EncuentrosActualesQuery>({ query: EncuentrosActualesQueryNode})
      .map(({data}) => data.fixture.encuentrosActuales);
  }

  robotsScore() {
    return this.apollo.watchQuery<RobotsScoreQuery>({ query: RobotsScoreQueryNode})
      .map(({data}) => data.fixture.robots);
  }

  generarRonda(tct: Boolean) {
    // Llamando a la mutacion generar ronda
    let obs$ = this.apollo.mutate<GenerarRondaMutation>({
      mutation: GenerarRondaMutationNode,
      variables: { tct },
    })
    obs$.subscribe(({data}) => this.actualizarEstado(data.generarRonda.estado));
    return obs$.map(({data}) => data.generarRonda.ronda );
  }

  ganaRobot(key: String, ronda: Number = null, encuentro: Number = null) {
    // Llamando a la mutacion generar ronda
    let obs$ = this.apollo.mutate<GanaRobotMutation>({
      mutation: GanaRobotMutationNode,
      variables: { key },
    })
    obs$.subscribe(({data}) => this.actualizarEstado(data.ganaRobot.estado));
    return obs$.map(({data}) => data.ganaRobot.encuentro );
  }
}
