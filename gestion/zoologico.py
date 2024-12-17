

class Zoologico():
    

    def __init__(self,nombre=None,ubicacion=None,zona=[]):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.zona=zona

    def agregarZonas(self,zona):
        self.zona.append(zona)

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self.zona:
            totalAnimales += zona.cantidadAnimales()
        return totalAnimales
    
    def getNombre(self):
        return self.nombre
    def getUbicacion(self):
        return self.nombre
    def getZona(self):
        return self.zona
    
    def setNombre(self,nombre):
        self.nombre=nombre
    def setUbicacion(self,ubicacion):
        self.ubicacion=ubicacion
    def setZona(self,zona):
        self.zona=zona






