import { RondaTableComponent } from './ronda-table/ronda-table.component';
import { RobotsScoreTableComponent } from './robots-score-table/robots-score-table.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const routes: Routes = [
  { path: 'robots', component: RobotsScoreTableComponent },
  { path: 'ronda/:numero', component: RondaTableComponent },
  {
    path: '',
    children: []
  },
  { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
