import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RobotsScoreTableComponent } from './robots-score-table.component';

describe('RobotsScoreTableComponent', () => {
  let component: RobotsScoreTableComponent;
  let fixture: ComponentFixture<RobotsScoreTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RobotsScoreTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RobotsScoreTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
