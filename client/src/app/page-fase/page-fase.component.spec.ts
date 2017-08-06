import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PageFaseComponent } from './page-fase.component';

describe('PageFaseComponent', () => {
  let component: PageFaseComponent;
  let fixture: ComponentFixture<PageFaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageFaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PageFaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
