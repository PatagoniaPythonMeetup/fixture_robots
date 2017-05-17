import { Router } from '@angular/router';
import { RondasQuery } from '../../../graphql/schema';
import { ApolloQueryObservable } from 'apollo-angular/build/src';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  rondas$: ApolloQueryObservable<any>;
  title = 'Rob Fixture';
  estado: Estado;

  constructor(private router: Router, private fixture: FixtureService) { }

  ngOnInit() {
    this.fixture.getEstado().subscribe(estado => this.estado = estado);
    this.rondas$ = this.fixture.rondas();
  }

  generarRonda() {
    this.fixture.generarRonda(false)
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
