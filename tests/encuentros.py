import unittest

from server import Encuentro

class TestEncuentros(unittest.TestCase):
    def test_estado_inicial(self):
        self.assertEqual(Encuentro("r1", "r2").finalizado(), False)

    def test_r1r2r2(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, r2)
        self.assertEqual(e1.iniciado(), True)
        self.assertEqual(e1.compitiendo(), False)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.iniciado(), True)
        self.assertEqual(e1.compitiendo(), True)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r2)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r2)
        self.assertEqual(e1.iniciado(), False)
        self.assertEqual(e1.compitiendo(), False)
        self.assertEqual(e1.finalizado(), True)

    def test_r1r1(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, r2)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), True)
    
    def test_custom(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, r2)
        e1.JUGADAS = 5
        self.assertEqual(e1.finalizado(), False)
        self.assertEqual(e1.iniciado(), True)
        self.assertEqual(e1.compitiendo(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), False)
        self.assertEqual(e1.iniciado(), True)
        self.assertEqual(e1.compitiendo(), True)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), True)

    def test_none(self):
        r1 = "robot 1"
        r2 = "robot 2"
        e1 = Encuentro(r1, None)
        e1.JUGADAS = 5
        self.assertEqual(e1.iniciado(), False)
        e1.agregar_adversario(r2)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), False)
        self.assertEqual(e1.iniciado(), True)
        self.assertEqual(e1.compitiendo(), True)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), False)
        e1.agregar_ganador(r1)
        self.assertEqual(e1.finalizado(), True)
    