import { Router } from '@angular/router';
import { RondasQuery } from '../../../graphql/schema';
import { ApolloQueryObservable } from 'apollo-angular/build/src';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  rondas$: ApolloQueryObservable<any>;
  title = 'Rob Fixture';
  estado: any = {compitiendo: false, finalizado: false}
  constructor(
    private router: Router,
    private fixture: FixtureService
  ) {
    this.fixture.estado.subscribe(estado => this.estado = estado);
  }

  ngOnInit() {
    this.rondas$ = this.fixture.rondas();
  }

  generarRonda() {
    this.fixture.generarRonda(false)
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
