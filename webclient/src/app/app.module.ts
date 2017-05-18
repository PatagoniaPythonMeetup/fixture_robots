import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ApolloModule } from 'apollo-angular';

//Components
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RobotCardComponent } from './robot-card/robot-card.component';

import { getClient } from './apollo-client';
import { EncuentroCardComponent } from './encuentro-card/encuentro-card.component';
import { RobotsScoreTableComponent } from './robots-score-table/robots-score-table.component';
import { MenuComponent } from './layout/menu/menu.component';
import { MainComponent } from './layout/main/main.component';
import { FooterComponent } from './layout/footer/footer.component';
import { RondaTableComponent } from './ronda-table/ronda-table.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    RobotCardComponent,
    EncuentroCardComponent,
    RobotsScoreTableComponent,
    MenuComponent,
    MainComponent,
    FooterComponent,
    RondaTableComponent,
    PageNotFoundComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ApolloModule.withClient(getClient),
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
