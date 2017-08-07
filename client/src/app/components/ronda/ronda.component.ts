import { Component, OnInit, Input } from '@angular/core';
import { FixtureService } from "../../fixture.service";

@Component({
  selector: 'ronda',
  templateUrl: './ronda.component.html',
  styleUrls: ['./ronda.component.css']
})
export class RondaComponent implements OnInit {
  @Input() ronda: any

  constructor(private fixture: FixtureService) { }

  resultado(event, numero, key) {
    if (event.shiftKey) {
      $(event.target).transition('flash')
      this.fixture.quitarGanador(key, numero)
    } else {
      $(event.target).transition('jiggle')
      this.fixture.agregarGanador(key, numero)
    }
  }

  ngOnInit(): void {
  }
}
