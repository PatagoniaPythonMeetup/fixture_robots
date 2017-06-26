import unittest
import random

from server import Fixture

from base import TestBase

class TestGanadores(TestBase):
    def test_ganador_1_en_eliminacion_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        fase = fixture.eliminacion()
        fase.generar_rondas()
        for e in fase.get_encuentros():
            ganadores.add(e.robot_1)
            e.agregar_ganador(e.robot_1)
        self.assertEqual(set(ganadores), set(fase.ganadores()))

    def test_ganador_2_en_eliminacion_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        fase = fixture.eliminacion()
        fase.generar_rondas()
        for e in fase.get_encuentros():
            ganadores.add(e.robot_2)
            e.agregar_ganador(e.robot_2)
        self.assertEqual(set(ganadores), set(fase.ganadores()))

    def test_ganador_por_eliminacion_del_torneo(self):
        robots = self.robots[:]
        ganador = random.choice(robots)
        fixture = Fixture(robots)
        fase = fixture.eliminacion()
        while not fixture.finalizado():
            fase.generar_rondas()
            for e in fase.get_encuentros():
                while not e.finalizado():
                    robot = ganador if e.participa(ganador) else random.choice([e.robot_1, e.robot_2])
                    e.agregar_ganador(robot)
        self.assertEqual(ganador, fixture.ganador())

    def test_ganador_por_eliminacion_impares_del_torneo(self):
        robots = self.robots[:]
        while len(robots) % 2 != 1:
            robots.pop()
        ganador = random.choice(robots)
        fixture = Fixture(robots)
        fase = fixture.eliminacion()
        while not fixture.finalizado():
            fase.generar_rondas()
            for e in fase.get_encuentros():
                while not e.finalizado():
                    robot = ganador if e.participa(ganador) else random.choice([e.robot_1, e.robot_2])
                    e.agregar_ganador(robot)
        self.assertEqual(ganador, fixture.ganador())

    def test_ganador_por_clasificacion_del_torneo(self):
        robots = self.robots[:24]
        fixture = Fixture(robots)
        fase = fixture.clasificacion(4)
        ganadores = [g.robots[0] for g in fase.get_grupos()]
        self.assertEqual([len(g) for g in fase.get_grupos()], [6,6,6,6])
        while not fixture.finalizado():
            fase.generar_rondas()
            for e in fase.get_encuentros():
                while not e.finalizado():
                    if e.robot_1 in ganadores:
                        robot = e.robot_1
                    elif e.robot_2 in ganadores:
                         robot = e.robot_2
                    else:
                        robot = random.choice([e.robot_1, e.robot_2])
                    e.agregar_ganador(robot)
        self.assertEqual(ganadores, fixture.ganadores())
    
    def test_ganador_por_clasificacion_tct_del_torneo(self):
        robots = self.robots[:32]
        fixture = Fixture(robots)
        fase = fixture.clasificacion(8)
        ganadores = [g.robots[0] for g in fase.get_grupos()]
        self.assertEqual([len(g) for g in fase.get_grupos()], [4,4,4,4,4,4,4,4])
        while not fixture.finalizado():
            fase.generar_rondas(tct=True)
            for e in fase.get_encuentros():
                while not e.finalizado():
                    if e.robot_1 in ganadores:
                        robot = e.robot_1
                    elif e.robot_2 in ganadores:
                         robot = e.robot_2
                    else:
                        robot = random.choice([e.robot_1, e.robot_2])
                    e.agregar_ganador(robot)
        self.assertEqual(ganadores, fixture.ganadores())
    
    def test_ganador_por_clasificacion_impares_tct_del_torneo(self):
        robots = self.robots[:27]
        fixture = Fixture(robots)
        fase = fixture.clasificacion(8)
        ganadores = [g.robots[0] for g in fase.get_grupos()]
        self.assertEqual([len(g) for g in fase.get_grupos()], [3,3,3,3,3,4,4,4])
        while not fixture.finalizado():
            fase.generar_rondas(tct=True)
            for e in fase.get_encuentros():
                while not e.finalizado():
                    if e.robot_1 in ganadores:
                        robot = e.robot_1
                    elif e.robot_2 in ganadores:
                         robot = e.robot_2
                    else:
                        robot = random.choice([e.robot_1, e.robot_2])
                    e.agregar_ganador(robot)
        self.assertEqual(ganadores, fixture.ganadores())