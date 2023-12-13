from configuraciones import *

class Tornado:
    def __init__(self, animaciones, tamaño, boss_rectx, boss_recty):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rect_principal = self.animaciones["Tornado"][0].get_rect()
        self.animacion_actual = self.animaciones["Tornado"]
        self.contador_pasos = 0
        self.rect_principal.x = boss_rectx
        self.rect_principal.y = boss_recty

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

    def actualizar(self, pantalla):
        self.animar(pantalla)
        self.rect_principal.x -= 10