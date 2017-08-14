/* tslint:disable */
//  This file was automatically generated and should not be edited.

export type AgregarAdversarioMutationVariables = {
  encuentro: number,
};

export type AgregarAdversarioMutation = {
  agregarAdversario:  {
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
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type AgregarGanadorMutationVariables = {
  key: string,
  encuentro: number,
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
      } | null > | null,
      puntos: Array< number | null > | null,
    } | null,
  } | null,
};

export type EncuentrosQuery = {
  fixture:  {
    encuentros:  Array< {
      numero: number | null,
    } | null > | null,
  } | null,
};

export type FaseQueryVariables = {
  numero: number,
};

export type FaseQuery = {
  fixture:  {
    fase:  {
      tipo: string | null,
      nombre: string | null,
      numero: number | null,
      estado:  {
        iniciado: boolean | null,
        compitiendo: boolean | null,
        finalizado: boolean | null,
      } | null,
      grupos:  Array< {
        numero: number | null,
        nombre: string | null,
        robots:  Array< {
          key: string | null,
          nombre: string | null,
          escuela: string | null,
          encargado:  {
            nombre: string | null,
            dni: string | null,
            email: string | null,
            rol: string | null,
          } | null,
          escudo: string | null,
        } | null > | null,
        estado:  {
          iniciado: boolean | null,
          compitiendo: boolean | null,
          finalizado: boolean | null,
        } | null,
        rondas:  Array< {
          numero: number | null,
          nombre: string | null,
          tct: boolean | null,
          promovidos:  Array< {
            key: string | null,
            nombre: string | null,
            escuela: string | null,
            escudo: string | null,
            encargado:  {
              nombre: string | null,
              dni: string | null,
              email: string | null,
              rol: string | null,
            } | null,
          } | null > | null,
          estado:  {
            iniciado: boolean | null,
            compitiendo: boolean | null,
            finalizado: boolean | null,
          } | null,
          encuentros:  Array< {
            robots:  Array< {
              key: string | null,
              nombre: string | null,
              escuela: string | null,
              escudo: string | null,
            } | null > | null,
            numero: number | null,
            puntos: Array< number | null > | null,
            estado:  {
              iniciado: boolean | null,
              compitiendo: boolean | null,
              finalizado: boolean | null,
            } | null,
          } | null > | null,
        } | null > | null,
        scores: Array< Array< number | null > | null > | null,
      } | null > | null,
    } | null,
  } | null,
};

export type FasesQuery = {
  fixture:  {
    fases:  Array< {
      numero: number | null,
      nombre: string | null,
    } | null > | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
    } | null,
  } | null,
};

export type FixtureQuery = {
  fixture:  {
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarAdhocMutationVariables = {
  robots?: Array< string | null > | null,
};

export type GenerarAdhocMutation = {
  generarAdhoc:  {
    ok: boolean | null,
    mensaje: string | null,
    fase:  {
      nombre: string | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarClasificacionMutationVariables = {
  grupos: number,
  esc: boolean,
};

export type GenerarClasificacionMutation = {
  generarClasificacion:  {
    ok: boolean | null,
    mensaje: string | null,
    fase:  {
      nombre: string | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarEliminacionMutation = {
  generarEliminacion:  {
    ok: boolean | null,
    mensaje: string | null,
    fase:  {
      nombre: string | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarFinalMutationVariables = {
  jugadores: number,
};

export type GenerarFinalMutation = {
  generarFinal:  {
    ok: boolean | null,
    mensaje: string | null,
    fase:  {
      nombre: string | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type GenerarRondaMutationVariables = {
  grupo: number,
  tct: boolean,
  esc: boolean,
  allowNone: boolean,
  shuffle: boolean,
};

export type GenerarRondaMutation = {
  generarRonda:  {
    ok: boolean | null,
    mensaje: string | null,
    ronda:  {
      numero: number | null,
      tct: boolean | null,
    } | null,
    estado:  {
      iniciado: boolean | null,
      compitiendo: boolean | null,
      finalizado: boolean | null,
      jugadas: number | null,
      encuentros: Array< number | null > | null,
      ronda: number | null,
    } | null,
  } | null,
};

export type QuitarGanadorMutationVariables = {
  key: string,
  encuentro: number,
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
      encargado:  {
        nombre: string | null,
        dni: string | null,
        email: string | null,
        rol: string | null,
      } | null,
      escudo: string | null,
    } | null,
  } | null,
};

export type RobotsQuery = {
  fixture:  {
    robots:  Array< {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado:  {
        nombre: string | null,
        dni: string | null,
        email: string | null,
        rol: string | null,
      } | null,
      escudo: string | null,
    } | null > | null,
  } | null,
};

export type RondaQueryVariables = {
  numero: number,
};

export type RondaQuery = {
  fixture:  {
    ronda:  {
      numero: number | null,
      nombre: string | null,
      tct: boolean | null,
      encuentros:  Array< {
        numero: number | null,
        robots:  Array< {
          key: string | null,
          nombre: string | null,
          escuela: string | null,
          escudo: string | null,
        } | null > | null,
        puntos: Array< number | null > | null,
      } | null > | null,
      promovidos:  Array< {
        key: string | null,
        nombre: string | null,
        escuela: string | null,
        encargado:  {
          nombre: string | null,
          dni: string | null,
          email: string | null,
          rol: string | null,
        } | null,
        escudo: string | null,
      } | null > | null,
    } | null,
  } | null,
};

export type RondasQuery = {
  fixture:  {
    rondas:  Array< {
      numero: number | null,
      tct: boolean | null,
    } | null > | null,
  } | null,
};

export type ScoreQueryVariables = {
  key?: string | null,
};

export type ScoreQuery = {
  fixture:  {
    robot:  {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado:  {
        nombre: string | null,
        dni: string | null,
        email: string | null,
        rol: string | null,
      } | null,
      escudo: string | null,
    } | null,
    score: Array< number | null > | null,
  } | null,
};

export type ScoresGeneralQuery = {
  fixture:  {
    robots:  Array< {
      key: string | null,
      nombre: string | null,
      escuela: string | null,
      encargado:  {
        nombre: string | null,
        dni: string | null,
        email: string | null,
        rol: string | null,
      } | null,
      escudo: string | null,
    } | null > | null,
    scores: Array< Array< number | null > | null > | null,
  } | null,
};
/* tslint:enable */
