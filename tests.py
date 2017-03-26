import unittest
from Robot import Robot
from Fixture import Fixture

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.robots = robots = [
            Robot("Ultron", "Los Avengers","Nick Fury"),
            Robot("Wall-e","Pixar","Sr. Disney"),
            Robot("Sony","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop","O.C.P.","Bob Morthon"),
            Robot("Terminator","Skynet","Jhon Connor"),
            Robot("R2-D2","La Republica","Obiwan Kenobi"),
            Robot("3-CPO","La Republica","Anakin Skywalker"),
            Robot("BB-8","La Republica","Poe Dameron")
        ]
        self.fixture = Fixture(self.robots)

    def test_rondas(self):
        for i in range(1000):
            key = self.fixture.ronda()
            robots = set()
            for e in self.fixture.encuentros(key):
                robots.add(e.robot_1)
                robots.add(e.robot_2)
            self.assertEqual(set(self.robots), robots)
            self.fixture.limpiar()


if __name__ == '__main__':
    unittest.main()