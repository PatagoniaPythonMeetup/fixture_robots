//  This file was automatically generated and should not be edited.
/* tslint:disable */

export interface EncuentrosActualesQuery {
  fixture: {
    encuentrosActuales: Array< {
      numero: number | null,
      jugadas: number | null,
      finalizado: boolean | null,
      robots: Array< {
        key: string | null,
        nombre: string | null,
        escudo: string | null,
      } > | null,
      puntos: Array< number | null > | null,
    } > | null,
  } | null;
}

export interface GanaRobotMutationVariables {
  key: string;
  ronda: number | null;
  encuentro: number | null;
}

export interface GanaRobotMutation {
  ganaRobot: {
    ok: boolean | null,
    mensaje: string | null,
    encuentro: {
      numero: number | null,
      jugadas: number | null,
      finalizado: boolean | null,
      puntos: Array< number | null > | null,
    } | null,
  } | null;
}

export interface GenerarRondaMutationVariables {
  tct: boolean;
}

export interface GenerarRondaMutation {
  generarRonda: {
    ok: boolean | null,
    mensaje: string | null,
    ronda: {
      numero: number | null,
      vuelta: number | null,
      jugadas: number | null,
      finalizada: boolean | null,
      tct: boolean | null,
    } | null,
  } | null;
}

export interface RobotsQuery {
  fixture: {
    robots: Array< {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado: string | null,
      escudo: string | null,
      score: Array< number | null > | null,
    } > | null,
  } | null;
}

export interface RondaActualQuery {
  fixture: {
    rondaActual: {
      numero: number | null,
      vuelta: number | null,
      jugadas: number | null,
      finalizada: boolean | null,
      tct: boolean | null,
      encuentros: Array< {
        numero: number | null,
        robots: Array< {
          key: string | null,
          nombre: string | null,
          escudo: string | null,
        } > | null,
        puntos: Array< number | null > | null,
      } > | null,
    } | null,
  } | null;
}
/* tslint:enable */
