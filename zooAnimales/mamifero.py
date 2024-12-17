from zooAnimales.animal import Animal


class Mamifero(Animal):

    cantidadMamiferos=0
    listado=[]
    caballos=0
    leones=0
    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,pelaje=False,patas=0,):
        super().__init__(nombre,edad,habitat,genero)
        self.pelaje=pelaje
        self.patas=patas
        Mamifero.cantidadMamiferos+=1

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        M=Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos+=1
                
        return M
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        M=Mamifero(nombre,edad,"selva",genero,True,4)
        cls.caballos+=1
                
        return M