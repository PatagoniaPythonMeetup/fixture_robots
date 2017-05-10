import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'encuentro-card',
  templateUrl: './encuentro-card.component.html',
  styleUrls: ['./encuentro-card.component.css']
})
export class EncuentroCardComponent implements OnInit {
  @Input() encuentro: any = {}

  constructor() { }

  ngOnInit() {
  }

}
