from zooAnimales.animal import Animal

class Anfibio(Animal):

    cantidadAnfibios=0
    ranas=0
    salamandras=0
    listado=[]

    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorPiel=None,venenoso=False):
        super().__init__(nombre,edad,habitat,genero)
        self.colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio.cantidadAnfibios+=1



    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def movimiento():
        return "saltar"
    

