import { Router } from '@angular/router';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewInit, AfterViewChecked, ElementRef, ViewChild, AfterContentInit } from '@angular/core';

declare var jQuery: any;

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html'
})
export class MenuComponent implements OnInit {
  fases$: any
  fases: any[]
  title = 'RoboFixture'
  estado: Estado
  jqueyBind: Boolean = false
  @ViewChild("inputGrupos") inputGrupos: ElementRef;
  @ViewChild("checkboxEsc") checkboxEsc: ElementRef;
  @ViewChild("inputJugadores") inputJugadores: ElementRef;

  constructor(
    private router: Router, 
    private fixture: FixtureService, 
    private rootNode: ElementRef
  ) {
    this.fixture.estado$.subscribe(estado => this.setEstado(estado))
  }

  ngOnInit() {
    this.fases$ = this.fixture.fases();
    this.fases$.valueChanges.subscribe(({data}) => {
      this.fases = data.fixture.fases
    })
  }

  setEstado(estado: Estado) {
    this.estado = estado;
    jQuery(".ui.dropdown", this.rootNode.nativeElement).dropdown();
  }

  // Crear fases
  generarClasificacion() {
    let grupos = jQuery(this.inputGrupos.nativeElement).val();
    let esc = jQuery(this.checkboxEsc.nativeElement).prop( "checked" );
    this.fixture.generarClasificacion(Number(grupos), esc)
      .subscribe(({data}) => this.fases$.refetch());
  }

  generarEliminacion() {
    this.fixture.generarEliminacion()
      .subscribe(({data}) => this.fases$.refetch())
  }

  generarFinal() {
    let jugadores = jQuery(this.inputJugadores.nativeElement).val();
    this.fixture.generarFinal(Number(jugadores))
      .subscribe(({data}) => this.fases$.refetch());
  }

  generarAdhoc() {
    let seleccion = [...this.estado.seleccion];
    if (seleccion.length > 1)
      this.fixture.generarAdhoc(this.estado.seleccion)
        .subscribe(({data}) => this.fases$.refetch());
  }

}
