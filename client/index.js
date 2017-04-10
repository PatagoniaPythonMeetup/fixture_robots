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
    var robots = result.robots;
    var rondas = result.rondas;
    var teams = rondas[0].encuentros.map( encuentro => encuentro.robots.map(robot => robot.nombre) );
    var resultados = rondas[0].encuentros.map( encuentro => encuentro.resultados );
    window.TEAMS = teams;
    console.log(resultados);
    var data = {
      teams: [ teams[0], teams[1], teams[2] ],
      results: [[resultados[0], resultados[1], resultados[2]]]
    };
    $(function() {
      $('#bracket.demo').bracket({
        init: data 
      });
    });
});

