from NodoSalida import NodoSalida
class ListaPosicionesSalida:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    def vacia(self):
         return self.primero == None 
    
    def agregar(self, x, y, combustible):
        if self.vacia():
            self.primero = self.ultimo = NodoSalida(x, y, combustible)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoSalida(x, y, combustible)
            self.ultimo.anterior = aux
            
        self.size+=1

    def agregarFinal(self, x, y, combustible):
        if self.vacia():
            self.ultimo=self.primero=NodoSalida(x,y,combustible)
        else:
            aux=self.primero
            self.primero=aux.anterior=NodoSalida(x,y,combustible)
            self.primero.siguiente=aux
        self.size+=1



    def imprimir(self):
        aux = self.primero
        while aux:
            print("x= "+str(aux.x)+" y= "+str(aux.y)+" Combustible= "+str(aux.combustible))
            aux = aux.siguiente
    
    def getCoordenada(self,x,y):
        tmp = self.primero
        while tmp is not None:
            if tmp.x==x and tmp.y==y:
                return tmp
            tmp = tmp.siguiente
        return None

    def Escribir(self):
        body=''
        aux = self.primero
        while aux:
            body+='\t\t<posicion x="'+aux.x+'" y="'+aux.y+'">'+str(aux.combustible)+'</posicion>\n'
            aux = aux.siguiente
        return body
    
    