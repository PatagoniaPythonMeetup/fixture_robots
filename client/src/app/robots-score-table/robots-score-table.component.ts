import { Component, OnInit } from '@angular/core';
import { FixtureService } from "../fixture.service";

@Component({
  selector: 'app-robots-score-table',
  templateUrl: './robots-score-table.component.html',
  styleUrls: ['./robots-score-table.component.css']
})
export class RobotsScoreTableComponent implements OnInit {
  robots$: any
  robots: any[]
  
  constructor(private fixture: FixtureService) {
    this.robots$ = this.fixture.robots()
    this.robots$.subscribe(({data}) => {
      let robots = data.fixture.robots.slice();
      
      robots.sort((a, b) => b.score[7] - a.score[7]);
      this.robots = robots;
    })
  }

  ngOnInit() {
    this.robots$.refetch();
  }

}

