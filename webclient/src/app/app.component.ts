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
  title = 'app works!';
  robots$: Observable<any>;

  constructor(private fixture: FixtureService) {
    this.robots$ = this.fixture.getRobots();
    this.robots$.subscribe(robots => console.log(robots));
  }
}
