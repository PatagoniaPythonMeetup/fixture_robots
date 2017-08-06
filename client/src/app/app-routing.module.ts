import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { PageGeneralComponent } from "./page-general/page-general.component";
import { PageFaseComponent } from "./page-fase/page-fase.component";

const routes: Routes = [
  { path: 'general', component: PageGeneralComponent },
  { path: 'fase/:numero', component: PageFaseComponent },
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
