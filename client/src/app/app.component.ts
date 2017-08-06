import { FixtureService } from './fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [FixtureService]
})
export class AppComponent implements OnInit {
  constructor(private fixture: FixtureService) {
    
  }

  ngOnInit() {
    this.fixture.getEstado()
  }

}
