from zooAnimales.animal import Animal

class Pez(Animal):

    cantidadPeces=0
    listado=[]
    salmones=0
    bacalaos=0
    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorEscamas=None,cantidadAletas=0,):
        super().__init__(nombre,edad,habitat,genero)
        self.colorEscamas=colorEscamas
        self.cantidadAletas=cantidadAletas
        Pez.cantidadPeces+=1

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def movimiento():
        return "nadar"
