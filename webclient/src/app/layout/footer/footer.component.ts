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
      let encuentros = this.encuentros.map(e => e.numero)
      estado.encuentros.forEach((numero, index) => {
        if (encuentros.length === 0 || encuentros.indexOf(numero) == -1) {
          this.fixture.encuentro(estado.encuentros[index])
            .subscribe((e: any) => {
              encuentros[index] = e
              this.encuentros = encuentros
            })
        }
      })
    } else { this.encuentros = [] }
  }

}
