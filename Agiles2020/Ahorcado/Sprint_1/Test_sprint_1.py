import unittest

from sprint_1 import Juego


class AhorcadoTest(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()

    def test_letras_correctas(self):
        self.assertEqual("ganador", self.juego.jugar())

   
