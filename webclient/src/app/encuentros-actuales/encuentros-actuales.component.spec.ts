import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EncuentrosActualesComponent } from './encuentros-actuales.component';

describe('EncuentrosActualesComponent', () => {
  let component: EncuentrosActualesComponent;
  let fixture: ComponentFixture<EncuentrosActualesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EncuentrosActualesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EncuentrosActualesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
