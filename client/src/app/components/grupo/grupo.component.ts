import { ModalComponent } from '../../layout/modal/modal.component';
import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { FixtureService } from "../../fixture.service";

@Component({
  selector: 'grupo',
  templateUrl: './grupo.component.html',
  styleUrls: ['./grupo.component.css']
})
export class GrupoComponent implements OnInit {
  @Input() grupo: any = {}
  nombre: string
  robots: any[];
  rondas: any[];
  @ViewChild("rondaModal") rondaModal: ModalComponent;
  
  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.nombre = `Grupo ${this.grupo.numero}`
    let robots = this.grupo.robots.slice().map(r => _.clone(r));
    let scores = this.grupo.scores.slice().map(s => _.clone(s));
    robots.forEach((r, i) => r.score = scores[i]);
    robots.sort((a, b) => b.score[7] - a.score[7]);
    this.robots = robots;
    this.rondas = this.grupo.rondas.map(r => _.clone(r));
  }

  agregarRonda(numero) {
    this.rondaModal.show();
    this.fixture.generarRonda(numero, false, false, false)
  }

}
