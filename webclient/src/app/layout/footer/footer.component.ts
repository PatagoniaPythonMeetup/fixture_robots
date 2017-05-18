import { Observable } from 'rxjs/Rx';
import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewChecked, AfterViewInit, AfterContentChecked, DoCheck } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  TRACKS_EN_PARALELO: Number = 1
  encuentros: Array<any> = []
  estado: Estado

  constructor(private fixture: FixtureService) { 
    this.fixture.estado.subscribe(estado => this.cargarEstado(estado))
  }

  ngOnInit() {
    
  }

  cargarEstado(estado: Estado) {
    this.estado = estado
    if (estado.compitiendo) {
      estado.encuentros.forEach(e => this.fixture.encuentro(e)
        .subscribe(e => this.encuentros = [e])
      )  
    }
  }

}
