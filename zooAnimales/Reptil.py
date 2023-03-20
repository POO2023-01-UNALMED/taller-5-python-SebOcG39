from gestion.Zona import Zona
from .Animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self,  nombre=None, edad=0, habitat=None, genero=None, colorEscamas=None, largoCola=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, None, genero)
        iguana._colorEscamas = "verde"
        iguana._largoCola = 3
        iguana.super()._habitat = "humedal"
        cls.iguanas += 1
        cls._listado.append(iguana)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, None, genero)
        serpiente._colorEscamas = "blanco"
        serpiente._largoCola = 1
        serpiente.super()._habitat = "jungla"
        cls.serpientes += 1
        cls._listado.append(serpiente)

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo

    def getLargoCola(self):
        return self._largoCola

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, listado):
        cls._listado = listado