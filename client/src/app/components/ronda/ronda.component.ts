import { Component, OnInit, Input } from '@angular/core';
import { FixtureService } from "../../fixture.service";

@Component({
  selector: 'ronda',
  templateUrl: './ronda.component.html',
  styleUrls: ['./ronda.component.css']
})
export class RondaComponent implements OnInit {
  @Input() ronda: any
  nombre: String

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

  agregarAdversario(evento, encuentro){
    this.fixture.agregarAdversario(encuentro)
  }

  ngOnInit() {
    if (this.ronda.tct)
      this.nombre = `Todos vs Todos`
    else
      this.nombre = `Ronda ${this.ronda.numero}`
  }
}
