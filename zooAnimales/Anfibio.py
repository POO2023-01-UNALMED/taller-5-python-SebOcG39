from gestion.Zona import Zona
from .Animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self,  nombre=None, edad=0, habitat=None, genero=None, colorPiel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, None, genero)
        rana._colorPiel = "rojo"
        rana._venenoso = True
        rana.super()._habitat = "selva"
        cls.ranas += 1
        cls._listado.append(rana)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, None, genero)
        salamandra._colorPiel = "negro y amarillo"
        salamandra._venenoso = False
        salamandra.super()._habitat = "selva"
        cls.salamandras += 1
        cls._listado.append(salamandra)

    def setColorPiel(self, color):
        self._colorPiel = color

    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def getVenenoso(self):
        return self._venenoso

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado