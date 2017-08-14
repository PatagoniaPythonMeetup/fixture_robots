import { ModalComponent } from '../../layout/modal/modal.component';
import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { FixtureService } from "../../fixture.service";

declare var jQuery: any;

@Component({
  selector: 'grupo',
  templateUrl: './grupo.component.html',
  styleUrls: ['./grupo.component.css']
})
export class GrupoComponent implements OnInit {
  @Input() grupo: any = {}
  robots: any[];
  rondas: any[];
  @ViewChild("rondaModal") rondaModal: ModalComponent;
  @ViewChild("checkboxTct") checkboxTct: ElementRef;
  @ViewChild("checkboxEsc") checkboxEsc: ElementRef;
  @ViewChild("checkboxAllowNone") checkboxAllowNone: ElementRef;
  @ViewChild("checkboxShuffle") checkboxShuffle: ElementRef;

  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    let robots = this.grupo.robots.slice().map(r => _.clone(r));
    let scores = this.grupo.scores.slice().map(s => _.clone(s));
    robots.forEach((r, i) => r.score = scores[i]);
    robots.sort((a, b) => b.score[7] - a.score[7]);
    this.robots = robots;
    this.rondas = this.grupo.rondas.map(r => _.clone(r));
  }

  agregarRonda() {
    let tct = jQuery(this.checkboxTct.nativeElement).prop( "checked" );
    let esc = jQuery(this.checkboxEsc.nativeElement).prop( "checked" );
    let allowNone = jQuery(this.checkboxAllowNone.nativeElement).prop( "checked" );
    let shuffle = jQuery(this.checkboxShuffle.nativeElement).prop( "checked" );
    this.fixture.generarRonda(this.grupo.numero, tct, esc, allowNone, shuffle)
  }
}
