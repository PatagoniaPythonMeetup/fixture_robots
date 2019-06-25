import { FixtureService } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'page-posiciones',
  templateUrl: './page-posiciones.component.html',
})
export class PagePosicionesComponent implements OnInit {
  posiciones$: any;
  equipos: any[];
  
  constructor(private fixture: FixtureService) {
    this.posiciones$ = this.fixture.posiciones();
    this.posiciones$.valueChanges.subscribe(({data}) => {
      this.equipos = data.fixture.posiciones.slice();
    })
  }

  ngOnInit() {
    this.posiciones$.refetch();
  }

}
