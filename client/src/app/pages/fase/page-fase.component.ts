import { Component } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { Estado, FixtureService } from '../../fixture.service';
 
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'page-fase',
  template: `
<div *ngIf="fase && fase.tipo === 'clasificacion'">
  <fase [fase]="fase"></fase>
</div>
<div *ngIf="fase && fase.tipo === 'final'">
  <fase [fase]="fase"></fase>
  <button 
    *ngIf="fase.estado.finalizado && fase.grupos.length === 2"
    (click)="armarFinal(fase.numero)"
    class="primary ui button" ><i class="plus icon"></i>Armar Final
  </button>
</div>
<div *ngIf="fase && fase.tipo === 'eliminacion'">
  <fase [fase]="fase"></fase>
</div>
<div *ngIf="fase && fase.tipo === 'adhoc'">
  <fase [fase]="fase"></fase>
</div>
  `,
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
    this.route.params.pipe(
        switchMap(params => (this.faseQuery$ = this.fixture.fase(+params['numero']).valueChanges))
        )
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
