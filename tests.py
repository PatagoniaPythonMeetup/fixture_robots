import unittest
import random

from server import Robot, Fixture

class TestBase(unittest.TestCase):
    def setUp(self):
        self.robots = [
            Robot("Ultron I", "Los Avengers","Nick Fury"),
            Robot("Wall-e I","Pixar","Sr. Disney"),
            Robot("EVA I","Pixar","Sr. Disney"),
            Robot("Sony I","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop I","O.C.P.","Bob Morthon"),
            Robot("Terminator I","Skynet","Jhon Connor"),
            Robot("R2-D2 I","La Republica","Obiwan Kenobi"),
            Robot("3-CPO I","La Republica","Anakin Skywalker"),
            Robot("BB-8 I","La Republica","Poe Dameron"),
            Robot("Ultron II", "Los Avengers","Nick Fury"),
            Robot("Wall-e II","Pixar","Sr. Disney"),
            Robot("EVA II","Pixar","Sr. Disney"),
            Robot("Sony II","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop II","O.C.P.","Bob Morthon"),
            Robot("Terminator II","Skynet","Jhon Connor"),
            Robot("R2-D2 II","La Republica","Obiwan Kenobi"),
            Robot("3-CPO II","La Republica","Anakin Skywalker"),
            Robot("BB-8 II","La Republica","Poe Dameron"),
            Robot("Rodney I", "Robots", "Sr. Ewan McGregor"),
            Robot("Rodney II", "Robots", "Sr. Ewan McGregor"),
            Robot("ED 209 I", "O.C.P.", "Bob Morthon"),
            Robot("ED 209 II", "O.C.P.", "Bob Morthon"),
            Robot("Johnny 5 I", "Cortocircuito", "Ally Sheedy"),
            Robot("Johnny 5 II", "Cortocircuito", "Ally Sheedy"),
            Robot("T-800 I", "Cyberdyne Systems", "Jhon Connor"),
            Robot("T-800 II", "Cyberdyne Systems", "Jhon Connor"),
            Robot("T-1000 I", "Cyberdyne Systems", "Arnie"),
            Robot("T-1000 II", "Cyberdyne Systems", "Arnie"),
            Robot("Roy Batty I", "Blade Runner", "Roy"),
            Robot("Roy Batty II", "Blade Runner", "Roy"),
            Robot("HAL 9000 I", "Discovery Uno", "David Bowman"),
            Robot("HAL 9000 II", "Discovery Uno", "David Bowman"),
            Robot("Ash I", "Nostromo", "Ellen Ripley"),
            Robot("Ash II", "Nostromo", "Ellen Ripley"),
            Robot("Optimus Prime I", "Transformers", "Ellen Ripley"),
            Robot("Optimus Prime II", "Transformers", "Ellen Ripley"),
            Robot("David Swinton I", "IA", "Ellen Ripley"),
            Robot("David Swinton II", "IA", "Ellen Ripley"),
            Robot("Teddy I", "IA", "Haley Joel Osment"),
            Robot("Teddy II", "IA", "Haley Joel Osment"),
            Robot("Centinelas I", "Matrix", "Neo"),
            Robot("Centinelas II", "Matrix", "Neo"),
            Robot("Bender I", "Futurama", "Philip J. Fry"),
            Robot("Bender II", "Futurama", "Philip J. Fry")
        ]
        random.shuffle(self.robots)


class TestGeneradoresDeRonda(TestBase):
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

class TestGanadores(TestBase):
    def test_ganador_1_en_ronda_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        for e in ronda.encuentros:
            ganadores.add(e.robot_1)
            e.gano(e.robot_1)
        self.assertEqual(set(ganadores), set(ronda.ganadores()))
        
    def test_ganador_2_en_ronda_1(self):
        robots = self.robots[:]
        ganadores = set()
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda()
        for e in ronda.encuentros:
            ganadores.add(e.robot_2)
            e.gano(e.robot_2)
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
                    e.gano(robot)
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
                    e.gano(robot)
        self.assertEqual(ganador, fixture.ganador())

class TestTorneo(TestBase):
    def test_torneo_de_ocho(self):
        robots = self.robots[:8]
        scores = [[robot, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        while not fixture.finalizado():
            ronda = fixture.generar_ronda()
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado() or encuentro.jugadas() < 5:
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0] - s[1], swin[6] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3] + 1, slose[4], slose[5] + s[1] - s[0], slose[6]]
        scores = sorted(scores, key=lambda t: t[6], reverse=True)
        self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

if __name__ == '__main__':
    unittest.main()