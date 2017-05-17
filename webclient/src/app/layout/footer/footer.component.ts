import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit, AfterViewChecked, AfterViewInit, AfterContentChecked, DoCheck } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  estado: Estado

  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.estado = this.fixture.getEstado();
    this.fixture.estado.subscribe(estado => this.estado = estado);
  }
  
}
