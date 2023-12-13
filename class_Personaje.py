import pygame
from class_Disparo import Disparo
from configuraciones import *

class Personaje:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, * tamaño)
        self.rect_principal = animaciones["Idle_r"][0].get_rect()
        self.rect_principal.x = pos_x
        self.rect_principal.y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.que_hace = "Quieto"
        self.animacion_actual = self.animaciones["Idle_r"]
        self.rectangulos = obtener_rectangulos(self.rect_principal)
        self.direccion = "Derecha"
        self.visible = True

        self.gravedad = 3
        self.saltando = False
        self.desplazamiento_y = 0
        self.potencia_salto = -30
        self.limite_velocidad_salto = 20

        self.en_plataforma_movil = False

        self.lista_disparos = []
        self.flag_disparo = True
        self.tiempo_ultimo_disparo = 0
        self.disparando = False
        self.elemento = "Hielo"

        self.img_vidas_actuales = vidas[5]
        self.vidas = 5
        self.puntos = 0
        self.timer_daño_recibido = 2000
        self.ultimo_daño_recibido = pygame.time.get_ticks()

        self.fuente = pygame.font.Font(r"Fuente\PixelifySans.ttf", 30)
        self.tiempo = 5
        self.tiempo_pausado = False


        #Sonidos
        pygame.mixer.init()
        self.sonido_colision_disparos =  pygame.mixer.Sound(r"Sonidos\t_colision_entre_disparos.wav")
        self.sonido_colision_disparos.set_volume(0.04)

        self.sonido_disparar = pygame.mixer.Sound(r"Sonidos\t_disparar.wav")
        self.sonido_disparar.set_volume(0.1)

        self.sonido_disparo_fuego = pygame.mixer.Sound(r"Sonidos\t_disparo_fuego.wav")
        self.sonido_disparo_fuego.set_volume(0.1)
        
        self.sonido_impacto_fuego = pygame.mixer.Sound(r"Sonidos\t_impacto_fuego.wav")
        self.sonido_impacto_fuego.set_volume(0.1)
        
        self.sonido_impacto_hielo = pygame.mixer.Sound(r"Sonidos\t_impacto_hielo.wav")
        self.sonido_impacto_hielo.set_volume(0.1)

        self.sonido_recibir_daño = pygame.mixer.Sound(r"Sonidos\t_recibir_daño.wav")
        self.sonido_recibir_daño.set_volume(0.1)

        self.sonido_recoger_diamante = pygame.mixer.Sound(r"Sonidos\t_recoger_diamante.wav")
        self.sonido_recoger_diamante.set_volume(0.1)

        self.sonido_recoger_bola_hielo = pygame.mixer.Sound(r"Sonidos\t_recoger_hielo.wav")
        self.sonido_recoger_bola_hielo.set_volume(0.2)

        self.sonido_recuperar_vida = pygame.mixer.Sound(r"Sonidos\t_recuperar_hp.wav")
        self.sonido_recuperar_vida.set_volume(0.1)

    def caminar(self, pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda":
            velocidad_actual *= -1
        nueva_posicion = self.rect_principal.x + velocidad_actual
        if nueva_posicion > 0 - self.rect_principal.width /2 and nueva_posicion <= (pantalla.get_width() - self.rect_principal.width / 2):
            for lado in self.rectangulos:
                self.rectangulos[lado].x += velocidad_actual

    def animar(self, pantalla):
        if self.visible:
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
            self.contador_pasos += 1

    def aplicar_gravedad(self, pantalla, plataformas, plataformas_moviles, pisos, cajas):

        #SALTO
        if self.saltando:
            self.animar(pantalla)
            for lado in self.rectangulos:
                self.rectangulos[lado].y += self.desplazamiento_y
                self.rectangulos = obtener_rectangulos(self.rect_principal)

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            self.en_plataforma_movil = False

        #ANIMACIONES DE SALTO
        if self.direccion == "Derecha" and self.desplazamiento_y < 0:
            self.animacion_actual = self.animaciones["Jump_r"]
        elif self.direccion == "Derecha" and self.desplazamiento_y > 0:
            self.animacion_actual = self.animaciones["Fall_r"]
        elif self.direccion == "Izquierda" and self.desplazamiento_y < 0:
            self.animacion_actual = self.animaciones["Jump_l"]
        elif self.direccion == "Izquierda" and self.desplazamiento_y > 0:
            self.animacion_actual = self.animaciones["Fall_l"]

    #CAMBIO DE ANIMACIONES

    def actualizar(self, pantalla):
        match self.que_hace:
            case "Derecha":
                self.direccion = "Derecha"
                if not self.saltando:
                    if self.direccion == "Derecha":
                        self.animacion_actual = self.animaciones["Run_r"]
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "Izquierda":
                self.direccion = "Izquierda"
                if not self.saltando:
                    if self.direccion == "Izquierda":
                        self.animacion_actual = self.animaciones["Run_l"]
                    self.animar(pantalla)
                self.caminar(pantalla)
            case "Quieto":
                if not self.saltando:
                    if self.direccion == "Derecha":
                        self.animacion_actual = self.animaciones["Idle_r"]
                    else:
                        self.animacion_actual = self.animaciones["Idle_l"]
                        self.direccion = "Izquierda"
                    self.animar(pantalla)
            case "Golpea":
                if not self.saltando:
                    if self.direccion == "Derecha":
                        self.animacion_actual = self.animaciones["Punch_r"]
                    else:
                        self.animacion_actual = self.animaciones["Punch_l"]
                    self.animar(pantalla)
            case "Salta":
                if not self.saltando:
                    self.saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.en_plataforma_movil = False
                    self.animar(pantalla)

            case "Dispara":
                if not self.saltando:
                    if self.direccion == "Derecha":
                        self.animacion_actual = self.animaciones["Shoot_r"]
                    else:
                        self.animacion_actual = self.animaciones["Shoot_l"]
                    self.animar(pantalla)


    def detectar_colision_con_piso(self, pisos):
        for piso in pisos:
            if self.rectangulos["bottom"].colliderect(piso.rectangulos["top"]):
                self.saltando = False
                self.desplazamiento_y = 0
                self.rectangulos["main"].bottom = piso.rectangulos["main"].top
                break
            else:
                self.saltando = True
    
    def detectar_colision_con_plataformas(self, plataformas):
        for plataforma in plataformas:
            if self.rectangulos["bottom"].colliderect(plataforma.rectangulos["top"]):
                self.saltando = False
                self.desplazamiento_y = 0
                self.rectangulos["main"].bottom = plataforma.rectangulos["main"].top

            elif self.rectangulos["top"].colliderect(plataforma.rectangulos["bottom"]):    
                self.saltando = True
                self.desplazamiento_y = self.limite_velocidad_salto
                self.rectangulos["main"].top = plataforma.rectangulos["main"].bottom
            elif self.rectangulos["right"].colliderect(plataforma.rectangulos["left"]):
                self.saltando = True
                self.rectangulos["main"].right = plataforma.rectangulos["main"].left
            elif self.rectangulos["left"].colliderect(plataforma.rectangulos["right"]):
                self.saltando = True
                self.rectangulos["main"].left = plataforma.rectangulos["main"].right

    def detectar_colision_con_plataformas_moviles(self, plataformas_moviles):
        for plataforma in plataformas_moviles:
            if plataforma.movil:
                if self.rectangulos["bottom"].colliderect(plataforma.rectangulos["top"]):
                    self.saltando = False
                    self.desplazamiento_y = 0
                    self.rectangulos["main"].bottom = plataforma.rectangulos["main"].top
                    self.en_plataforma_movil = True
                    if self.en_plataforma_movil:
                        self.saltando = False
                        self.rect_principal.y += plataforma.velocidad 
                        self.rectangulos["main"].bottom = plataforma.rectangulos["main"].top
                        self.rectangulos = obtener_rectangulos(self.rect_principal)
            elif self.rect_principal.x < plataforma.cc_inicial or self.rect_principal.x > plataforma.cc_final:
                self.en_plataforma_movil = False

    def detectar_colision_con_cajas(self, cajas):
        for caja in cajas:
            if self.rectangulos["bottom"].colliderect(caja.rectangulos["top"]):
                self.saltando = False
                self.desplazamiento_y = 0
                self.rectangulos["main"].bottom = caja.rectangulos["main"].top

    def moverse_en_plataformas_moviles_en_y(self, plataforma):
        if plataforma.velocidad < 0:
            self.rectangulos = obtener_rectangulos(self.rect_principal)
            # self.saltando = False
            self.rectangulos["main"].bottom = plataforma.rect_principal.top
        elif plataforma.velocidad > 0:
            self.rectangulos = obtener_rectangulos(self.rect_principal)
            # self.saltando = False
            self.rectangulos["main"].bottom = plataforma.rect_principal.top
        else:
            self.en_plataforma_movil = False
            self.saltando = True

    def detectar_colision_con_items(self, items):
        for item in items:
            if self.rect_principal.colliderect(item.rect_principal):
                match item.tipo:
                    case "diamante":
                        self.puntos += 50
                        self.sonido_recoger_diamante.play()
                        items.remove(item)
                    case "rayo":
                        items.remove(item)
                        self.velocidad *= 1.2
                        self.puntos += 5
                    case "bola_hielo":
                        items.remove(item)
                        self.elemento = "Hielo"
                        self.puntos += 5
                        self.sonido_recoger_bola_hielo.play()
                    case "bola_fuego":
                        items.remove(item)
                        self.elemento = "Fuego"
                        self.puntos += 5
                    case "vida":
                        if self.vidas < 5:
                            self.vidas += 1
                            self.sonido_recuperar_vida.play()
                            items.remove(item)
                        elif self.vidas >= 5:
                            pass
                            # items.remove(item)

    def disparar(self):
        self.disparando = True
        self.sonido_disparar.play()

        x = None
        y = self.rect_principal.centery - 7
        if (self.que_hace == "Derecha" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "saltando") and self.direccion == "Derecha":
            x = self.rect_principal.right
        elif (self.que_hace == "Izquierda" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "saltando") and self.direccion == "Izquierda":
            x = self.rect_principal.left - 40

        if x is not None:
            self.lista_disparos.append(Disparo(x, y, self.que_hace, self.direccion, self.elemento))

    def actualizar_disparos(self, pantalla, enemigos, enemigos_disparo, boss):
        if len(self.lista_disparos) > 0:
            for disparo in self.lista_disparos:
                disparo.animar(pantalla)
                disparo.actualizar()
                if disparo.rect_principal.centerx > 1820 or disparo.rect_principal.centerx < 0:
                    self.lista_disparos.remove(disparo)
                else:
                    for enemigo in enemigos:
                        if disparo.rect_principal.colliderect(enemigo.rect_principal):
                            disparo.colision = True
                            enemigo.velocidad = 0
                            enemigo.esta_muriendo = True
                            self.puntos += 20
                            enemigo.sonido_recibir_disparo.play()
                            enemigos.remove(enemigo)
                            del enemigo
                            self.lista_disparos.remove(disparo)
                    for enemigo_disparo in enemigos_disparo:
                        if disparo.rect_principal.colliderect(enemigo_disparo.rect_principal):
                            disparo.colision = True
                            enemigo_disparo.sonido_recibir_disparo.play()
                            enemigo_disparo.esta_muriendo = True
                            self.puntos += 20
                            enemigos_disparo.remove(enemigo_disparo)
                            del enemigo_disparo
                            self.lista_disparos.remove(disparo)
                    if boss is not None:
                        if disparo.rect_principal.colliderect(boss.rect_principal):
                            disparo.colision = True
                            if boss.vidas > 0:
                                boss.recibir_daño()
                                self.puntos += 100
                            elif boss.esta_muerto == True:
                                self.puntos += 500
                                boss.visible = False
                            elif boss.visible == False:
                                pass
                    else:
                        pass
    def controlar_personaje(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.que_hace = "Derecha"
        elif keys[pygame.K_LEFT]:
            self.que_hace = "Izquierda"
        elif keys[pygame.K_UP]:
            self.que_hace = "Salta"
        elif keys[pygame.K_a]:
            self.que_hace = "Golpea"
        elif keys[pygame.K_s]:
            self.que_hace = "Dispara"
            if self.flag_disparo:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.tiempo_ultimo_disparo >= 300:
                    self.disparar()
                    self.tiempo_ultimo_disparo = tiempo_actual
                    self.disparando = False

        else:
            self.que_hace = "Quieto"

    def mostrar_vida(self, pantalla):

        if self.vidas == 5:
            self.img_vidas_actuales = vidas[5]
        elif self.vidas == 4:
            self.img_vidas_actuales = vidas[4]
        elif self.vidas == 3:
            self.img_vidas_actuales = vidas[3]
        elif self.vidas == 2:
            self.img_vidas_actuales = vidas[2]
        elif self.vidas == 1:
            self.img_vidas_actuales = vidas[1]
        else:
            self.img_vidas_actuales = vidas[0]

        vidas_actuales = pygame.transform.scale(self.img_vidas_actuales, (160, 25))
        pantalla.blit(vidas_actuales, (10, 30))

    def recibir_daño(self):

        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - self.ultimo_daño_recibido >= self.timer_daño_recibido:
            self.sonido_recibir_daño.play()
            self.vidas -= 1

            self.ultimo_daño_recibido = tiempo_actual


    def detectar_colision_con_enemigos(self, enemigos):
        for enemigo in enemigos:
            if self.rectangulos["bottom"].colliderect(enemigo.rectangulos["top"]):
                enemigo.velocidad = 0
                enemigo.esta_muriendo = True
                enemigos.remove(enemigo)
                self.puntos += 20
                enemigo.sonido_recibir_daño.play()
                del enemigo
            elif self.rectangulos["main"].colliderect(enemigo.rectangulos["left"]):
                self.recibir_daño()
            elif self.rectangulos["main"].colliderect(enemigo.rectangulos["right"]):
                self.recibir_daño()


    def detectar_colision_con_trampas(self, trampas):
        for trampa in trampas:
            if self.rectangulos["main"].colliderect(trampa.rect_principal):
                self.recibir_daño()

    def detectar_colision_con_disparo_enemigo(self, enemigo_disparo):
        try:
            for enemigo in enemigo_disparo:
                for disparo in enemigo.lista_disparos:
                    if disparo.rect_principal.colliderect(self.rect_principal):
                        self.recibir_daño()
                        enemigo.lista_disparos.remove(disparo)
                    
                    for disparo_personaje in self.lista_disparos:
                        if disparo_personaje.rect_principal.colliderect(disparo.rect_principal):
                            self.sonido_colision_disparos.play()
                            self.puntos += 10
                            self.lista_disparos.remove(disparo_personaje)
                            enemigo.lista_disparos.remove(disparo)
        except ValueError as e:
            print(f"Disparo no encontrado, error: {e}")

    def detectar_colision_con_explosion(self, explosiones):
        if explosiones is not None:
            for explosion in explosiones:
                if self.rect_principal.colliderect(explosion.rect_principal):
                    self.recibir_daño()

    def detectar_colision_con_lluvia(self, lluvia):
        if lluvia is not None:
            for flama in lluvia:
                if self.rect_principal.colliderect(flama.rect_principal):
                    self.recibir_daño()
                    lluvia.remove(flama)
                try:
                    for disparo_personaje in self.lista_disparos:
                        if disparo_personaje.rect_principal.colliderect(flama.rect_principal):
                            self.sonido_colision_disparos.play()
                            self.puntos += 10
                            self.lista_disparos.remove(disparo_personaje)
                            lluvia.remove(flama)
                except ValueError as e:
                    print(f"Disparo o flama no encontrados, error: {e}")

    def detectar_colision_con_portal(self, portal):
        for p in portal:
            if p.visible:
                if self.rect_principal.colliderect(p.rect_principal):
                    self.visible = False
