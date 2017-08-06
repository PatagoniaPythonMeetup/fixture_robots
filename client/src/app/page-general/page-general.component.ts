import { Component, OnInit } from '@angular/core';
import { FixtureService } from "../fixture.service";

@Component({
  selector: 'page-general',
  templateUrl: './page-general.component.html',
  styleUrls: ['./page-general.component.css']
})
export class PageGeneralComponent implements OnInit {
  robots$: any;
  robots: any[];
  
  constructor(private fixture: FixtureService) {
    this.robots$ = this.fixture.scoresGeneral()
    this.robots$.subscribe(({data}) => {
      let robots = data.fixture.robots.slice().map(r => _.clone(r));
      let scores = data.fixture.scores.slice().map(s => _.clone(s));
      robots.forEach((r, i) => r.score = scores[i]);
      robots.sort((a, b) => b.score[7] - a.score[7]);
      this.robots = robots;
    })
  }

  ngOnInit() {
    this.robots$.refetch();
  }

}
