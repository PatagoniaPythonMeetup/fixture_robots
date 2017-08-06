import { Component, OnInit, Input } from '@angular/core';

interface IRobot {
  key: String,
  nombre: String,
  escuela: String,
  encargado: String,
  escudo: String,
  score: Array<Number>
}

@Component({
  selector: 'robots-score',
  templateUrl: './robots-score.component.html',
  styleUrls: ['./robots-score.component.css']
})
export class RobotsScoreComponent implements OnInit {
  @Input() robots: IRobot[] = <IRobot[]>[]
  constructor() {
  }

  ngOnInit() {
  }

}