from gestion.zona import Zona
from .animal import Animal

class Mamifero(Animal):
    leones = 0
    caballos = 0
    _listado = []

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, pelaje=False, patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, None, genero)
        caballo._patas = 4
        caballo._pelaje = True
        caballo.super()._habitat = "pradera"
        cls.caballos += 1
        cls._listado.append(caballo)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, None, genero)
        leon._patas = 4
        leon._pelaje = True
        leon.super()._habitat = "selva"
        cls.leones += 1
        cls._listado.append(leon)

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPelaje(self):
        return self._pelaje
    
    def setPatas(self, patas):
        self._patas = patas

    def getPatas(self):
        return self._patas
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado