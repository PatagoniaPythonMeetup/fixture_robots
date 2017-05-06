import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { ApolloModule } from 'apollo-angular';

//Components
import { AppComponent } from './app.component';
import { RobotCardComponent } from './robot-card/robot-card.component';

import { getClient } from './apollo-client';

@NgModule({
  declarations: [
    AppComponent,
    RobotCardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ApolloModule.withClient(getClient)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
