import {
    ChangeDetectionStrategy,
    Component,
    Directive,
    ElementRef,
    EventEmitter,
    Input,
    OnDestroy,
    Output,
    ViewChild,
} from '@angular/core';

declare var jQuery: any;

@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'modal',
  template: `
<div class="ui modal {{class}}" #modal>
    <i class="close icon"></i>
    <div [ngClass]="{'icon': icon}" class="header">
        <i *ngIf="icon" class="icon {{icon}}"></i>
        {{title}}
    </div>
    <div class="content">
        <ng-content select="modal-content"></ng-content>
    </div>
    <div class="actions">
        <ng-content select="modal-actions"></ng-content>
    </div>
</div>
  `,
})
export class ModalComponent implements OnDestroy {
  @Input() class: string;
  @Input() title: string;
  @Input() icon: string;
  @ViewChild("modal") modal: ElementRef;
  @Output() onModalShow: EventEmitter<boolean> = new EventEmitter<boolean>();
  @Output() onModalHide: EventEmitter<boolean> = new EventEmitter<boolean>();

  show(data?: {}) {
    jQuery(this.modal.nativeElement)
      .modal(data || {})
      .modal("toggle");

    this.onModalShow.next(true);
  }

  hide() {
    jQuery(this.modal.nativeElement)
      .modal("hide");

    this.onModalHide.emit(true);
  }

  ngOnDestroy(): void {
    const parent = this.modal.nativeElement.parentElement;
    parent.removeChild(this.modal.nativeElement);
  }
}

@Directive({ selector: 'modal-content, modal-actions' })
export class ModalTagsDirective {
  // No behavior
  // The only purpose is to "declare" the tag in Angular2
}