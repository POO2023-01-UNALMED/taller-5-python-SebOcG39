from gestion.Zona import Zona
from .Animal import Animal

class Ave(Animal):
    _listado = []
    aguilas = 0
    halcones = 0
    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPLumas = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, None, genero)
        halcon._colorPLumas = "cafe glorioso"
        halcon.super()._habitat = "montana"
        cls.halcones += 1
        cls._listado.append(halcon)

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, None, genero)
        aguila._colorPLumas = "blanco y amarillo"
        aguila.super()._habitat = "montana"
        cls.aguilas += 1
        cls._listado.append(aguila)

    
    def setColorPlumas(self, color):
        self._colorPLumas = color

    def getColorPlumas(self):
        return self._colorPLumas
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado