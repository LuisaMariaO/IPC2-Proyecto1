from nodo import Nodo
class ListaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
        
    def vacia(self):
         return self.primero == None 
    
    def agregar(self, x, y, combustible):
        if self.vacia():
            self.primero = self.ultimo = Nodo(x, y, combustible)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(x, y, combustible)
            self.ultimo.anterior = aux
            
        self.size+=1
        

    def imprimir(self):
        aux = self.primero
        while aux:
            print("x= "+str(aux.x)+" y= "+str(aux.y)+" Combustible= "+str(aux.combustible))
            aux = aux.siguiente
    
    def getInicio(self,x,y):
        tmp = self.primero
        while tmp is not None:
            if tmp.x==x and tmp.y==y:
                return tmp
            tmp = tmp.siguiente
        return None

    def searchCoordenada(self,x,y):
        tmp = self.primero
        while tmp is not None:
            if tmp.x==x and tmp.y==y:
                return tmp
            tmp= tmp.siguiente
        return None