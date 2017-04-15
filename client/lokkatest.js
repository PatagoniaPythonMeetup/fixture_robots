import $ from 'jquery'
import 'lodash'
import './styles.scss'

import Lokka from 'lokka';
import Transport from 'lokka-transport-http';

const client = new Lokka({
  transport: new Transport(`http://${location.host}/fixture`)
});

let consultarRobots = () =>
  client.query(`
      {
        robots {
          nombre
          escuela
          encargado
          score
        }
      }
  `).then(result => result.robots);

let ganaRobot = (ronda, encuentro, robot) =>
  client.mutate(`{
    success: ganaRobot(ronda: ${ronda}, encuentro: ${encuentro}, robot: "${robot}") {
        ok
    }
  }`).then(result => result.success);

ganaRobot(1, 1, "HAL 9000");
ganaRobot(1, 1, "HAL 9000");
ganaRobot(1, 1, "Centinelas");
ganaRobot(1, 2, "ED 209");
ganaRobot(1, 2, "ED 209");
ganaRobot(1, 2, "Roy Batty");
ganaRobot(1, 3, "Ultron");
ganaRobot(1, 3, "Bender");
ganaRobot(1, 3, "Bender");
ganaRobot(1, 4, "Teddy");
ganaRobot(1, 4, "Wall-e");
ganaRobot(1, 4, "Teddy");
ganaRobot(1, 5, "Optimus Prime");
ganaRobot(1, 5, "Johnny 5");
ganaRobot(1, 5, "Optimus Prime");
ganaRobot(1, 6, "Rodney");
ganaRobot(1, 6, "Rodney");
ganaRobot(1, 6, "Rodney");
ganaRobot(1, 7, "BB-8");
ganaRobot(1, 7, "Robocop");
ganaRobot(1, 7, "BB-8");
ganaRobot(1, 8, "T-1000");
ganaRobot(1, 8, "3-CPO");
ganaRobot(1, 8, "T-1000");
ganaRobot(1, 9, "R2-D2");
ganaRobot(1, 9, "Sony");
ganaRobot(1, 9, "Sony");
ganaRobot(1, 10, "T-800");
ganaRobot(1, 10, "T-800");
ganaRobot(1, 10, "David Swinton");

window.consultar = () =>
  consultarRobots().then(robots => console.log(robots));