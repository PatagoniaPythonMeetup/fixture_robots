import $ from 'jquery'
import 'lodash'
import './styles.scss'

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
        score
      }
      rondas {
        numero
        vuelta
        jugadas
        encuentros {
          numero
          jugadas
          robots {
            nombre
          }
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
    console.log(robots)
});

