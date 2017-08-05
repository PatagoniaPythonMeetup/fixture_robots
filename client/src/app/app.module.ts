import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ApolloModule } from "apollo-angular";
import { getClient } from "./apollo-client";
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { FooterComponent } from './layout/footer/footer.component';
import { MainComponent } from './layout/main/main.component';
import { MenuComponent } from './layout/menu/menu.component';
import { RobotsScoreTableComponent } from './robots-score-table/robots-score-table.component';
import { AppRoutingModule } from "./app-routing.module";

@NgModule({
  declarations: [
    AppComponent,
    PageNotFoundComponent,
    FooterComponent,
    MainComponent,
    MenuComponent,
    RobotsScoreTableComponent
  ],
  imports: [
    BrowserModule,
    ApolloModule.withClient(getClient),
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }