from ListaPosicionesSalida import ListaPosicionesSalida
class TerrenoSalida:
     def __init__(self, nombre, dimensionx, dimensiony, iniciox, inicioy, finx, finy,combustible):
        self.nombre = nombre
        self.dimensionx = dimensionx
        self.dimensiony = dimensiony
        self.iniciox = iniciox
        self.inicioy = inicioy
        self.finx = finx
        self.finy = finy
        self.combustible=combustible
        self.lista_posiciones = ListaPosicionesSalida()
        self.siguiente = None
