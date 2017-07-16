import { FixtureService } from '../fixture.service';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

declare let $: any;

@Component({
  selector: 'encuentro-card',
  templateUrl: './encuentro-card.component.html',
  styleUrls: ['./encuentro-card.component.css']
})
export class EncuentroCardComponent implements OnInit {
  @Input() encuentro: any = {}
  
  constructor(private fixture: FixtureService) { }

  agregarGanador(event, key) {
    $(event.target).transition('jiggle')
    this.fixture.agregarGanador(key, this.encuentro.numero)
      .subscribe((encuentro: any) => {
        this.encuentro = Object.assign({}, this.encuentro, encuentro)
      })
  }
  
  quitarGanador(event, key) {
    $(event.target).transition('jiggle')
    this.fixture.quitarGanador(key, this.encuentro.numero)
      .subscribe((encuentro: any) => {
        this.encuentro = Object.assign({}, this.encuentro, encuentro)
      })
  }

  ngOnInit() {
  }

}
