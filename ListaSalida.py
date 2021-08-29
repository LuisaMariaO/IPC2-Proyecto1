from TerrenoSalida import TerrenoSalida

class ListaSalida():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def crearTerreno(self,nombre, dimensionx, dimensiony, iniciox, inicioy, finx, finy, combustible): 
            nuevo = TerrenoSalida(nombre, dimensionx, dimensiony, iniciox, inicioy, finx, finy, combustible) 
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

    def setCombustible(self,nombre,combustible):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == nombre:
                tmp.combustible=combustible
                return tmp
            tmp = tmp.siguiente
        return None

    def Archivo(self,ruta):
        archivo=open(ruta,'w')
        aux = self.primero
       
        body=''
        body+='<terrenos>\n'
        while aux is not None:
            
            body+='\t<terreno nombre="'+aux.nombre+'">\n'
            body+='\t\t<dimension>\n'
            body+='\t\t\t<m>'+aux.dimensionx+'</m>\n'
            body+='\t\t\t<n>'+aux.dimensiony+'</n>\n'
            body+='\t\t</dimension>\n'
            body+='\t\t<posicioninicio>\n'
            body+='\t\t\t<x>'+aux.iniciox+'</x>\n'
            body+='\t\t\t<y>'+aux.inicioy+'</y>\n'
            body+='\t\t</posicioninicio>\n'
            body+='\t\t<posicionfin>\n'
            body+='\t\t\t<x>'+aux.finx+'</x>\n'
            body+='\t\t\t<y>'+aux.finy+'</y>\n'
            body+='\t\t</posicionfin>\n'
            body+='\t\t<combustible>'+str(aux.combustible)+'</combustible>\n'
            body+=aux.lista_posiciones.Escribir()
            body+='\t</terreno>\n'
            aux = aux.siguiente
        body+='</terrenos>'
        archivo.write(body)
        print("¡Archivo generado con éxito!")
        
        