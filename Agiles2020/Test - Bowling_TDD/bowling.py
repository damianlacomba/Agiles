#1 probar el juego perfecto
    #2 probar todos 1
class Juego(object):

    def __init__(self):
        self.tiradas = []

    def tirar(self, pinos):
        self.tiradas.append(pinos)

    def tot_puntos(self):
        puntos=0 
        ini=0
        for i in range(10):
            if self.tiradas[ini] == 10:
                puntos += 10 + self.tiradas[ini + 1]+  self.tiradas[ini + 2]
                ini += 1
            else:
                puntos += self.tiradas[ini] + self.tiradas[ini + 1]
                ini = ini + 2
        return puntos
        
#okaa ahora hay que probar unos