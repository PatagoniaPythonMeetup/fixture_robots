import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PageGeneralComponent } from './page-general.component';

describe('PageGeneralComponent', () => {
  let component: PageGeneralComponent;
  let fixture: ComponentFixture<PageGeneralComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageGeneralComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PageGeneralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
