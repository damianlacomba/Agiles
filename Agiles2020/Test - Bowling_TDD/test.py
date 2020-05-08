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
            self.assertEqual(300, self.juego.tot_puntos())

    def test_pruba(self):
            self.juego.tirar(10) 
            self.juego.tirar(4) 
            self.juego.tirar(3) 
            self.juego.tirar(10) 
            self.cant_tiradas(0,14)
            """ ej = [[1,4],[4,5],[6,4],[5,5],[10],[0,1],[7,3],[6,4],[10],[2,8,6]]
            for pinos in ej:
                self.juego.tirar(pinos)"""
            self.assertEqual(6, self.juego.tot_puntos())
            #[[10],[3,4],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
            #[[3,4],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
            #[[10],[3,4],[10],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    

    def cant_tiradas(self, pinos,tiradas):
        for i in range(tiradas):
            self.juego.tirar(pinos)
 