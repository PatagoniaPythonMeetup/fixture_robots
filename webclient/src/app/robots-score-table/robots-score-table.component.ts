import { Observable } from 'rxjs/Rx';
import { FixtureService } from '../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'robots-score-table',
  templateUrl: './robots-score-table.component.html',
  styleUrls: ['./robots-score-table.component.css']
})
export class RobotsScoreTableComponent implements OnInit {
  robotsScore$: Observable<any>;
  
  constructor(private fixture: FixtureService) {
    this.robotsScore$ = this.fixture.robotsScore();
  }

  ngOnInit() {
  }

}
