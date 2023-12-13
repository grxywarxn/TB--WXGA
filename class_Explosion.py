import pygame
from configuraciones import *
import random

class Explosion():
    def __init__(self, animaciones, tamaño):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rect_principal = self.animaciones["Explosion"][0].get_rect()
        self.animacion_actual = self.animaciones["Explosion"]
        self.contador_pasos = 0

        self.lista_coordenadas = [(71.5, 200), (214.5, 350), (357.5, 500)]
        self.coordenada_actual = random.choice(self.lista_coordenadas)
        self.rect_principal.x = self.coordenada_actual[0]
        self.rect_principal.y = self.coordenada_actual[1]
        self.animando = True

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

    def actualizar(self, pantalla):
        if self.animando:
            self.animar(pantalla)
