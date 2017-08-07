import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
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
