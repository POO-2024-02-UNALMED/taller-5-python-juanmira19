from .animal import Animal

class Reptil(Animal):

    cantidadReptiles=0
    listado=[]
    iguanas=0
    serpientes=0
    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorEscamas=None,largoCola=0,):
        super().__init__(nombre,edad,habitat,genero)
        self.colorEscamas=colorEscamas
        self.largoCola=largoCola
        Reptil.cantidadReptiles+=1

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def movimiento():
        return "reptar"
    

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        
        M=Reptil(nombre,edad,"humedal",genero,"blanco y amarillo",3)
        cls.iguanas+=1
                
        return M
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        
        M=Reptil(nombre,edad,"jungla",genero,"blanco",1)
        cls.serpientes+=1
                
        return M




