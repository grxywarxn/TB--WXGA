import pygame
import random
from configuraciones import *
from class_Flama import Flama
from class_Explosion import Explosion
from class_Tornado import Tornado

class Boss:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, * tamaño)
        self.rect_principal = animaciones["Idle_l"][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["Idle_l"]
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        self.que_hace = "Quieto"


        self.img_vidas_actuales = vidas_boss[10]
        self.vidas = 10
        self.timer_daño_recibido = 3000
        self.ultimo_daño_recibido = pygame.time.get_ticks()
        self.esta_muerto = False
        self.esta_muriendo = False
        self.visible = True

        self.lista_explosiones = []

        self.tiempo_ultimo_casteo = pygame.time.get_ticks()
        self.intervalo_casteo = 5000
        self.casteo = False

        self.tiempo_ultimo_teleport = pygame.time.get_ticks()
        self.intervalo_teleport = 3000
        self.teleport = False
        self.lista_coordenadas = [(1225, 233), (1082, 383), (939, 533)]

        self.lista_flamas = []

        # self.lista_tornados = []
        # self.flag_tornado = False
        # self.tiempo_ultimo_tornado = 0
        # self.creando_tornado = False

        self.sonido_castear = pygame.mixer.Sound(r"Sonidos\dabi_cast.wav")
        self.sonido_castear.set_volume(0.1)

        self.sonido_explosion = pygame.mixer.Sound(r"Sonidos\dabi_explosion.wav")
        self.sonido_explosion.set_volume(0.05)

        self.sonido_recibir_daño = pygame.mixer.Sound(r"Sonidos\dabi_recibir_daño.wav")
        self.sonido_recibir_daño.set_volume(0.1)

        self.sonido_teleport = pygame.mixer.Sound(r"Sonidos\dabi_teleport.wav")
        self.sonido_teleport.set_volume(0.1)
        
        self.sonido_7_vidas = pygame.mixer.Sound(r"Sonidos\dabi_vidas_7.wav")
        self.sonido_7_vidas.set_volume(0.3)
        self.flag_sonido_7_vidas = False

        self.sonido_3_vidas = pygame.mixer.Sound(r"Sonidos\dabi_vidas_3.wav")
        self.sonido_3_vidas.set_volume(0.3)
        self.flag_sonido_3_vidas = False

        self.sonido_morir = pygame.mixer.Sound(r"Sonidos\dabi_morir.wav")
        self.sonido_morir.set_volume(0.3)
        self.flag_sonido_muerte = False


    def aplicar_gravedad(self, plataformas):
        if self.saltando:
            for lado in self.rectangulos:
                self.rectangulos[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida :
                self.desplazamiento_y += self.gravedad
                
        for plataforma in plataformas:   
            if self.rectangulos["bottom"].colliderect(plataforma.rectangulos["top"]):
                self.rectangulos["main"].bottom = plataforma.rectangulos["main"].top - 5
                self.saltando = False
                self.desplazamiento_y = 0
                break 
            else:
                self.saltando = True
    
    def animar(self, pantalla):
        if self.visible:
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
            self.contador_pasos += 1
            
            if self.que_hace == "Teletransporte" and self.contador_pasos >= largo:
                self.que_hace = "Quieto"

            if self.que_hace == "Castea" and self.contador_pasos >= largo:
                self.que_hace = "Quieto"



    def actualizar(self, pantalla):
        if self.visible == True:
            match self.que_hace:
                case "Quieto":
                        self.animacion_actual = self.animaciones["Wait_l"]
                        self.animar(pantalla)
                case "Teletransporte":
                        self.animacion_actual = self.animaciones["Teleport"]
                        self.animar(pantalla)
        else:
            pass


    def actualizar_posicion(self):
        if self.visible == True:
            self.sonido_teleport.play()
            self.sonido_castear.play()
            coordenada_actual = (self.rect_principal.x, self.rect_principal.y)
            nueva_coordenada = random.choice(self.lista_coordenadas)
            x = nueva_coordenada[0]
            y = nueva_coordenada[1]
            if coordenada_actual != nueva_coordenada:
                self.rect_principal.x = x
                self.rect_principal.y = y
                coordenada_actual = nueva_coordenada

    def verificar_teleport(self):
        tiempo_actual = pygame.time.get_ticks()
        if self.visible == True:
            if tiempo_actual - self.tiempo_ultimo_teleport >= self.intervalo_teleport:
                self.que_hace = "Teletransporte"
                self.actualizar_posicion()
                self.crear_lluvia_de_fuego()
                self.crear_explosion()
                # self.crear_tornado()
                self.tiempo_ultimo_teleport = tiempo_actual

    def mostrar_vida(self, pantalla):

        if self.vidas == 10:
            self.img_vidas_actuales = vidas_boss[10]
        elif self.vidas == 9:
            self.img_vidas_actuales = vidas_boss[9]
        elif self.vidas == 8:
            self.img_vidas_actuales = vidas_boss[8]
        elif self.vidas == 7:
            self.img_vidas_actuales = vidas_boss[7]
            if self.flag_sonido_7_vidas == False:
                self.sonido_7_vidas.play()
                self.flag_sonido_7_vidas = True
        elif self.vidas == 6:
            self.img_vidas_actuales = vidas_boss[6]
        elif self.vidas == 5:
            self.img_vidas_actuales = vidas_boss[5]
        elif self.vidas == 4:
            self.img_vidas_actuales = vidas_boss[4]
        elif self.vidas == 3:
            self.img_vidas_actuales = vidas_boss[3]
            if self.flag_sonido_3_vidas == False:
                self.sonido_3_vidas.play()
                self.flag_sonido_3_vidas = True
        elif self.vidas == 2:
            self.img_vidas_actuales = vidas_boss[2]
        elif self.vidas == 1:
            self.img_vidas_actuales = vidas_boss[1]
        else:
            self.img_vidas_actuales = vidas_boss[0]
            if self.flag_sonido_muerte == False:
                self.sonido_morir.play()
                self.flag_sonido_muerte = True

        vidas_actuales = pygame.transform.scale(self.img_vidas_actuales, (160, 54))
        pantalla.blit(vidas_actuales, (1186, 30))

    def recibir_daño(self):
        tiempo_actual = pygame.time.get_ticks()
        if self.visible == True:
            if tiempo_actual - self.ultimo_daño_recibido >= self.timer_daño_recibido:
                self.sonido_recibir_daño.play()
                self.vidas -= 1
                self.ultimo_daño_recibido = tiempo_actual
                if self.vidas <= 0:
                    self.esta_muerto = True
                    self.visible = False
                    self.lista_explosiones = []

    def crear_lluvia_de_fuego(self):
        if self.visible == True:

            if self.vidas > 6:
                flamas = 5
            elif self.vidas > 3:
                flamas = 10
            else:
                flamas = 20
            for i in range(flamas):
                velocidad = random.randint(5, 15)
                self.lista_flamas.append(Flama(animaciones_lluvia, (17,30), velocidad))
            return self.lista_flamas

    def actualizar_flamas(self, plataformas):
        if self.visible == True:

            for flama in self.lista_flamas:
                if flama.rect_principal.y >= 990:
                    self.lista_flamas.remove(flama)
                for plataforma in plataformas:
                    if flama.rect_principal.colliderect(plataforma.rect_principal):
                        self.lista_flamas.remove(flama)

    def crear_explosion(self):
        if self.visible == True:

            if self.vidas > 5:
                explosiones = 1
            else:
                explosiones = 2
            
            self.sonido_explosion.play()
            for i in range(explosiones):
                self.lista_explosiones.append(Explosion(animaciones_ataque_dabi, (100,100)))
            return self.lista_explosiones
    
    def actualizar_explosiones(self):
        if self.esta_muerto == False:
            for explosion in self.lista_explosiones:
                if explosion.animando and explosion.contador_pasos >= len(explosion.animacion_actual):
                    explosion.animando = False
                    self.lista_explosiones.remove(explosion)

    # def crear_tornado(self):
    #     if self.vidas > 7:
    #         tornado = 0
    #     else: 
    #         tornado = 1
    #     for i in range(tornado):
    #         self.lista_tornados.append(Tornado(animaciones_ataque_dabi, (100, 70), self.rect_principal.x, self.rect_principal.y))

    # def actualizar_tornados(self):
    #     if len(self.lista_tornados) > 0:
    #         for tornado in self.lista_tornados:
    #             if tornado.rect_principal.centerx > 1820 or tornado.rect_principal.centerx < 0:
    #                 self.lista_tornados.remove(tornado)