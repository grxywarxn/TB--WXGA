from configuraciones import * 
from class_Disparo_enemigo import Disparo_enemigo

class Enemigo_disparo():
    def __init__(self, animaciones, pos_x, pos_y, tamaño, direccion_disparo):
        #Animaciones y tamaños
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        #Direccion
        self.direccion_disparo = direccion_disparo
        #Rectangulo Principal
        if self.direccion_disparo == "Derecha":
            self.rect_principal = animaciones["Idle_r"][0].get_rect()
        else:
            self.rect_principal = animaciones["Idle_l"][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        #Animacion actual
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Idle_r"]
        #Vida
        self.vidas = 3
        self.esta_muerto = False
        self.esta_muriendo = False
        self.timer_daño_recibido = 1500
        self.ultimo_daño_recibido = pygame.time.get_ticks()
        #Sonidos
        self.sonido_recibir_daño = pygame.mixer.Sound(r"Sonidos\nomu_recibir_daño.wav")
        self.sonido_recibir_daño.set_volume(0.1)

        self.sonido_recibir_disparo = pygame.mixer.Sound(r"Sonidos\nomu_death.wav")
        self.sonido_recibir_disparo.set_volume(0.1)

        self.sonido_disparo = pygame.mixer.Sound(r"Sonidos\nomu_disparo_oscuro.wav")
        self.sonido_disparo.set_volume(0.02)
        #Disparos
        self.lista_disparos = []
        self.flag_disparo = True
        self.tiempo_ultimo_disparo = 0
        self.disparando = False


    def actualizar(self, pantalla):
        if not self.esta_muerto:
            self.actualizar_animaciones()
            self.actualizar_disparos(pantalla)
            self.animar(pantalla)
            if self.flag_disparo:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.tiempo_ultimo_disparo >= 3000:
                    self.disparar()
                    self.tiempo_ultimo_disparo = tiempo_actual
                    self.disparando = True



    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
        self.contador_pasos += 1

        if self.esta_muriendo and self.contador_pasos == largo:
            self.esta_muerto = True

        if self.disparando and self.contador_pasos == largo:
            self.disparando = False

    def actualizar_animaciones(self):
        if self.direccion_disparo == "Derecha":
            self.animacion_actual = self.animaciones["Idle_r"]
            if self.disparando and self.direccion_disparo == "Derecha":
                self.animacion_actual = self.animaciones["Attack_r"]
        elif self.direccion_disparo == "Izquierda":
            self.animacion_actual = self.animaciones["Idle_l"]
            if self.disparando and self.direccion_disparo == "Izquierda":
                self.animacion_actual = self.animaciones["Attack_l"]
    
    def disparar(self):
        self.sonido_disparo.play()
        self.disparando = True
        x = None
        y = self.rect_principal.centery - 7
        if self.direccion_disparo == "Derecha":
            
            x = self.rect_principal.right
        elif self.direccion_disparo == "Izquierda":
            
            x = self.rect_principal.left - 40

        if x is not None:
            self.lista_disparos.append(Disparo_enemigo(x, y, self.direccion_disparo))


    def actualizar_disparos(self, pantalla):
        if len(self.lista_disparos) > 0:
            for disparo in self.lista_disparos:
                disparo.animar(pantalla)
                disparo.actualizar()
                if disparo.rect_principal.centerx > 1820 or disparo.rect_principal.centerx < 0:
                    self.lista_disparos.remove(disparo)
