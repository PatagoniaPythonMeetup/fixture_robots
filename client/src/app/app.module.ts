import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FooterComponent } from './layout/footer/footer.component';
import { MainComponent } from './layout/main/main.component';
import { MenuComponent } from './layout/menu/menu.component';
import { ModalComponent, ModalTagsDirective } from './layout/modal/modal.component';
import { GraphQLModule } from './graphql.module';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { ApolloModule, Apollo } from 'apollo-angular';
import { PageNotFoundComponent } from './pages/not-found/page-not-found.component';
import { PageGeneralComponent } from './pages/general/page-general.component';
import { PageFaseComponent } from './pages/fase/page-fase.component';
import { GrupoComponent } from './components/grupo/grupo.component';
import { RondaComponent } from './components/ronda/ronda.component';
import { FaseComponent } from './components/fase/fase.component';
import { ScoreComponent } from './components/score/score.component';
import { PagePosicionesComponent } from './pages/posiciones/page-posiciones.component';
import { FixtureService } from './fixture.service';
import { HttpLink } from 'apollo-angular-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

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
    ModalTagsDirective,
    FaseComponent,
    ScoreComponent,
    PagePosicionesComponent,
    ModalComponent
  ],
  imports: [
    BrowserModule,
    ApolloModule,
    GraphQLModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [FixtureService],
  bootstrap: [AppComponent]
})
export class AppModule {
 }
