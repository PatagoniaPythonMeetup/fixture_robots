import { ActivatedRoute, Router} from '@angular/router';
import { FixtureService } from '../fixture.service';
import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/switchMap';
import { ApolloQueryObservable } from "apollo-angular/build/src";

@Component({
  selector: 'ronda-table',
  templateUrl: './ronda-table.component.html',
  styleUrls: ['./ronda-table.component.css']
})
export class RondaTableComponent implements OnInit {
  ronda: any

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private fixture: FixtureService
  ) { 
  }

  ngOnInit() {
    this.route.params
      .switchMap(params => this.fixture.ronda(+params['numero']))
      .subscribe(ronda => this.ronda = ronda);
  }
}
