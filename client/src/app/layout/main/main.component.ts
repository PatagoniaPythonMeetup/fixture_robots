import { Estado } from '../../fixture.service';
import { FixtureService } from '../../fixture.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  template: `
<div class="ui main text container">
  <router-outlet></router-outlet>
</div>
`,
  styles: [`
.ui.main.container {
  margin-top: 4em;
  margin-bottom: 7em;
}
`]
})
export class MainComponent implements OnInit {
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
