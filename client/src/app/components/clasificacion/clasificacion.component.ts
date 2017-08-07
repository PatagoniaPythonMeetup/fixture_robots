import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'clasificacion',
  templateUrl: './clasificacion.component.html',
  styleUrls: ['./clasificacion.component.css']
})
export class ClasificacionComponent implements OnInit {
  @Input() fase: any
  
  constructor() { }

  ngOnInit() {
  }

}
