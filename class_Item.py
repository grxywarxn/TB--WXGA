import pygame
from configuraciones import *

class Item:
    def __init__(self, imagen, pos_x, pos_y, tamaño, tipo, animaciones = None):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen, (tamaño[0], tamaño[1]))
        self.animaciones = animaciones
        self.rect = self.imagen.get_rect()
        self.rect_principal = self.rect
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        self.visible = True
        self.eliminado = False
        self.tipo = tipo

    def actualizar(self, pantalla):
        if self.visible:
            pantalla.blit(self.imagen, (self.rect_principal.x, self.rect_principal.y))

    def eliminar(self):
        self.visible = False
        self.eliminado = True

# #ITEMS LVL 1

# items_lvl_1 = []
# items_lvl_1.append(Item(heart, 215, 360, (20, 20), "vida"))
# items_lvl_1.append(Item(speed_boost, 800, 350, (20,30), "rayo"))
# items_lvl_1.append(Item(ice_ball, 1200, 500, (30,30), "bola_hielo"))
# items_lvl_1.append(Item(fire_ball, 800, 800, (30,30), "bola_fuego"))
# items_lvl_1.append(Item(bonus_gem, 885, 60, (30,30), "diamante")) 