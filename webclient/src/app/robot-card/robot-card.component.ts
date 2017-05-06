import { Input } from '@angular/core';
import { Component, OnInit } from '@angular/core';

interface IRobot {
  key: String,
  nombre: String,
  escuela: String,
  encargado: String,
  escudo: String,
  score: Array<Number>
}

@Component({
  selector: 'robot-card',
  templateUrl: './robot-card.component.html',
  styleUrls: ['./robot-card.component.css']
})
export class RobotCardComponent implements OnInit {
  @Input() robot: IRobot = <IRobot>{}
  constructor() { 
    this.robot.score = [3,3]
  }

  ngOnInit() {
  }

}
