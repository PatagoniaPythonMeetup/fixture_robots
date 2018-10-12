import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-page-not-found',
  template: `
<div class="ui centered card">
  <a class="image" href="#">
    <img class="ui centered medium image" src="/assets/images/404.png">
  </a>
  <div class="content">
    <a class="header" href="#">404 oops...</a>
    <div class="meta">
      <a>page not found</a>
    </div>
  </div>
</div>
  `,
})
export class PageNotFoundComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
