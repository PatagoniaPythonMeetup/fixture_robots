import unittest
import random

from server import Robot, Fixture

class TestGeneradoresDeRonda(unittest.TestCase):
    def setUp(self):
        self.robots = [
            Robot("Ultron I", "Los Avengers","Nick Fury"),
            Robot("Wall-e I","Pixar","Sr. Disney"),
            Robot("Sony I","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop I","O.C.P.","Bob Morthon"),
            Robot("Terminator I","Skynet","Jhon Connor"),
            Robot("R2-D2 I","La Republica","Obiwan Kenobi"),
            Robot("3-CPO I","La Republica","Anakin Skywalker"),
            Robot("BB-8 I","La Republica","Poe Dameron"),
            Robot("Ultron II", "Los Avengers","Nick Fury"),
            Robot("Wall-e II","Pixar","Sr. Disney"),
            Robot("Sony II","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop II","O.C.P.","Bob Morthon"),
            Robot("Terminator II","Skynet","Jhon Connor"),
            Robot("R2-D2 II","La Republica","Obiwan Kenobi"),
            Robot("3-CPO II","La Republica","Anakin Skywalker"),
            Robot("BB-8 II","La Republica","Poe Dameron")
        ]
        random.shuffle(self.robots)

    def test_sin_robots(self):
        fixture = Fixture([])
        self.assertEqual(fixture.finalizado(), True)
        
    def test_un_robot(self):
        robots = self.robots[:]
        robot = random.choice(robots)
        fixture = Fixture([robot])
        self.assertEqual(fixture.finalizado(), False)
        ronda = fixture.generar_ronda()
        self.assertEqual(fixture.finalizado(), True)
        self.assertEqual(robot, fixture.ganador())

    def test_robots_en_ronda(self):
        robots = self.robots[:]
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_pares_en_ronda(self):
        robots = self.robots[:]
        while len(robots) % 2 != 0:
            robots.pop()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_impares_en_ronda(self):
        robots = self.robots[:]
        while len(robots) % 2 != 1:
            robots.pop()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_random_en_ronda(self):
        robots = self.robots[:]
        robots = robots[random.randint(1, len(robots)):]
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        self.assertEqual(set(robots), set(ronda.robots))

class TestGanadores(unittest.TestCase):
    def setUp(self):
        self.robots = [
            Robot("Ultron I", "Los Avengers","Nick Fury"),
            Robot("Wall-e I","Pixar","Sr. Disney"),
            Robot("Sony I","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop I","O.C.P.","Bob Morthon"),
            Robot("Terminator I","Skynet","Jhon Connor"),
            Robot("R2-D2 I","La Republica","Obiwan Kenobi"),
            Robot("3-CPO I","La Republica","Anakin Skywalker"),
            Robot("BB-8 I","La Republica","Poe Dameron"),
            Robot("Ultron II", "Los Avengers","Nick Fury"),
            Robot("Wall-e II","Pixar","Sr. Disney"),
            Robot("Sony II","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop II","O.C.P.","Bob Morthon"),
            Robot("Terminator II","Skynet","Jhon Connor"),
            Robot("R2-D2 II","La Republica","Obiwan Kenobi"),
            Robot("3-CPO II","La Republica","Anakin Skywalker"),
            Robot("BB-8 II","La Republica","Poe Dameron")
        ]
        random.shuffle(self.robots)

    def test_ganador_1_en_ronda_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        for e in ronda.encuentros:
            ganadores.add(e.robot_1)
            ronda.gano(e.robot_1)
        self.assertEqual(set(ganadores), set(ronda.ganadores()))
        
    def test_ganador_2_en_ronda_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        for e in ronda.encuentros:
            ganadores.add(e.robot_2)
            ronda.gano(e.robot_2)
        self.assertEqual(set(ganadores), set(ronda.ganadores()))

    def test_ganador_del_torneo(self):
        robots = self.robots[:]
        ganador = random.choice(robots)
        fixture = Fixture(robots)
        while not fixture.finalizado():
            ronda = fixture.generar_ronda()
            while not ronda.finalizada() or ronda.vuelta() < 5:
                for e in ronda.encuentros:
                    robot = ganador if e.participa(ganador) else random.choice([e.robot_1, e.robot_2])
                    ronda.gano(robot)
        self.assertEqual(ganador, fixture.ganador())

    def test_ganador_impares_del_torneo(self):
        robots = self.robots[:]
        while len(robots) % 2 != 1:
            robots.pop()
        ganador = random.choice(robots)
        fixture = Fixture(robots)
        while not fixture.finalizado():
            ronda = fixture.generar_ronda()
            while not ronda.finalizada() or ronda.vuelta() < 5:
                for e in ronda.encuentros:
                    robot = ganador if e.participa(ganador) else random.choice([e.robot_1, e.robot_2])
                    ronda.gano(robot)
        self.assertEqual(ganador, fixture.ganador())

if __name__ == '__main__':
    unittest.main()