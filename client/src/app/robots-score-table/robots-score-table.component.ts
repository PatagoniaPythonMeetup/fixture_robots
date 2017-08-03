import { Component, OnInit } from '@angular/core';
import { FixtureService } from "../fixture.service";

@Component({
  selector: 'app-robots-score-table',
  templateUrl: './robots-score-table.component.html',
  styleUrls: ['./robots-score-table.component.css']
})
export class RobotsScoreTableComponent implements OnInit {
  robotsScore$: any
  robots: any[]
  
  constructor(private fixture: FixtureService) {
    this.robotsScore$ = this.fixture.robots()
    this.robotsScore$.subscribe(({data}) => {
      let robots = data.fixture.robots.slice();
      
      robots.sort((a, b) => b.score[7] - a.score[7]);
      this.robots = robots;
    })
  }

  ngOnInit() {
    this.robotsScore$.refetch();
  }

}

