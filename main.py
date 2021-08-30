
from os import system,startfile
from ListaSimpleEnlazada import ListaSimple
from ListaSalida import ListaSalida
import xml.etree.ElementTree as ET


def carga(ruta, terrenos):
     
    try:
        
        tree = ET.parse(ruta)
        root = tree.getroot()
        for terreno in root:
            nombre=terreno.attrib['nombre']
            
                #Busca las dimensiones del terreno
            for dimension in terreno.iter('m'):
                m=dimension.text
            
            for dimension in terreno.iter('n'):
                n=dimension.text
            #Busca la posición de inicio del terreno    
            for posicioni in terreno.iter('posicioninicio'):
                for x in posicioni.iter('x'):
                    iniciox=x.text
                for y in posicioni.iter('y'):
                    inicioy=y.text   
            #Busca la posicion de fin del terreno        
            for posicionf in terreno.iter('posicionfin'):
                for x in posicionf.iter('x'):
                    finx=x.text
                for y in posicionf.iter('y'):
                    finy=y.text  
            if int(m)<=100 and int(n)<=100:
                terrenos.crearTerreno(nombre, m, n, iniciox, inicioy, finx, finy)
                print("Se ha guardado la información del mapa: "+nombre )
                for posicion in terreno.iter('posicion'):
                    mapa= terrenos.getTerreno(nombre)
                    mapa.lista_posiciones.agregar(posicion.attrib['x'], posicion.attrib['y'], posicion.text)
            else:
                print("No se cargó el terreno "+nombre+": Las dimensiones sobrepasan el límite de 100x100")
            
            
        print("¡Archivo cargado con éxito!\n")
        
    except:
        print("Ha ocurrido un error")

def proceso(terrenos, terrenosalida):  
    print("-------------Proceso de terrenos-------------")
    print("Terrenos disponibles en el sistema:")
    terrenos.imprimirTerreno()
    busqueda=input("Ingrese el nombre del mapa a procesar: ")
    terreno=terrenos.getTerreno(busqueda)
    
    if terreno is None:
        print("Terreno no encontrado")
    else:
        if terreno.procesado:
            print("Error: "+terreno.nombre+" ya ha sido procesado")
        else:

            terreno=terrenos.setProcesado(terreno.nombre)
            #terreno.lista_posiciones.imprimir()
            print("Procesando: ",terreno.nombre)
            print("Obteniendo dimensiones del terreno: ",terreno.dimensionx,"x",terreno.dimensiony)
            print("Obteniendo coordenada inicial: (",terreno.iniciox,",",terreno.inicioy,")")
            xinicial=terreno.iniciox
            yinicial=terreno.inicioy
            print("Obteniendo coordenada final: (",terreno.finx,",",terreno.finy,")")
            xfinal=terreno.finx
            yfinal=terreno.finy
            print("Obteniendo la distancia...")
            distanciax=abs(int(terreno.finx)-int(terreno.iniciox))
            distanciay=abs(int(terreno.finy)-int(terreno.inicioy))
            
            
            #Tomando posición inical
            actual=terreno.lista_posiciones.getInicio(xinicial,yinicial)
            
            actual.etiqueta.acumulado=actual.combustible
            actual.etiqueta.anterior=None
            actual.etiqueta.iteraciones=0
            actual.etiqueta.terminal=True

            #Tomo el nodo final
            final=terreno.lista_posiciones.searchCoordenada(xfinal,yfinal)

            #Agregando el terreno a la lista de salida
            terrenosalida.crearTerreno(terreno.nombre, terreno.dimensionx, terreno.dimensiony, terreno.iniciox, terreno.inicioy, terreno.finx, terreno.finy,0)
            #Agregando la posición inical a la lista de salida
            mapafinal= terrenosalida.getTerreno(terreno.nombre)
            
            combustible=0
            iteraciones=0
            while not final.etiqueta.terminal:
                iteraciones+=1
                #Obteniendo los nodos adyacentes
                arriba=terreno.lista_posiciones.searchCoordenada(str(int(actual.x)-1),actual.y)
                abajo=terreno.lista_posiciones.searchCoordenada(str(int(actual.x)+1),actual.y)
                derecha=terreno.lista_posiciones.searchCoordenada(actual.x,str(int(actual.y)+1))
                izquierda=terreno.lista_posiciones.searchCoordenada(actual.x,str(int(actual.y)-1))

                #Etiquetando
                if arriba!=None and not arriba.etiqueta.terminal:
                    tmp_arriba_acumulado=0
                    acumulado=0
                    if arriba.etiqueta.acumulado==0:
                        acumulado=int(actual.etiqueta.acumulado)+int(arriba.combustible) 
                        terreno.lista_posiciones.setEtiqueta(arriba.x, arriba.y, acumulado, actual, iteraciones)
                        
                    else:
                        tmp_arriba_acumulado=int(actual.etiqueta.acumulado)+int(arriba.combustible) 

                        if int(tmp_arriba_acumulado)<int(arriba.etiqueta.acumulado):
                            terreno.lista_posiciones.setEtiqueta(str(arriba.x), str(arriba.y), tmp_arriba_acumulado, actual, iteraciones)


                        
                if abajo!=None and not abajo.etiqueta.terminal:
                    acumulado=0
                    tmp_abajo_acumulado=0
                    if abajo.etiqueta.acumulado==0:
                        acumulado=int(actual.etiqueta.acumulado)+int(abajo.combustible)
                        terreno.lista_posiciones.setEtiqueta(str(abajo.x), str(abajo.y), acumulado, actual, iteraciones)
                    else:
                        tmp_abajo_acumulado=int(actual.etiqueta.acumulado)+int(abajo.combustible) 
                    
                        if int(tmp_abajo_acumulado)<int(abajo.etiqueta.acumulado) and tmp_abajo_acumulado!=0:
                            terreno.lista_posiciones.setEtiqueta(str(abajo.x), str(abajo.y), tmp_abajo_acumulado, actual, iteraciones)

            
                if derecha!=None and not derecha.etiqueta.terminal :
                    acumulado=0
                    tmp_derecha_acumulado=0
                    if derecha.etiqueta.acumulado==0:
                        acumulado=int(actual.etiqueta.acumulado)+int(derecha.combustible) 
                        terreno.lista_posiciones.setEtiqueta(str(derecha.x), str(derecha.y), acumulado, actual, iteraciones)
                    else:                    
                        tmp_derecha_acumulado=int(actual.etiqueta.acumulado)+int(derecha.combustible)

                        if int(tmp_derecha_acumulado)<int(derecha.etiqueta.acumulado) and tmp_derecha_acumulado!=0:
                            terreno.lista_posiciones.setEtiqueta(str(derecha.x), str(derecha.y), tmp_derecha_acumulado, actual, iteraciones)

                if izquierda!=None and not izquierda.etiqueta.terminal :
                    acumulado=0
                    tmp_izquierda_acumulado=0
                    if izquierda.etiqueta.acumulado==0:
                        acumulado=int(actual.etiqueta.acumulado)+int(izquierda.combustible) 
                        terreno.lista_posiciones.setEtiqueta(str(izquierda.x), str(izquierda.y), acumulado, actual, iteraciones)
                    else:                    
                        tmp_izquierda_acumulado=int(actual.etiqueta.acumulado)+int(izquierda.combustible)

                        if int(tmp_izquierda_acumulado)<int(izquierda.etiqueta.acumulado) and tmp_izquierda_acumulado!=0:
                            terreno.lista_posiciones.setEtiqueta(str(izquierda.x), str(izquierda.y), tmp_izquierda_acumulado, actual, iteraciones)
                menor=terreno.lista_posiciones.retornarMenor(actual)

                actual=menor
                #actual=terreno.lista_posiciones.setTerminal(actual.x, actual.y)
                
                if(actual.x==final.x and actual.y==final.y and actual.etiqueta.terminal):
                    combustible=actual.etiqueta.acumulado
                    break
                
                combustible=actual.etiqueta.acumulado
                
            mapafinal= terrenosalida.setCombustible(terreno.nombre,combustible)    
            final=terreno.lista_posiciones.searchCoordenada(xfinal,yfinal)  
            
            
            nodocamino=final
            while nodocamino is not None:
                mapafinal.lista_posiciones.agregarFinal(nodocamino.x, nodocamino.y, nodocamino.combustible)
                nodocamino=nodocamino.etiqueta.anterior 

            filas= int(terreno.dimensionx)
            columnas= int(terreno.dimensiony)

            columnaactual=1
            filaactual=1
            actual=mapafinal.lista_posiciones.getCoordenada(str(filaactual),str(columnaactual))
            while columnaactual<=columnas and filaactual<=filas :
                    if actual!=None:
                        if columnaactual==columnas:
                            columnaactual=1
                            filaactual+=1
                            print("|1|",end="")
                            print("")
                        else:
                            print("|1",end="")
                            columnaactual+=1
                        
                        
                    else:
                        if columnaactual==columnas:
                            columnaactual=1
                            filaactual+=1
                            print("|0|",end="")
                            print("")
                        
                        else:
                            print("|0",end="")
                            columnaactual+=1
                    actual=mapafinal.lista_posiciones.getCoordenada(str(filaactual),str(columnaactual))
            print("Consumo de combustible calculado: ", combustible)
        
                    
                    
def salida(terrenosalida):
    try:
        print("-------------Generador de archivos de salida-------------")
        print("Terrenos procesados en el sistema:")
        terrenosalida.imprimirTerreno()
        ruta=input("Escribir una ruta específica: ")
        terrenosalida.Archivo(ruta)
    except:
        print("Ha ocurrido un error, intente nuevamente\n")
    
                  
                    
                    
                
                

        
        
        
        
        
        
def grafica(terrenos):
    try:
        print("-------------Graficadora-------------")
        
        busqueda=input("Ingrese el nombre del mapa a graficar: ")
        terreno=terrenos.getTerreno(busqueda)
        if terreno is None:
            print("Terreno no encontrado")
        else:
            graphviz="""
        digraph L{
        node[shape=circle fillcolor=cadetblue3 style =filled]
        
        subgraph cluster_p{\n"""
            graphviz+='\t\tlabel="'+terreno.nombre+'\nDimensiones: '+terreno.dimensionx+'x'+terreno.dimensiony+'"\n'
            graphviz+="""\t\tbgcolor = brown3
            edge[dir = "none"]\n"""
            
        graphviz+=terreno.lista_posiciones.graficar(terreno.dimensionx, terreno.dimensiony)   
        graphviz+="}\n}"
        graph= open('mapa'+terreno.nombre+'.dot','w')
        graph.write(graphviz)
        graph.close()
        
        system('dot -Tpng mapa'+terreno.nombre+'.dot -o Mapa_'+terreno.nombre+'.png')
        system('Mapa_'+terreno.nombre+'.png')
        print("¡Gráfica generada con éxito")
    except:
        print("Ha ocurrido un error, intente nuevamente\n")
      
def menu():
    #lista_nodos=ListaDoble()
    lista_terrenos=ListaSimple()
    lista_salida=ListaSalida()
    while True:
        print("\nAgencia Guatemalteca de Investigación Espacial")
        print("Monitoreo de r2r2 \n")
        print("Menú principal:")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salir del sistema")
        option=input("Seleccione una opción: ")
        if option=="1":
            filename=input("Ingrese la ruta del archivo: ")
            carga(filename, lista_terrenos)
            
        elif option=="2":
            print("Procesando archivo...\n")
            proceso(lista_terrenos, lista_salida)
            
        elif option=="3":
            salida(lista_salida)
        elif option=="4":
            print("\n->Luisa María Ortíz Romero")
            print("->202003381")
            print('->Introducción a la Programación y Computación 2 sección "D"')
            print("->Ingeniería en Ciencias y Sistemas")
            print("->4to Semestre\n")
            print("___________________________________________________________________")
        elif option=="5":
            print("-----Terrenos disponibles-----","Total:",lista_terrenos.size)
            lista_terrenos.imprimirTerreno()
            grafica(lista_terrenos)
        elif option=="6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inexistente")

menu()