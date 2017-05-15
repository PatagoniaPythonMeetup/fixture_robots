import { ActivatedRoute, Router, Params } from '@angular/router';
import { FixtureService } from '../fixture.service';
import { Component, OnInit, Input } from '@angular/core';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'ronda-table',
  templateUrl: './ronda-table.component.html',
  styleUrls: ['./ronda-table.component.css']
})
export class RondaTableComponent implements OnInit {
  ronda: any = {encuentros: []}

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private fixture: FixtureService
  ) { 
  }

  ngOnInit() {
    this.route.params
      .switchMap((params: Params) => this.fixture.ronda(+params['numero']))
      .subscribe((ronda) => this.ronda = ronda);
  }

}
