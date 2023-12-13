from configuraciones import *

class Enemigo():
    def __init__(self, animaciones, pos_x, pos_y, tamaño, movil=False, cc_inicial=None, cc_final = None, velocidad=7):
        #Animaciones y tamaños
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        #Rectangulo Principal
        self.rect_principal = animaciones["Idle_r"][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        #Rectangulos 
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        #Animacion actual
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Idle_r"]
        #Direccion
        self.movil = movil
        self.velocidad = velocidad
        self.direccion = "Derecha"
        self.cc_inicial = cc_inicial
        self.cc_final = cc_final
        #Vida
        self.vidas = 1
        self.esta_muerto = False
        self.esta_muriendo = False
        #Sonidos
        pygame.mixer.init()
        self.sonido_recibir_daño = pygame.mixer.Sound(r"Sonidos\nomu_recibir_daño.wav")
        self.sonido_recibir_daño.set_volume(0.1)

        self.sonido_recibir_disparo = pygame.mixer.Sound(r"Sonidos\nomu_death.wav")
        self.sonido_recibir_disparo.set_volume(0.1)



    def actualizar(self, pantalla):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.mover_en_x(pantalla)
    
    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

    def actualizar_animaciones(self):
        if self.direccion == "Derecha":
            self.animacion_actual = self.animaciones["Walk_r"]
            if self.esta_muriendo:
                self.rectangulos = obtener_rectangulos(self.rect_principal)
                self.animacion_actual = self.animaciones["Fall_down_r"]
        elif self.direccion == "Izquierda":
            self.animacion_actual = self.animaciones["Walk_l"]
            if self.esta_muriendo:
                self.rectangulos = obtener_rectangulos(self.rect_principal)
                self.animacion_actual = self.animaciones["Fall_down_l"]


    def mover_en_x(self, pantalla):
        self.actualizar_animaciones()
        if self.esta_muerto == False:
            if self.direccion == "Derecha":
                if self.rect_principal.x >= self.cc_final:
                    self.rect_principal.x = self.cc_final
                    self.velocidad *= -1
                    self.direccion = "Izquierda"
            elif self.rect_principal.x <= self.cc_inicial:
                self.rect_principal.x = self.cc_inicial
                self.velocidad *= -1
                self.direccion = "Derecha"
            self.animar(pantalla)
        
        self.rect_principal.x += self.velocidad
        self.rectangulos = obtener_rectangulos(self.rect_principal)
