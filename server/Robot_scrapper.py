#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import threading
import urllib.request

class Robot_scrapper(object):
	""" Objeto encargado de obtener y mantener actualizados los robots inscriptos a la competencia,
	organizados según sus categorías (seguidor de linea, sumo, mini zumo y futbol) """

	def __init__(self, pagina="http://robocomp.dit.ing.unp.edu.ar/getRobots", reload_data=False):
		self.pagina = pagina
		self.equipos = None
		self.raw_data = ""
		self.reload = reload_data
		self.scrap_robots()

	def scrap_robots(self):
		"""  Obtiene los robots desde la pagina """
		rta_page = urllib.request.urlopen( self.pagina ).read().decode()
		if self.reload:
			threading.Timer(60.0, self.scrap_robots).start()

		if (self.raw_data != rta_page):
			self.build_equipos(rta_page)
		return

    def build_equipos(self, raw_robots):
        """ """
        self.raw_data = raw_robots
        json_robots = json.loads(raw_robots)
        self.equipos = []
        for data_r in json_robots:
            componentes = []
            p = data_r["profesor"]
            p["rol"] = "Profesor"
            profesor = encargado = Participante(*list(p.values()))
            
            e = data_r["representante"]
            e["rol"] = "Representante"
            encargado = Participante(*list(e.values()))
            
            lista_alumnos = data_r["alumnos"]
            lista_alumnos = []
            for a in lista_alumnos:
                lista_alumnos.append( Participante(a["nombre"], a["dni"], a["email"], "Alumno") )

            rob = Robot(data_r["nombre"], data_r["escuela"], encargado )
            componentes.append( rob )
            componentes.append( data_r["categoria"] )
            componentes.append( profesor )
            componentes.append( encargado )
            componentes.append( lista_alumnos )
            componentes.append( data_r["escuela"] )
            componentes.append( rob.escudo )
            self.equipos.append( Equipo(*componentes) )
            
        return
            

	def get_equipos(self, categoria=None):
		if(categoria):
			return [equipo for equipo in self.equipos if equipo.categoria == categoria]
		return self.equipos

	def set_reload(self):
		self.reload = True
		return

	def stop_reload(self):
		self.reload = False
		return