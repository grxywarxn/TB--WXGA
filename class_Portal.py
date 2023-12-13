import pygame
from configuraciones import *
class Portal():
    def __init__(self, animaciones, tamaño, pos_x, pos_y):
        #Animaciones y tamaños
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        #Rectangulo Principal
        self.rect_principal = animaciones["Abrir"][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        #Rectangulos
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        #Animacion actual
        self.animacion_actual = self.animaciones["Abrir"]
        self.contador_pasos = 0
        self.visible = False

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

        if self.visible and self.contador_pasos >= largo:
            self.animacion_actual = self.animaciones["Idle"]

    def actualizar(self, pantalla):
        if self.visible:
            self.animar(pantalla)