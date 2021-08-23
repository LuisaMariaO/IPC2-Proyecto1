from TerrenoSalida import TerrenoSalida

class ListaSalida():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def crearTerreno(self,nombre, dimensionx, dimensiony, iniciox, inicioy, finx, finy): 
            nuevo = TerrenoSalida(nombre, dimensionx, dimensiony, iniciox, inicioy, finx, finy) 
            self.size += 1
            if self.primero is None:
                self.primero = nuevo
            else:
                aux = self.primero
                while aux.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente = nuevo

    def imprimirTerreno(self):
        aux = self.primero
        while aux is not None:
            print(aux.nombre)
            aux = aux.siguiente
    
    def getTerreno(self, nombre):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente
        return None