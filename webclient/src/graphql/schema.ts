/* tslint:disable */
//  This file was automatically generated and should not be edited.

export type AgregarGanadorMutationVariables = {
  key: string,
  encuentro?: number | null,
};

export type AgregarGanadorMutation = {
  agregarGanador:  {
    ok: boolean | null,
    mensaje: string | null,
    encuentro:  {
      numero: number | null,
      puntos: Array< number | null > | null,
      estado:  {
        finalizado: boolean | null,
      } | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type EncuentroQueryVariables = {
  numero: number,
};

export type EncuentroQuery = {
  fixture:  {
    encuentro:  {
      numero: number | null,
      robots:  Array< {
        key: string | null,
        nombre: string | null,
        escudo: string | null,
      } > | null,
      puntos: Array< number | null > | null,
    } | null,
  } | null,
};

export type EncuentrosQuery = {
  fixture:  {
    encuentros:  Array< {
      numero: number | null,
    } > | null,
  } | null,
};

export type FixtureQuery = {
  fixture:  {
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarRondasMutation = {
  generarRondas:  {
    ok: boolean | null,
    mensaje: string | null,
    rondas:  Array< {
      numero: number | null,
      tct: boolean | null,
    } > | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type QuitarGanadorMutationVariables = {
  key: string,
  encuentro?: number | null,
};

export type QuitarGanadorMutation = {
  quitarGanador:  {
    ok: boolean | null,
    mensaje: string | null,
    encuentro:  {
      numero: number | null,
      puntos: Array< number | null > | null,
      estado:  {
        finalizado: boolean | null,
      } | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      vuelta: number | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type RobotQueryVariables = {
  key?: string | null,
};

export type RobotQuery = {
  fixture:  {
    robot:  {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado: string | null,
      escudo: string | null,
    } | null,
  } | null,
};

export type RobotFixtureScoreQueryVariables = {
  key?: string | null,
};

export type RobotFixtureScoreQuery = {
  fixture:  {
    score: Array< number | null > | null,
  } | null,
};

export type RobotsQuery = {
  fixture:  {
    robots:  Array< {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado: string | null,
      escudo: string | null,
    } > | null,
  } | null,
};

export type RondaQueryVariables = {
  numero: number,
};

export type RondaQuery = {
  fixture:  {
    ronda:  {
      numero: number | null,
      tct: boolean | null,
      encuentros:  Array< {
        numero: number | null,
        robots:  Array< {
          key: string | null,
          nombre: string | null,
          escudo: string | null,
        } > | null,
        puntos: Array< number | null > | null,
      } > | null,
      promovidos:  Array< {
        key: string | null,
        nombre: string | null,
        escudo: string | null,
      } > | null,
    } | null,
  } | null,
};

export type RondasQuery = {
  fixture:  {
    rondas:  Array< {
      numero: number | null,
      tct: boolean | null,
    } > | null,
  } | null,
};
/* tslint:enable */
