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
export class MenuComponent implements OnInit, AfterViewInit {
  rondas$: ApolloQueryObservable<any>;
  title = 'Rob Fixture';

  constructor(
    private router: Router,
    private fixture: FixtureService
  ) { }

  ngOnInit() {
    this.rondas$ = this.fixture.rondas();
  }

  public ngAfterViewInit() {
  }

  generarRonda() {
    this.fixture.generarRonda(false)
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
