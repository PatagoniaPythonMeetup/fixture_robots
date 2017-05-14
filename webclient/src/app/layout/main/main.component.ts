import { Observable } from 'rxjs/Rx';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  rondas$: Observable<any>

  constructor(private fixture: FixtureService) { 
    this.rondas$ = this.fixture.rondas()
  }

  ngOnInit() {
  }

}
