import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RobotsScoreComponent } from './robots-score.component';

describe('RobotsScoreComponent', () => {
  let component: RobotsScoreComponent;
  let fixture: ComponentFixture<RobotsScoreComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RobotsScoreComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RobotsScoreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
