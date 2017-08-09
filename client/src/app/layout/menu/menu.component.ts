import { Router } from '@angular/router';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewInit, AfterViewChecked, ElementRef, ViewChild, AfterContentInit } from '@angular/core';

declare var jQuery: any;

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit, AfterViewChecked {
  fases$: any
  fases: any[]
  title = 'RoboFixture'
  estado: Estado
  jqueyBind: Boolean = false
  @ViewChild("inputGrupos") inputGrupos: ElementRef;
  @ViewChild("checkboxEsc") checkboxEsc: ElementRef;

  constructor(
    private router: Router, 
    private fixture: FixtureService, 
    private rootNode: ElementRef
  ) {
    this.fixture.estado.subscribe(estado => this.setEstado(estado))
  }

  ngOnInit() {
    this.fases$ = this.fixture.fases();
    this.fases$.subscribe(({data}) => {
      this.fases = data.fixture.fases
    })
  }

  setEstado(estado: Estado) {
    this.estado = estado
  }

  ngAfterViewChecked(): void {
    if (!this.jqueyBind && $(".ui.dropdown", this.rootNode.nativeElement).length) {
      jQuery(".ui.dropdown", this.rootNode.nativeElement).dropdown()
      this.jqueyBind = true
    }
  }

  // Crear fases
  generarClasificacion() {
    let grupos = jQuery(this.inputGrupos.nativeElement).val();
    let esc = jQuery(this.checkboxEsc.nativeElement).prop( "checked" );
    this.fixture.generarClasificacion(Number(grupos), esc)
  }

  generarEliminacion() {
    this.fixture.generarAdhoc(this.estado.seleccion)
  }

  generarFinal() {
    this.fixture.generarAdhoc(this.estado.seleccion)
  }

  generarAdhoc() {
    this.fixture.generarAdhoc(this.estado.seleccion)
  }

}
