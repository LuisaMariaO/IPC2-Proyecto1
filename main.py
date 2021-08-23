
from ListaSimpleEnlazada import ListaSimple
import xml.etree.ElementTree as ET


def carga(ruta, terrenos):
     
    try:
        
        tree = ET.parse(ruta)
        root = tree.getroot()
        for terreno in root:
            nombre=terreno.attrib['nombre']
            print("Se ha guardado la información del mapa: "+nombre )
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
            terrenos.crearTerreno(nombre, m, n, iniciox, inicioy, finx, finy)
           
            for posicion in terreno.iter('posicion'):
                mapa= terrenos.getTerreno(nombre)
                mapa.lista_posiciones.agregar(posicion.attrib['x'], posicion.attrib['y'], posicion.text)
            
            
        print("¡Archivo cargado con éxito!\n")
        
    except:
        print("Ha ocurrido un error")

def proceso(terrenos):  
    print("-------------Proceso de terrenos-------------")
    print("Terrenos disponibles en el sistema:")
    terrenos.imprimirTerreno()
    busqueda=input("Ingrese el nombre del mapa a procesar: ")
    terreno=terrenos.getTerreno(busqueda)
    if terreno is None:
        print("Terreno no encontrado")
    else:
        #terreno.lista_posiciones.imprimir()
        print("Procesando: ",terreno.nombre)
        print("Obteniendo dimensiones del terreno: (",terreno.dimensionx,",",terreno.dimensiony,")")
        print("Obteniendo coordenada inicial: (",terreno.iniciox,",",terreno.inicioy,")")
        xinicial=terreno.iniciox
        yinicial=terreno.inicioy
        print("Obteniendo coordenada final: (",terreno.finx,",",terreno.finy,")")
        print("Obteniendo la distancia...")
        distanciax=abs(int(terreno.finx)-int(terreno.iniciox))
        distanciay=abs(int(terreno.finy)-int(terreno.inicioy))
        
        print("Obteniendo la dirección del movimiento...")
        if terreno.iniciox<=terreno.finx:
            direccionx="derecha"
        else:
            direccionx="izquierda"
        
        if terreno.inicioy<=terreno.finy:
            direcciony="abajo"
        else:
            direcciony="arriba"
        inicio=terreno.lista_posiciones.getInicio(xinicial,yinicial)
        print(inicio.combustible)
        
def grafica(terrenos):
    print("-------------Graficadora-------------")
    busqueda=input("Ingrese el nombre del mapa a graficar: ")
    terreno=terrenos.getTerreno(busqueda)
    if terreno is None:
        print("Terreno no encontrado")
    else:
        terreno.lista_posiciones.imprimir()
      
def menu():
    #lista_nodos=ListaDoble()
    lista_terrenos=ListaSimple()
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
            proceso(lista_terrenos)
            
        elif option=="3":
            ("Escribe")
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