import pygame
from configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self, imagen, pos_x, pos_y, tamaño:tuple):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen, (tamaño[0], tamaño[1]))
        self.rect = self.imagen.get_rect()
        self.rect_principal = self.rect
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.rectangulos = obtener_rectangulos(self.rect_principal)

    def actualizar(self, pantalla):
        pantalla.blit(self.imagen, (self.rect_principal.x, self.rect_principal.y))
