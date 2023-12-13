from pygame.locals import *
from class_Nivel_uno import Nivel_Uno
from class_Nivel_dos import Nivel_Dos
from class_Nivel_tres import Nivel_Tres

class Manejador_niveles:
    def __init__(self, pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno" : Nivel_Uno, "nivel_dos" : Nivel_Dos, "nivel_tres" : Nivel_Tres}


    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
