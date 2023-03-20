from gestion.Zona import Zona
from .Animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__(self,  nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, cantidadAletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, None, genero)
        salmon._colorEscamas = "rojo"
        salmon._cantidadAletas = 6
        salmon.super()._habitat = "oceano"
        cls.salmones += 1
        cls._listado.append(salmon)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, None, genero)
        bacalao._colorEscamas = "gris"
        bacalao._cantidadAletas = 6
        bacalao.super()._habitat = "oceano"
        cls.bacalaos += 1
        cls._listado.append(bacalao)

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, aletas):
        self._cantidadAletas = aletas

    def getCantidadAletas(self):
        return self._cantidadAletas

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado