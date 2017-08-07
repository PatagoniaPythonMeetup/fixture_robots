import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ApolloModule } from "apollo-angular";
import { getClient } from "./apollo-client";
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { FooterComponent } from './layout/footer/footer.component';
import { MainComponent } from './layout/main/main.component';
import { MenuComponent } from './layout/menu/menu.component';
import { AppRoutingModule } from "./app-routing.module";
import { PageGeneralComponent } from './page-general/page-general.component';
import { PageFaseComponent } from './page-fase/page-fase.component';
import { GrupoComponent } from './components/grupo/grupo.component';
import { RobotsScoreComponent } from './components/robots-score/robots-score.component';
import { ClasificacionComponent } from './components/clasificacion/clasificacion.component';
import { RondaComponent } from './components/ronda/ronda.component';

@NgModule({
  declarations: [
    AppComponent,
    PageNotFoundComponent,
    FooterComponent,
    MainComponent,
    MenuComponent,
    PageGeneralComponent,
    PageFaseComponent,
    GrupoComponent,
    RobotsScoreComponent,
    ClasificacionComponent,
    RondaComponent
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
