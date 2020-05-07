class Juego(object):

    def __init__(self):
        self.tiradas = []

    def tirar(self, pinos):
        self.tiradas.append(pinos)

    
    def tot_puntos(self):
        puntos=0
        ini=0
        for i in range(10):
            if self.strike(ini):
                puntos += 10 + self.tiradas[ini + 1]+  self.tiradas[ini + 2]
                ini = ini + 1
            elif self.spare(ini):
                puntos += 10 + self.tiradas[ini + 2]
                ini= ini + 2
            else:
                puntos += self.tiradas[ini] + self.tiradas[ini + 1]
                ini= ini + 2
        return puntos

    
    def spare(self, tirada_ini):
        return self.tiradas[tirada_ini] + self.tiradas[tirada_ini+1] == 10

    def strike(self, tirada_ini):
        return self.tiradas[tirada_ini] == 10   
    

