import { Observable } from 'rxjs/Rx';
import { Component, OnInit } from '@angular/core';

import { FixtureService } from '../fixture.service';

@Component({
  selector: 'encuentros-actuales',
  templateUrl: './encuentros-actuales.component.html',
  styleUrls: ['./encuentros-actuales.component.css']
})
export class EncuentrosActualesComponent implements OnInit {
  encuentrosActuales$: Observable<any>;
  
  constructor(private fixture: FixtureService) {
    this.encuentrosActuales$ = this.fixture.encuentrosActuales();
  }

  ngOnInit() {
  }

}
