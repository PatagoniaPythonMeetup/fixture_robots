import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PageNotFoundComponent } from './pages/not-found/page-not-found.component';
import { PageGeneralComponent } from "./pages/general/page-general.component";
import { PageFaseComponent } from "./pages/fase/page-fase.component";
import { PagePosicionesComponent } from "./pages/posiciones/page-posiciones.component";

const routes: Routes = [
  { path: 'general', component: PageGeneralComponent },
  { path: 'fase/:numero', component: PageFaseComponent },
  { path: 'posiciones', component: PagePosicionesComponent },
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
