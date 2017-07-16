import { Observable } from 'rxjs/Rx';
import { ApolloQueryObservable } from 'apollo-angular';
import { Injectable, EventEmitter } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import 'rxjs/add/operator/map';

import {
    RobotsQuery,
    RobotFixtureScoreQuery,
    RondasQuery,
    EncuentroQuery,
    GenerarRondasMutation,
    AgregarGanadorMutation,
    QuitarGanadorMutation,
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

const GenerarRondasMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRondas.graphql');
const AgregarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/AgregarGanador.graphql');
const QuitarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/QuitarGanador.graphql');
const GenerarClasificacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarClasificacion.graphql');
const GenerarEliminacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarEliminacion.graphql');
const GenerarFinalMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarFinal.graphql');

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
  estado: EventEmitter<Estado> = new EventEmitter<Estado>()

  constructor(private apollo: Apollo) {
  }
  
  getEstado() {
    let obs$ = this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
      .map(({data}) => data.fixture.estado)
    obs$.subscribe(estado => this.estado.emit(estado))
    return obs$
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
      .map(({data}) => data.fixture.ronda);
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

  generarRonda() {
    // Llamando a la mutacion generar ronda
    let obs$ = this.apollo.mutate<GenerarRondasMutation>({
      mutation: GenerarRondasMutationNode
    })
    obs$.subscribe(({data}) => this.estado.emit(data.generarRondas.estado))
    return obs$.map(({data}) => data.generarRondas.rondas);
  }

  agregarGanador(key: String, encuentro: Number = null) {
    // Llamando a la mutacion agregar a un ganador
    let obs$ = this.apollo.mutate<AgregarGanadorMutation>({
      mutation: AgregarGanadorMutationNode,
      variables: { key, encuentro },
    })
    obs$.subscribe(({data}) => this.estado.emit(data.agregarGanador.estado))
    return obs$.map(({data}) => data.agregarGanador.encuentro );
  }

  quitarGanador(key: String, encuentro: Number = null) {
    // Llamando a la mutacion quitar a un ganador
    let obs$ = this.apollo.mutate<QuitarGanadorMutation>({
      mutation: QuitarGanadorMutationNode,
      variables: { key, encuentro },
    })
    obs$.subscribe(({data}) => this.estado.emit(data.quitarGanador.estado))
    return obs$.map(({data}) => data.quitarGanador.encuentro );
  }
}
