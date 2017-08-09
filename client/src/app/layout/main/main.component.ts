import { Estado } from '../../fixture.service';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  estado: Estado

  constructor(private fixture: FixtureService) { 
    this.fixture.estado.subscribe(estado => this.setEstado(estado))
  }

  ngOnInit() {
    
  }

  setEstado(estado: Estado) {
    this.estado = estado
  }

}
