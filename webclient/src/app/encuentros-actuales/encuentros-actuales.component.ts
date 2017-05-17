import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/switchMap';

import { FixtureService, Estado } from '../fixture.service';

@Component({
  selector: 'encuentros-actuales',
  templateUrl: './encuentros-actuales.component.html',
  styleUrls: ['./encuentros-actuales.component.css']
})
export class EncuentrosActualesComponent implements OnInit {
  TRACKS_EN_PARALELO: Number = 1
  encuentros: Array<any> = []
  
  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.fixture.getEstado().subscribe(estado => this.cargarEstado(estado));
  }

  finalizado(fin, encuentro) {
    if (fin) {
      this.encuentros = this.encuentros.filter(e => e.numero !== encuentro.numero)
      this.fixture.getEstado().subscribe(estado => this.cargarEstado(estado))
    }
  }

  cargarEstado(estado: Estado) {
    if (estado.compitiendo) {
      Observable.from(estado.encuentros)
        .switchMap(e => this.fixture.encuentro(e))
        .subscribe(e => this.encuentros = [...this.encuentros, e])
    }
  }
}
