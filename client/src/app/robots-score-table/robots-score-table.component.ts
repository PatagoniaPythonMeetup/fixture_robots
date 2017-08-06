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
  selector: 'robots-score-table',
  templateUrl: './robots-score-table.component.html',
  styleUrls: ['./robots-score-table.component.css']
})
export class RobotsScoreTableComponent implements OnInit {
  @Input() robots: IRobot[] = <IRobot[]>[]
  constructor() {
  }

  ngOnInit() {
  }

}

