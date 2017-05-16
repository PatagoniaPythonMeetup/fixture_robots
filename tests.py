import unittest
import random
import json

from server import Robot, Fixture, Encuentro

class TestEncuentros(unittest.TestCase):
    def test_estado_inicial(self):
        self.assertEqual(Encuentro("r1", "r2").finalizado(), False)

    def test_r1r2r2(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, r2)
        self.assertEqual(e1.finalizado(), False)
        e1.gano(r1)
        self.assertEqual(e1.finalizado(), False)
        e1.gano(r2)
        self.assertEqual(e1.finalizado(), False)
        e1.gano(r2)
        self.assertEqual(e1.finalizado(), True)

    def test_r1r1(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, r2)
        self.assertEqual(e1.finalizado(), False)
        e1.gano(r1)
        self.assertEqual(e1.finalizado(), False)
        e1.gano(r1)
        self.assertEqual(e1.finalizado(), True)

class TestRobots(unittest.TestCase):
    def test_robots_iguales(self):
        r1 = Robot("Ultron", "Los Avengers", "Nick Fury")
        r2 = Robot("Wall-e", "Pixar", "Sr. Disney")
        r3 = Robot("Ultron", "Los Avengers", "Nick Fury")
        self.assertTrue(not r1 is r2)
        self.assertTrue(not r1 == r2)
        self.assertTrue(r1 is r1)
        self.assertTrue(r1 == r1)
        self.assertTrue(not r1 is r3)
        self.assertTrue(r1 == r3)

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
        self.assertEqual(fixture.iniciado(), False)
        self.assertEqual(fixture.finalizado(), True)
        
    def test_con_robots(self):
        fixture = Fixture(self.robots)
        self.assertEqual(fixture.iniciado(), False)
        self.assertEqual(fixture.finalizado(), False)
    
    def test_con_robots_y_ronda(self):
        fixture = Fixture(self.robots)
        ronda = fixture.generar_ronda()
        self.assertEqual(fixture.iniciado(), True)
        self.assertEqual(fixture.finalizado(), False)
    
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

    def test_tres_robots(self):
        robots = self.robots[:3]
        fixture = Fixture(robots)
        ronda = fixture.generar_ronda(True)
        self.assertEqual(set(robots), set(ronda.robots))
        self.assertEqual(3, len(ronda.encuentros))

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
            while not ronda.finalizada():
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
            while not ronda.finalizada():
                for e in ronda.encuentros:
                    robot = ganador if e.participa(ganador) else random.choice([e.robot_1, e.robot_2])
                    e.gano(robot)
        self.assertEqual(ganador, fixture.ganador())

class TestTorneo(TestBase):
    def test_torneo_de_ocho(self):
        robots = self.robots[:8]
        # (robot, jugados, triunfos, empates, derrotas, a favor, en contra, diferencia, puntos)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        while not fixture.finalizado():
            ronda = fixture.generar_ronda()
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        scores = sorted(scores, key=lambda t: t[8], reverse=True)
        self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

    def test_torneo_de_tres_tct(self):
        robots = self.robots[:3]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            ronda = fixture.generar_ronda(True)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

    def test_torneo_de_cinco_tct(self):
        robots = self.robots[:5]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            ronda = fixture.generar_ronda(True)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

    def test_torneo_de_doce_con_tct_en_tres(self):
        robots = self.robots[:12]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            r = len(fixture.robots_en_juego())
            ronda = fixture.generar_ronda(r <= 3)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))
    
    def test_torneo_de_veintiuno_con_tct_en_cinco(self):
        robots = self.robots[:21]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            r = len(fixture.robots_en_juego())
            ronda = fixture.generar_ronda(r <= 5)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

    def test_torneo_de_cuarenta_y_tres_con_tct_en_tres(self):
        robots = self.robots[:43]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            r = len(fixture.robots_en_juego())
            ronda = fixture.generar_ronda(r <= 3)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))

    def test_torneo_de_cuarenta_y_cuatro_con_tct_en_once(self):
        robots = self.robots[:44]
        fixture = Fixture(robots)
        scores = [[robot, 0, 0, 0, 0, 0, 0, 0, 0] for robot in robots ]
        fixture = Fixture(robots)
        ronda = None
        while not fixture.finalizado():
            r = len(fixture.robots_en_juego())
            ronda = fixture.generar_ronda(r <= 11)
            for encuentro in ronda.encuentros:
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                    fixture.gano(rwin, nronda=ronda.numero, nencuentro=encuentro.numero)
                rwin = encuentro.ganador()
                rlose = encuentro.robot_2 if encuentro.robot_1 == rwin else encuentro.robot_1
                s = encuentro.score(rwin)
                swin = [s for s in scores if s[0] == rwin].pop()
                slose = [s for s in scores if s[0] == rlose].pop()
                scores[scores.index(swin)] = [swin[0], swin[1] + 1, swin[2] + 1, swin[3], swin[4], swin[5] + s[0], swin[6] + s[1], swin[7] + s[0] - s[1], swin[8] + 3]
                scores[scores.index(slose)] = [slose[0], slose[1] + 1, slose[2], slose[3], slose[4] + 1, slose[5] + s[1], slose[6] + s[0], slose[7] + s[1] - s[0], slose[8]]
        if ronda is not None and ronda.tct:
            self.assertEqual(ronda.ganador(), fixture.ganador())
        else:
            scores = sorted(scores, key=lambda t: t[8], reverse=True)
            self.assertEqual(scores[0][0], fixture.ganador())
        for robot in fixture.robots:
            score = [s for s in scores if s[0] == robot].pop()
            self.assertEqual(tuple(score[1:]), fixture.score(robot))
        
if __name__ == '__main__':
    unittest.main()