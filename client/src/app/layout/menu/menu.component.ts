import { Router } from '@angular/router';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewInit, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit, AfterViewInit {
  fases$: any;
  fases: any[]
  title = 'RoboFixture';
  estado: Estado;

  constructor(
    private router: Router, 
    private fixture: FixtureService, 
    private rootNode: ElementRef
  ) {
    this.fixture.estado.subscribe(estado => this.estado = estado)
  }

  ngOnInit() {
    this.fases$ = this.fixture.fases();
    this.fases$.subscribe(({data}) => {
      this.fases = data.fixture.fases;
    })
  }

  ngAfterViewInit(): void {
    console.log($(".ui", this.rootNode.nativeElement));
    $(".ui.dropdown", this.rootNode.nativeElement).dropdown();
  }

  generarRonda() {
    this.fixture.generarRondas()
      .subscribe(ronda => {
        this.fases$.refetch();
      })
  }
}
