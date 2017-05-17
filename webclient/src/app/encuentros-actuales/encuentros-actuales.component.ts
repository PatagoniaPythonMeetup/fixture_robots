import { Observable } from 'rxjs/Rx';
import { Component, OnInit } from '@angular/core';

import { FixtureService } from '../fixture.service';

@Component({
  selector: 'encuentros-actuales',
  templateUrl: './encuentros-actuales.component.html',
  styleUrls: ['./encuentros-actuales.component.css']
})
export class EncuentrosActualesComponent implements OnInit {
  encuentrosActuales$: Observable<any>
  TRACKS_EN_PARALELO: Number = 2
  
  constructor(private fixture: FixtureService) { }

  ngOnInit() {
    this.encuentrosActuales$ = this.fixture.encuentrosActuales();
  }

}
