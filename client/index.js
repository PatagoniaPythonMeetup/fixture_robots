import $ from 'jquery'
import 'imports-loader?jQuery=jquery!jquery-bracket'
import './jquery.bracket.scss'

import Lokka from 'lokka';
import Transport from 'lokka-transport-http';

const client = new Lokka({
  transport: new Transport(`http://${location.host}/fixture`)
});

client.query(`
    {
      robots {
        nombre
        escuela
        encargado
        puntaje
      }
      rondas {
        numero
        vuelta
        encuentros {
          numero
          vuelta
          robots {
            nombre
          }
          resultados
        }
        promovidos {
          nombre
          escuela
          encargado
        }
      }
    }
`).then(result => {
    console.log(result.robots);
    console.log(result.rondas);
});

var minimalData = {
    teams : [
      ["Team 1", "Team 2"],
      ["Team 3", "Team 4"]
    ],
    results : [
      [[1,2], [3,4]],
      [[4,6], [2,1]]
    ]
  }
 
$(function() {
    $('#bracket.demo').bracket({
      init: minimalData })
  })
