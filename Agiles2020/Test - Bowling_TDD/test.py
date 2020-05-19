import unittest

from bowling import Juego


class JuegoTest(unittest.TestCase):

    def setUp(self):
        self.juego = Juego()

    def test_perdedor(self):
            self.cant_tiradas(0,20)
            self.assertEqual(0, self.juego.tot_puntos())

    def test_juego_perfecto(self):
            self.cant_tiradas(10,12)
            self.assertEqual(300,self.juego.tot_puntos())

    def test_todos_uno(self):
        self.cant_tiradas(1,20)
        self.assertEqual(20,self.juego.tot_puntos())

    def test_un_strike(self):
        self.juego.tirar(3)
        self.juego.tirar(4)
        self.juego.tirar(10)
        self.cant_tiradas(0,16)
        self.assertEqual(18,self.juego.tot_puntos())






 

    def cant_tiradas(self, pinos,tiradas):
        for i in range(tiradas):
            self.juego.tirar(pinos)
 