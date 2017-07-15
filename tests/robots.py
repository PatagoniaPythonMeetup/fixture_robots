import unittest

from server import Robot
    
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