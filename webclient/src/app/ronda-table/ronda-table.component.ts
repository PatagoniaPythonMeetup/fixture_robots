import { RondaQuery } from '../../graphql/schema';
import { ActivatedRoute, Router} from '@angular/router';
import { FixtureService, Estado } from '../fixture.service';
import { Component } from '@angular/core';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/switchMap';
import { ApolloQueryObservable } from "apollo-angular/build/src";

@Component({
  selector: 'ronda-table',
  templateUrl: './ronda-table.component.html',
  styleUrls: ['./ronda-table.component.css']
})
export class RondaTableComponent {
  rondaQuery$: any;
  ronda: any
  estado: Estado

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private fixture: FixtureService
  ) { 
    this.fixture.estado.subscribe(estado => this.setEstado(estado))
    this.route.params
      .switchMap(params => (this.rondaQuery$ = this.fixture.ronda(+params['numero'])))
      .subscribe(ronda => this.ronda = ronda);
    }

  setEstado(estado: Estado) {
    this.estado = estado
    if (this.ronda && (estado.ronda === this.ronda.numero || estado.finalizado)) {
      this.rondaQuery$.refetch();
    }
  }
}
