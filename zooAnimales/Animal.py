from gestion.zona import Zona
from .mamifero import Mamifero
from .ave import Ave
from .reptil import Reptil
from .pez import Pez
from .anfibio import Anfibio

class Animal():
    _totalAnimales = 0
    def __init__(self, nombre=None, edad=0, habitat=None, genero=None, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.animalCreado(self)

    def movimiento():
        return "desplazarse"
    
    def totalPorTipo(self):
        return f'''Mamiferos: {Mamifero.cantidadMamiferos()}
        Aves: {Ave.cantidadAves()}
        Reptiles: {Reptil.cantidadReptiles()}
        Peces: {Pez.cantidadPeces()}
        Anfibios: {Anfibio.cantidadAnfibios()}
        '''

    @classmethod
    def animalCreado(cls, animal):
        cls._totalAnimales += 1
        animal._zona.agregarAnimales(animal)

    def __Str__(self):
        texto = f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}'
        if self._zona != None:
            texto += f', la zona en la que me ubico es {self._zona}, en el zoo {self._zona.getZoo}'
        return texto
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona