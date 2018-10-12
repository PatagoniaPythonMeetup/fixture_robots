import { FixtureService, Estado } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  template: `
<div class="ui inverted vertical footer segment">
  <div class="ui center aligned container">
    <img src="assets/images/unpsjb.png" class="ui centered mini image">
      <div class="ui horizontal inverted small divided link list">
        <a class="item" href="http://www.dit.ing.unp.edu.ar/">Universidad Nacional de la Patagonia San Juan Bosco - Departamento de Informática - Trelew</a><br/>
    </div>
  </div>
</div>
  `,
  styles: [`
.ui.footer {
  position: fixed;
  bottom: 0px;
  width: 100%;
}
  `]
})
export class FooterComponent implements OnInit {
  estado: Estado

  constructor(private fixture: FixtureService) { 
    this.fixture.estado$.subscribe(estado => this.setEstado(estado))
  }

  ngOnInit() {
    
  }

  setEstado(estado: Estado) {
    this.estado = estado
  }

}
