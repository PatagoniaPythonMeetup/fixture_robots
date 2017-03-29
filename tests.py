import unittest
import random
from Robot import Robot
from Fixture import Fixture

class TestStringMethods(unittest.TestCase):
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

    def test_robots_en_ronda(self):
        robots = self.robots[:]
        fixture = Fixture(robots)
        ronda = fixture.ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_pares_en_ronda(self):
        robots = self.robots[:]
        while len(robots) % 2 != 0:
            robots.pop()
        fixture = Fixture(robots)
        ronda = fixture.ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_impares_en_ronda(self):
        robots = self.robots[:]
        while len(robots) % 2 != 1:
            robots.pop()
        fixture = Fixture(robots)
        ronda = fixture.ronda()
        self.assertEqual(set(robots), set(ronda.robots))

    def test_robots_en_ronda_random(self):
        robots = self.robots[:]
        robots = robots[random.randint(1, len(robots)):]
        fixture = Fixture(robots)
        ronda = fixture.ronda()
        self.assertEqual(set(robots), set(ronda.robots))

if __name__ == '__main__':
    unittest.main()