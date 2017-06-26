import unittest

from server import Grupo

from base import TestBase

class TestGrupos(TestBase):
    def test_generar_grupos(self):
        robots = self.robots[:16]
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 8)],
            [2,2,2,2,2,2,2,2])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 4)],
            [4,4,4,4])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 2)],
            [8,8])
        robots = self.robots[:19]
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 8)],
            [2,2,2,2,2,3,3,3])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 4)],
            [4,5,5,5])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 2)],
            [9,10])
        robots = self.robots[:24]
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 8)],
            [3,3,3,3,3,3,3,3])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 4)],
            [6,6,6,6])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 2)],
            [12,12])
        robots = self.robots[:23]
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 8)],
            [2,3,3,3,3,3,3,3])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 4)],
            [5,6,6,6])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 2)],
            [11,12])
        robots = self.robots[:17]
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 6)],
            [2,3,3,3,3,3])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 4)],
            [4,4,4,5])
        self.assertEqual(
            [len(g.robots) for g in Grupo.generar(robots, 8)],
            [2, 2, 2, 2, 2, 2, 2, 3])