//  This file was automatically generated and should not be edited.
/* tslint:disable */

export interface EncuentroQueryVariables {
  numero: number;
}

export interface EncuentroQuery {
  fixture: {
    encuentro: {
      numero: number | null,
      robots: Array< {
        key: string | null,
        nombre: string | null,
        escudo: string | null,
      } > | null,
      puntos: Array< number | null > | null,
    } | null,
  } | null;
}

export interface EncuentrosQuery {
  fixture: {
    encuentros: Array< {
      numero: number | null,
    } > | null,
  } | null;
}

export interface FixtureQuery {
  fixture: {
    estado: {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null;
}

export interface GanaRobotMutationVariables {
  key: string;
  encuentro: number | null;
}

export interface GanaRobotMutation {
  ganaRobot: {
    ok: boolean | null,
    mensaje: string | null,
    encuentro: {
      numero: number | null,
      puntos: Array< number | null > | null,
      estado: {
        finalizado: boolean | null,
      } | null,
    } | null,
    estado: {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null;
}

export interface GenerarRondaMutation {
  generarRonda: {
    ok: boolean | null,
    mensaje: string | null,
    ronda: {
      numero: number | null,
      tct: boolean | null,
    } | null,
    estado: {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null;
}

export interface RobotQueryVariables {
  key: string | null;
}

export interface RobotQuery {
  fixture: {
    robot: {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado: string | null,
      escudo: string | null,
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
    } > | null,
  } | null;
}

export interface RobotsScoreQuery {
  fixture: {
    robots: Array< {
      key: string | null,
      nombre: string | null,
      escudo: string | null,
      escuela: string | null,
      score: Array< number | null > | null,
    } > | null,
  } | null;
}

export interface RondaQueryVariables {
  numero: number;
}

export interface RondaQuery {
  fixture: {
    ronda: {
      numero: number | null,
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
      promovidos: Array< {
        key: string | null,
        nombre: string | null,
        escudo: string | null,
      } > | null,
    } | null,
  } | null;
}

export interface RondasQuery {
  fixture: {
    rondas: Array< {
      numero: number | null,
      tct: boolean | null,
    } > | null,
  } | null;
}
/* tslint:enable */
