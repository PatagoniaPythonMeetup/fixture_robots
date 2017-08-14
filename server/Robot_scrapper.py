#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import threading
import urllib.request
from .Participante import Participante
from .Equipo import Equipo
from .Robot import Robot

class Robot_scrapper(object):
    """ Objeto encargado de obtener y mantener actualizados los robots inscriptos a la competencia. """

    def __init__(self, pagina="http://robocomp.dit.ing.unp.edu.ar/getRobots", reload_data=False):
        self.pagina = pagina
        self.equipos = []
        self.reload = reload_data
        self.scrap_equipos()

    def scrap_equipos(self):
        """  Obtiene los datos de los equipos desde la pagina """
        rta_page = urllib.request.urlopen( self.pagina ).read().decode()
        self.build_equipos(rta_page)
        if self.reload:
            threading.Timer(60.0, self.scrap_equipos).start()
        return

    def build_equipos(self, raw_equipos):
        """ Construye los equipos a partir de la información obtenida desde la pagina """
        json_equipos = json.loads(raw_equipos)
        new_equipos = []
        for data_r in json_equipos:
            componentes = []
            participante = data_r["profesor"]
            profesor = Participante(participante["nombre"], participante["dni"], participante["email"], "Profesor")
            
            participante = data_r["representante"]
            encargado = Participante(participante["nombre"], participante["dni"], participante["email"], "Representante")
            
            lista_alumnos = data_r["alumnos"]
            alumnos_equipo = []
            for participante in lista_alumnos:
                alumnos_equipo.append(Participante(participante["nombre"], participante["dni"], participante["email"], "Alumno"))

            rob = Robot(data_r["nombre"], data_r["escuela"], encargado )
            componentes.append( rob )
            componentes.append( data_r["categoria"] )
            componentes.append( profesor )
            componentes.append( encargado )
            componentes.append( alumnos_equipo )
            componentes.append( data_r["escuela"] )
            componentes.append( rob.escudo )
            new_equipos.append( Equipo(*componentes) )

        for equipo in new_equipos:
            if equipo not in self.equipos:
                self.equipos.append(equipo)
        return
            

    def get_equipos(self, categoria=None):
        """ Retorna todos los equipos. Si 'categoria' es distinto de None, retornara solo los 
            equipos que correspondan a la categoria dada """
        if(categoria):
            return [equipo for equipo in self.equipos if equipo.categoria == categoria]
        return self.equipos

    def set_reload(self):
        self.reload = True
        return

    def stop_reload(self):
        self.reload = False
        return