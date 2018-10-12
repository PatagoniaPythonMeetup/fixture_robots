import { Apollo } from 'apollo-angular';
import { Injectable, EventEmitter } from '@angular/core';
import { DocumentNode } from 'graphql';

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
    PosicionesQuery,
    GenerarClasificacionMutation,
    GenerarEliminacionMutation,
    GenerarFinalMutation,
    GenerarAdhocMutation,
    GenerarRondaMutation,
    AgregarGanadorMutation,
    QuitarGanadorMutation,
    AgregarAdversarioMutation,
    ArmarFinalMutation,
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
const PosicionesQueryNode: DocumentNode = require('graphql-tag/loader!../graphql/Posiciones.graphql');

const GenerarRondaMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarRonda.graphql');
const AgregarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/AgregarGanador.graphql');
const AgregarAdversarioMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/AgregarAdversario.graphql');
const QuitarGanadorMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/QuitarGanador.graphql');
const GenerarClasificacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarClasificacion.graphql');
const GenerarEliminacionMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarEliminacion.graphql');
const GenerarFinalMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarFinal.graphql');
const GenerarAdhocMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/GenerarAdhoc.graphql');
const ArmarFinalMutationNode: DocumentNode = require('graphql-tag/loader!../graphql/ArmarFinal.graphql');

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
  estado: Estado = ESTADO_INICIAL;
  estado$: EventEmitter<Estado> = new EventEmitter<Estado>()

  constructor(private apollo: Apollo) {
    let estado = this.apollo.watchQuery<FixtureQuery>({ query: FixtureQueryNode})
    estado.valueChanges.subscribe(({data}) => this.setEstado(data.fixture.estado))
  }
  
  setRobotsSeleccionados(robots) {
    this.estado$.emit(Object.assign(this.estado, {seleccion: robots}));
  }

  setEstado(estado) {
    this.estado$.emit(Object.assign(this.estado, estado));
  }

  robot(key: String) {
    return this.apollo.watchQuery<RobotQuery>({ 
      query: RobotQueryNode,
      variables: { key }
    });
  }

  robots() {
    return this.apollo.watchQuery<RobotsQuery>({ query: RobotsQueryNode});
  }

  fase(numero: Number) {
    return this.apollo.watchQuery<FaseQuery>({ 
      query: FaseQueryNode,
      variables: { numero }
    });
  }

  fases() {
    return this.apollo.watchQuery<FasesQuery>({ query: FasesQueryNode});
  }

  ronda(numero: Number) {
    return this.apollo.watchQuery<RondaQuery>({ 
      query: RondaQueryNode,
      variables: { numero }
    });
  }

  rondas() {
    return this.apollo.watchQuery<RondasQuery>({ query: RondasQueryNode});
  }

  encuentro(numero: Number) {
    return this.apollo.watchQuery<EncuentroQuery>({ 
      query: EncuentroQueryNode,
      variables: { numero }
    });
  }

  score(key: String) {
    return this.apollo.watchQuery<ScoreQuery>({ 
      query: ScoreQueryNode,
      variables: { key }
    });
  }
  
  posiciones() {
    return this.apollo.watchQuery<PosicionesQuery>({ query: PosicionesQueryNode});
  }

  scoresGeneral() {
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

  agregarAdversario(encuentro: Number) {
    // Llamando a la mutacion agregar a un ganador
    let obs$ = this.apollo.mutate<AgregarAdversarioMutation>({
      mutation: AgregarAdversarioMutationNode,
      variables: { encuentro },
    })
    obs$.subscribe(({data}) => this.setEstado(data.agregarAdversario.estado))
    return obs$;
  }

  armarFinal(fase: Number) {
    // Llamando a la mutacion armar final
    let obs$ = this.apollo.mutate<ArmarFinalMutation>({
      mutation: ArmarFinalMutationNode,
      variables: { fase },
    })
    obs$.subscribe(({data}) => this.setEstado(data.armarFinal.estado))
    return obs$;
  }
}

