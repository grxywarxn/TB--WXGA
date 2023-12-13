import pygame
import random
from configuraciones import *

class Flama():
    def __init__(self, animaciones, tamaño, velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rect_principal = self.animaciones["Flama"][0].get_rect()
        self.animacion_actual = self.animaciones["Flama"]
        self.rect_principal.x = random.randrange(0, 1366, 10)
        self.rect_principal.y = random.randrange(-100, 0, 100)
        self.velocidad = velocidad
        self.contador_pasos = 0

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

    def actualizar(self, pantalla):
        self.mover_flama()
        self.animar(pantalla)

    def mover_flama(self):
        self.rect_principal.y += self.velocidad
