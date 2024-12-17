

class Animal():
    totalAnimales=0
    def __init__ (self,nombre=None,edad=None,habitat=None,genero=None,zona=None):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=zona
    
    def movimiento():
        return "desplazarse"
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre


    
