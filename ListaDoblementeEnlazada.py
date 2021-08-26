from nodo import Nodo
from Etiqueta import Etiqueta
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


    def setEtiqueta(self, x,y,acumulado, anterior, iteraciones):
        tmp = self.primero
        while tmp is not None:
            if tmp.x==x and tmp.y==y:
                tmp.etiqueta.acumulado=acumulado
                tmp.etiqueta.anterior=anterior
                tmp.etiqueta.iteraciones=iteraciones
                return None
            tmp = tmp.siguiente
        return None

    def setTerminal(self,x,y):
        tmp = self.primero
        while tmp is not None:
            if tmp.x==x and tmp.y==y:
                tmp.etiqueta.terminal=True
                return tmp
            tmp=tmp.siguiente
        return None

    def retornarMenor(self,menor):
        
        actual=self.primero
        nodoactual=menor
        while actual is not None:
            if nodoactual.etiqueta.terminal and not actual.etiqueta.terminal and actual.etiqueta.acumulado!=0:
                nodoactual=actual
            else:
                if not actual.etiqueta.terminal and actual.etiqueta.acumulado!=0:
                    if int(actual.etiqueta.acumulado)<int(nodoactual.etiqueta.acumulado):
                        nodoactual=actual
            
            actual=actual.siguiente
        nodoactual.etiqueta.terminal=True
   
        return nodoactual

    def imprimirCamino(self):
        actual=self.ultimo
        while actual.etiqueta.anterior:
            print(actual.etiqueta.anterior.x," ",actual.etiqueta.anterior.y)
        actual=actual.anterior


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