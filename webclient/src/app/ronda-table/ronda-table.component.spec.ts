import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RondaTableComponent } from './ronda-table.component';

describe('RondaTableComponent', () => {
  let component: RondaTableComponent;
  let fixture: ComponentFixture<RondaTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RondaTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RondaTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
