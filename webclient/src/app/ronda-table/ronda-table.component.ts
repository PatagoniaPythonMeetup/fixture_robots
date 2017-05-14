import { Observable } from 'rxjs/Rx';
import { FixtureService } from '../fixture.service';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'ronda-table',
  templateUrl: './ronda-table.component.html',
  styleUrls: ['./ronda-table.component.css']
})
export class RondaTableComponent implements OnInit {
  @Input() ronda: any

  constructor(private fixture: FixtureService) { 
  }

  ngOnInit() {
  }

}
