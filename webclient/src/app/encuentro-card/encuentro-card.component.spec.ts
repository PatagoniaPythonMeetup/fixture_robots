import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EncuentroCardComponent } from './encuentro-card.component';

describe('EncuentroCardComponent', () => {
  let component: EncuentroCardComponent;
  let fixture: ComponentFixture<EncuentroCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EncuentroCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EncuentroCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
