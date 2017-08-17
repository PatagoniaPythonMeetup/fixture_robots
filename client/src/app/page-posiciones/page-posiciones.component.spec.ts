import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PagePosicionesComponent } from './page-posiciones.component';

describe('PagePosicionesComponent', () => {
  let component: PagePosicionesComponent;
  let fixture: ComponentFixture<PagePosicionesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PagePosicionesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PagePosicionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
