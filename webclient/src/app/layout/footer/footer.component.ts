import { FixtureService } from '../../fixture.service';
import { Component, OnInit, AfterViewChecked, AfterViewInit, AfterContentChecked, DoCheck } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit, DoCheck {
  enCurso: Boolean = false
  constructor(private fixture: FixtureService) { }

  ngOnInit() {
  }

  ngDoCheck(): void {
    console.log("ngDoCheck");
  }
  
}
