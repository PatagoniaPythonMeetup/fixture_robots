import { RondasQuery } from '../../../graphql/schema';
import { ApolloQueryObservable } from 'apollo-angular/build/src';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  rondas$: ApolloQueryObservable<any>;
  title = 'Rob Fixture';
  
  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.rondas$ = this.fixture.rondas();
  }

  activar(item, ronda) {
    console.log(item, ronda)
  }

  generarRonda() {
    this.fixture.generarRonda(false)
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
