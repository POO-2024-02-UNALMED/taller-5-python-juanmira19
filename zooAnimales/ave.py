from zooAnimales.animal import Animal

class Ave(Animal):

    cantidadAves=0
    listado=[]
    halcones=0
    aguilas=0
    

    def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorPlumas=None):
        super().__init__(nombre,edad,habitat,genero)
        self.colorPlumas=colorPlumas
        Ave.cantidadAves+=1

        

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        M=Ave(nombre,edad,"montañas",genero,"cafe glorioso")
        cls.halcones+=1
                
        return M
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        M=Ave(nombre,edad,"montañas",genero,"blanco y amarillo")
        cls.aguilas+=1
                
        return M
    
