import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'fase',
  templateUrl: './fase.component.html',
  styleUrls: ['./fase.component.css']
})
export class FaseComponent implements OnInit {
  @Input() fase: any
  
  constructor() { }

  ngOnInit() {
  }

}