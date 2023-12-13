from configuraciones import *

class Trampa:
    def __init__(self, animaciones, pos_x, pos_y, tamaño, tipo, movil=False, cc_inicial=None, cc_final = None, direccion_mov=None, velocidad=7) -> None:
        #Animaciones y tamaños
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, * tamaño)
        #Rectangulo Principal
        self.rect_principal = animaciones[tipo][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        #Rectangulos
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        #Animacion actual
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones[tipo]
        
        self.movil = movil
        self.velocidad = velocidad
        self.cc_inicial = cc_inicial
        self.cc_final = cc_final
        self.direccion = direccion_mov
    
    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

    def mover_trampa(self):
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
                    self.velocidad *= -1  
                elif self.rect_principal.y >= self.cc_final:
                    self.rect_principal.y = self.cc_final
                    self.velocidad *= -1
                self.rectangulos = obtener_rectangulos(self.rect_principal)
