import { RondasQuery } from '../../../graphql/schema';
import { ApolloQueryObservable } from 'apollo-angular/build/src';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit, AfterViewInit {
  rondas$: ApolloQueryObservable<any>;
  title = 'Rob Fixture';
  activo: String;

  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.rondas$ = this.fixture.rondas();
  }

  public ngAfterViewInit() {
    this.activar('robots');
  }

  activar(item, ronda = null) {
    this.activo = item;
    console.log(item, ronda)
  }

  generarRonda() {
    this.fixture.generarRonda(false)
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
