import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { Estado, FixtureService } from "../fixture.service";
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'page-fase',
  templateUrl: './page-fase.component.html',
  styleUrls: ['./page-fase.component.css']
})
export class PageFaseComponent {
  faseQuery$: any
  fase: any
  estado: Estado

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private fixture: FixtureService
  ) { 
    this.fixture.estado$.subscribe(estado => this.setEstado(estado))
    this.route.params
      .switchMap(params => (this.faseQuery$ = this.fixture.fase(+params['numero'])))
      .subscribe(({data}) => {
        this.fase = data.fixture.fase
      });
    }

  armarFinal(fase: Number) {
    this.fixture.armarFinal(fase);
  }

  setEstado(estado: Estado) {
    this.estado = estado
    this.faseQuery$.refetch();
  }

}
