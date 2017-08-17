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
import { RondaComponent } from './components/ronda/ronda.component';
import { ModalComponent, ModalTagsDirective } from './layout/modal/modal.component';
import { FaseComponent } from './components/fase/fase.component';
import { ScoreComponent } from './components/score/score.component';
import { PagePosicionesComponent } from './page-posiciones/page-posiciones.component';

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
    RondaComponent,
    ModalComponent,
    ModalTagsDirective,
    FaseComponent,
    ScoreComponent,
    PagePosicionesComponent
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
