import pygame
from configuraciones import *
from class_Plataforma import Plataforma

class Plataforma_movil(Plataforma):
    def __init__(self, imagen, pos_x, pos_y, tamaño, cc_inicial, cc_final, direccion_mov):
        super().__init__(imagen, pos_x, pos_y, tamaño)
        self.movil = True
        self.velocidad = 5
        self.cc_inicial = cc_inicial
        self.cc_final = cc_final
        self.direccion = direccion_mov

    def actualizar(self, pantalla):
        pantalla.blit(self.imagen, (self.rect_principal.x, self.rect_principal.y))
    
    def mover_plataforma(self):
        if self.movil:
            if self.direccion == "x":
                self.rect_principal.x += self.velocidad

                if self.rect_principal.x >= self.cc_final:
                    self.rect_principal.x = self.cc_final
                    self.velocidad *= -1  
                elif self.rect_principal.x <= self.cc_inicial:
                    self.rect_principal.x = self.cc_inicial
                    self.velocidad *= -1  

                self.rectangulos = obtener_rectangulos(self.rect_principal)
            elif self.direccion == "y":
                self.rect_principal.y += self.velocidad

                if self.rect_principal.y <= self.cc_inicial:
                    self.rect_principal.y = self.cc_inicial
                    self.rect_principal.top
                    self.velocidad *= -1  
                elif self.rect_principal.y >= self.cc_final:
                    self.rect_principal.y = self.cc_final
                    self.rect_principal.top
                    self.velocidad *= -1
                self.rectangulos = obtener_rectangulos(self.rect_principal)

    # @staticmethod
    # def crear_plataformas_moviles_n1(imagen):
    #     plataformas_moviles = []
    #     plataformas_moviles.append(Plataforma_movil(imagen, 800, 600, (250, 35), 600, 800, "y"))
    #     # plataformas_moviles.append(Plataforma_movil(imagen, 570, 100, (100, 25), 470, 670, "x"))#, 470, 670, "x"

    #     return plataformas_moviles
    
    # def crear_plataformas_moviles_n2(imagen):
    #     plataformas_moviles = []
    #     plataformas_moviles.append(Plataforma_movil(imagen, 700, 600, (250, 35), 600, 1200, "x"))
    #     return plataformas_moviles