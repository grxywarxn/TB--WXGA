from configuraciones import *

class Piso:
    def __init__(self, imagen, pos_x, pos_y, tamaño):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen, (tamaño[0], tamaño[1]))
        self.rect = self.imagen.get_rect()
        self.rect_principal = self.rect
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.rectangulos = obtener_rectangulos(self.rect)

    # @staticmethod
    # def crear_piso(imagen, pantalla):
    #     pisos = []
    #     piso = Piso(imagen, 0, pantalla.get_height() - 50, (1920, 50))
    #     pisos.append(piso)

        # return pisos
    
    def actualizar(self, pantalla):
        pantalla.blit(self.imagen, (self.rect_principal.x, self.rect_principal.y))