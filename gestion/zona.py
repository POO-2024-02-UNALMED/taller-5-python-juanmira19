class Zona():

    def __init__(self,nombre=None,zoo=None,animales=[]):
        self.nombre=nombre
        self.zoo=zoo
        self.animales=animales

    def agregarAnimales(self,animal):
        self.animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self.animales)
    
    def getNombre(self):
        return self.nombre
    def getZoo(self):
        return self.zoo
    def getAnimales(self):
        return self.animales
    

    def setNombre(self,nombre):
        self.nombre=nombre
    def setZoo(self,zoo):
        self.zoo=zoo
    def setAnimales(self,animales):
        self.animales=animales

    

    
    
    


