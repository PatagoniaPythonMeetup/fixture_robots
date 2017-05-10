import { Observable } from 'rxjs/Rx';
import { FixtureService } from './fixture.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [FixtureService]
})
export class AppComponent {
  title = 'Competencia Robótica';
  
  robots$: Observable<any>;
  encuentrosActuales$: Observable<any>;

  constructor(private fixture: FixtureService) {
    this.encuentrosActuales$ = this.fixture.encuentrosActuales();
    this.robots$ = this.fixture.robots();
  }
}
