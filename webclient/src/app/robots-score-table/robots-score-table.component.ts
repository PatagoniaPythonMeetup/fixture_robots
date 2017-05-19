import { Observable } from 'rxjs/Rx';
import { FixtureService } from '../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'robots-score-table',
  templateUrl: './robots-score-table.component.html',
  styleUrls: ['./robots-score-table.component.css']
})
export class RobotsScoreTableComponent implements OnInit {
  robotsScore$: any
  robots: any
  
  constructor(private fixture: FixtureService) {
    this.robotsScore$ = this.fixture.robotsScore()
    this.robotsScore$.subscribe(robots => {
      let r = robots.slice();
      r.sort((a, b) => b.score[7] - a.score[7]);
      this.robots = r;
    })
  }

  ngOnInit() {
    this.robotsScore$.refetch();
  }

}
