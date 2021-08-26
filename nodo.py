from Etiqueta import Etiqueta
class Nodo():
    def __init__(self,x,y,combustible):
        self.x = x
        self.y = y
        self.combustible = combustible
        self.siguiente = None
        self.anterior = None
        self.etiqueta=Etiqueta(0,None,0,False)

        