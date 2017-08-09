import { ApolloQueryObservable } from 'apollo-angular';
import { Injectable, EventEmitter } from '@angular/core';
import { Apollo } from "apollo-angular";
import { DocumentNode } from 'graphql';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';

import {
    RobotQuery,
    RobotsQuery,
    RondaQuery,
    RondasQuery,
    ScoreQuery,
    ScoresGeneralQuery,
    FaseQuery,
    FasesQuery,
    EncuentroQuery,
    GenerarClasificacionMutation,
    GenerarEliminacionMutation,
    GenerarFinalMutation,
    GenerarAdhocMutation,
    GenerarRondaMutation,
    AgregarGanadorMutation,
    QuitarGanadorMutation,
    FixtureQuery
} from '../graphql/schema';
const FixtureQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Fixture.graphql');
const RobotQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robot.graphql');
const RobotsQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Robots.graphql');
const RondaQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Ronda.graphql');
const RondasQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Rondas.graphql');
const ScoreQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Score.graphql');
const ScoresGeneralQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/ScoresGeneral.graphql');
const FaseQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Fase.graphql');
const FasesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Fases.graphql');
const EncuentroQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Encuentro.graphql');

const GenerarRondaMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRonda.graphql');
const AgregarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/AgregarGanador.graphql');
const QuitarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/QuitarGanador.graphql');
const GenerarClasificacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarClasificacion.graphql');
const GenerarEliminacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarEliminacion.graphql');
const GenerarFinalMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarFinal.graphql');
const GenerarAdhocMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarAdhoc.graphql');

export interface Estado {
  iniciado: Boolean
  compitiendo: Boolean
  finalizado: Boolean
  jugadas: Number
  encuentros: Array<Number>
  ronda: Number
  seleccion: Array<any>
}

let ESTADO_INICIAL: Estado = {
  iniciado: false,
  compitiendo: false,
  finalizado: false,
  jugadas: 0,
  encuentros: [],
  ronda: 0,
  seleccion: []
}

@Injectable()
export class FixtureService {
  estado: EventEmitter<Estado> = new EventEmitter<Estado>()
  seleccion: Array<any> = []

  constructor(private apollo: Apollo) {
  }
  
  setRobotsSeleccionados(robots) {
    this.seleccion = robots;
    this.getEstado();
  }

  getEstado() {
    let obs$ = this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
    obs$.subscribe(({data}) => this.setEstado(data.fixture.estado))
    return obs$
  }

  setEstado(estado) {
    estado = _.clone(estado);
    estado.seleccion = this.seleccion.slice();
    this.estado.emit(estado);
  }

  robot(key: String): ApolloQueryObservable<RobotQuery> {
    return this.apollo.watchQuery<RobotQuery>({ 
      query: RobotQueryNode,
      variables: { key }
    });
  }

  robots(): ApolloQueryObservable<RobotsQuery> {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode});
  }

  fase(numero: Number): ApolloQueryObservable<FaseQuery> {
    return this.apollo.watchQuery<FaseQuery>({ 
      query: FaseQueryNode,
      variables: { numero }
    });
  }

  fases(): ApolloQueryObservable<FasesQuery> {
    return this.apollo.watchQuery<FasesQuery>({ query: FasesQueryNode});
  }

  ronda(numero: Number): ApolloQueryObservable<RondaQuery> {
    return this.apollo.watchQuery<RondaQuery>({ 
      query: RondaQueryNode,
      variables: { numero }
    });
  }

  rondas(): ApolloQueryObservable<RondasQuery> {
    return this.apollo.watchQuery<RondasQuery>({ query: RondasQueryNode});
  }

  encuentro(numero: Number): ApolloQueryObservable<EncuentroQuery> {
    return this.apollo.watchQuery<EncuentroQuery>({ 
      query: EncuentroQueryNode,
      variables: { numero }
    });
  }

  score(key: String): ApolloQueryObservable<ScoreQuery> {
    return this.apollo.watchQuery<ScoreQuery>({ 
      query: ScoreQueryNode,
      variables: { key }
    });
  }
  
  scoresGeneral(): ApolloQueryObservable<ScoresGeneralQuery> {
    return this.apollo.watchQuery<ScoresGeneralQuery>({ query: ScoresGeneralQueryNode});
  }

  generarClasificacion(grupos: Number, esc: Boolean) {
    let obs$ = this.apollo.mutate<GenerarClasificacionMutation>({
      mutation: GenerarClasificacionMutationNode,
      variables: { grupos, esc }
    })
    obs$.subscribe(({data}) => this.setEstado(data.generarClasificacion.estado))
    return obs$;
  }

  generarEliminacion() {
    let obs$ = this.apollo.mutate<GenerarEliminacionMutation>({
      mutation: GenerarEliminacionMutationNode
    })
    obs$.subscribe(({data}) => this.setEstado(data.generarEliminacion.estado))
    return obs$;
  }

  generarFinal(jugadores: Number) {
    let obs$ = this.apollo.mutate<GenerarFinalMutation>({
      mutation: GenerarFinalMutationNode,
      variables: { jugadores }
    })
    obs$.subscribe(({data}) => this.setEstado(data.generarFinal.estado))
    return obs$;
  }

  generarAdhoc(robots: String[]) {
    let obs$ = this.apollo.mutate<GenerarAdhocMutation>({
      mutation: GenerarAdhocMutationNode,
      variables: { robots }
    })
    obs$.subscribe(({data}) => this.setEstado(data.generarAdhoc.estado))
    return obs$;
  }

  generarRonda(grupo: Number, tct: Boolean, esc: Boolean, allowNone: Boolean, shuffle: Boolean) {
    // Llamando a la mutacion generar ronda
    let obs$ = this.apollo.mutate<GenerarRondaMutation>({
      mutation: GenerarRondaMutationNode,
      variables: { grupo, tct, esc, allowNone, shuffle }
    })
    obs$.subscribe(({data}) => this.setEstado(data.generarRonda.estado))
    return obs$;
  }

  agregarGanador(key: String, encuentro: Number) {
    // Llamando a la mutacion agregar a un ganador
    let obs$ = this.apollo.mutate<AgregarGanadorMutation>({
      mutation: AgregarGanadorMutationNode,
      variables: { key, encuentro },
    })
    obs$.subscribe(({data}) => this.setEstado(data.agregarGanador.estado))
    return obs$;
  }

  quitarGanador(key: String, encuentro: Number = null) {
    // Llamando a la mutacion quitar a un ganador
    let obs$ = this.apollo.mutate<QuitarGanadorMutation>({
      mutation: QuitarGanadorMutationNode,
      variables: { key, encuentro },
    })
    obs$.subscribe(({data}) => this.setEstado(data.quitarGanador.estado))
    return obs$;
  }
}

