import { Router } from '@angular/router';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  rondas$: any;
  title = 'RoboFixture';
  estado: Estado

  constructor(private router: Router, private fixture: FixtureService) {
    this.fixture.estado.subscribe(estado => this.estado = estado)
  }

  ngOnInit() {
    this.rondas$ = this.fixture.rondas();
  }

  generarRonda() {
    this.fixture.generarRondas()
      .subscribe(ronda => {
        this.rondas$.refetch();
      })
  }
}
