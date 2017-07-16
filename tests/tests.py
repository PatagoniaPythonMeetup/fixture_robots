import unittest
import random
import json

from base import TestBase

from server import Robot, Fixture, Encuentro

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

class TestTorneo(TestBase):
    def test_estados(self):
        robots = self.robots[:16]
        fixture = Fixture(robots)
        self.assertEqual(fixture.iniciado(), False)
        self.assertEqual(fixture.finalizado(), False)
        self.assertEqual(fixture.compitiendo(), False)
        while not fixture.finalizado():
            ronda = fixture.generar_ronda()
            self.assertEqual(ronda.iniciado(), True)
            self.assertEqual(ronda.compitiendo(), True)
            self.assertEqual(fixture.iniciado(), True)
            self.assertEqual(fixture.compitiendo(), True)
            for encuentro in ronda.encuentros:
                self.assertEqual(encuentro.iniciado(), True)
                self.assertEqual(encuentro.compitiendo(), True)
                while not encuentro.finalizado():
                    rwin = random.choice([encuentro.robot_1, encuentro.robot_2])
                    fixture.gano(rwin, nencuentro=encuentro.numero)
                self.assertEqual(encuentro.iniciado(), False)
                self.assertEqual(encuentro.compitiendo(), False)
                self.assertEqual(encuentro.finalizado(), True)
            self.assertEqual(ronda.iniciado(), False)
            self.assertEqual(ronda.compitiendo(), False)
            self.assertEqual(fixture.compitiendo(), False)
        self.assertEqual(fixture.finalizado(), True)
        self.assertEqual(fixture.compitiendo(), False)
    
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
                    fixture.gano(rwin, nencuentro=encuentro.numero)
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
