import { FixtureService } from '../../fixture.service';
import { Component, OnInit, AfterViewChecked, AfterViewInit, AfterContentChecked, DoCheck } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  estado: any = {compitiendo: false}
  constructor(private fixture: FixtureService) {
    this.fixture.estado.subscribe(estado => this.estado = estado);
  }

  ngOnInit() {
  }
  
}
