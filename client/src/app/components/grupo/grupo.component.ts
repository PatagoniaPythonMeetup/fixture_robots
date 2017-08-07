import { Component, OnInit, Input } from '@angular/core';

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

  constructor() { }

  ngOnInit() {
    this.nombre = `Grupo ${this.grupo.numero}`
    let robots = this.grupo.robots.slice().map(r => _.clone(r));
    let scores = this.grupo.scores.slice().map(s => _.clone(s));
    robots.forEach((r, i) => r.score = scores[i]);
    robots.sort((a, b) => b.score[7] - a.score[7]);
    this.robots = robots;
    this.rondas = this.grupo.rondas.map(r => _.clone(r));
    console.log(this.grupo, "onInit");
  }

}
