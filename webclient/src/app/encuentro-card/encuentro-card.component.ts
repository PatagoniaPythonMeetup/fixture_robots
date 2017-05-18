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

  gano(event, key) {
    $(event.target).transition('jiggle')
    this.fixture.ganaRobot(key)
      .subscribe((encuentro: any) => {
        this.encuentro = Object.assign({}, this.encuentro, encuentro)
      })
  }

  ngOnInit() {
  }

}
