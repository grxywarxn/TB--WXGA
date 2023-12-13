import pygame
from Modo import *
from Funciones_bd import *


class Nivel():
    def __init__(self, pantalla, fondo, personaje, portal, pisos, plataformas, plataformas_moviles, enemigos, enemigos_disparo, trampas, items, cajas, boss, nivel_actual):
        self._slave = pantalla
        self.fuente = pygame.font.SysFont("Arial",30)  
        self.img_fondo = fondo
        self.img_perder = pygame.image.load(r"Todoroki sprites\fondo_perder_banner.png")
        self.img_perder = pygame.transform.scale(self.img_perder, (1366,768))
        self.img_ganar = pygame.image.load(r"Todoroki sprites\stodoroki_banner.jpg")
        self.img_ganar = pygame.transform.scale(self.img_ganar, (1366,768))
        self.personaje = personaje
        self.portal = portal
        self.pisos = pisos
        self.plataformas = plataformas
        self.plataformas_moviles = plataformas_moviles
        self.enemigos = enemigos
        self.enemigos_disparo = enemigos_disparo
        self.trampas = trampas
        self.items = items
        self.cajas = cajas
        self.boss = boss

        self.perder_nivel = False
        self.ganar_nivel = False

        self.tiempo = 0
        self.contador_segundos = 0
        self.tiempo_limite = 150
        self.parar_cronometro = False
        self.pasar_nivel = False
        self.jugando = True 

        self.lista_jugadores = leer_datos_de_bd()
        self.jugador = self.lista_jugadores[-1]
        self.puntaje = self.personaje.puntos
        # self.acumulador_puntos = leer_puntaje_total(self.jugador["nombre"])

        self.nivel_actual = nivel_actual


        if self.boss is not None:
            self.explosiones = boss.lista_explosiones
            self.lluvia = boss.lista_flamas
            # self.tornados = boss.lista_tornados
        else:
            self.explosiones = None
            self.lluvia = None
            # self.tornados = None


    def update(self, eventos):
        if self.jugando == True:
            for evento in eventos:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                    pass
            self.controlar_personaje()
            self.actualizar_pantalla()
            self.timer()
            self.Terminar_juego()
            if self.parar_cronometro == False:
                self.actualizar_ui_personaje()

    def controlar_personaje(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.personaje.que_hace = "Derecha"
        elif keys[pygame.K_LEFT]:
            self.personaje.que_hace = "Izquierda"
        elif keys[pygame.K_UP]:
            self.personaje.que_hace = "Salta"
        elif keys[pygame.K_a]:
            self.personaje.que_hace = "Golpea"
        elif keys[pygame.K_s]:
            self.personaje.que_hace = "Dispara"
            if self.personaje.flag_disparo:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.personaje.tiempo_ultimo_disparo >= 300:
                    self.personaje.disparar()
                    self.personaje.tiempo_ultimo_disparo = tiempo_actual
                    self.personaje.disparando = False
        elif keys[pygame.K_r]:
            self.reiniciar_nivel()
        else:
            self.personaje.que_hace = "Quieto"

    def actualizar_pantalla(self):
        if self.jugando == True:
            self._slave.blit(self.img_fondo, (0,0))
            for portal in self.portal:
                if self.boss is None:
                    if len(self.enemigos) == 0 and len(self.items) == 0:
                        portal.visible = True
                        portal.actualizar(self._slave)
                elif self.boss.esta_muerto == True:
                        portal.visible = True
                        portal.actualizar(self._slave)
            for plataforma in self.plataformas:
                plataforma.actualizar(self._slave)
            for caja in self.cajas:
                caja.actualizar(self._slave)
            for plataforma_movil in self.plataformas_moviles:
                plataforma_movil.actualizar(self._slave)
                plataforma_movil.mover_plataforma()
            for piso in self.pisos:
                piso.actualizar(self._slave)
            for trampa in self.trampas:
                trampa.animar(self._slave)
                trampa.mover_trampa()
            for item in self.items:
                item.actualizar(self._slave)
            for enemigo in self.enemigos:
                enemigo.mover_en_x(self._slave)
            for enemigo_disparo in self.enemigos_disparo:
                enemigo_disparo.actualizar(self._slave)
            if self.boss is not None:
                self.boss.mostrar_vida(self._slave)
                if self.boss.visible == True:
                    self.boss.verificar_teleport()
                    self.boss.actualizar(self._slave)
                    self.boss.actualizar_flamas(self.plataformas)
                    self.boss.actualizar_explosiones()
                    # self.boss.actualizar_tornados()
                    for explosion in self.explosiones:
                        explosion.actualizar(self._slave)
                    for flama in self.lluvia:
                        flama.actualizar(self._slave)
                    # for tornado in self.tornados:
                    #     tornado.actualizar(self._slave)
            
            if self.personaje.visible:
                self.personaje.actualizar(self._slave)
                self.personaje.aplicar_gravedad(self._slave, self.plataformas, self.plataformas_moviles, self.pisos, self.cajas)
                self.personaje.actualizar_disparos(self._slave, self.enemigos, self.enemigos_disparo, self.boss)
                self.personaje.detectar_colision_con_items(self.items)
                self.personaje.detectar_colision_con_enemigos(self.enemigos)
                self.personaje.detectar_colision_con_trampas(self.trampas)
                self.personaje.detectar_colision_con_disparo_enemigo(self.enemigos_disparo)
                self.personaje.detectar_colision_con_explosion(self.explosiones)
                self.personaje.detectar_colision_con_lluvia(self.lluvia)
                self.personaje.detectar_colision_con_piso(self.pisos)
                self.personaje.detectar_colision_con_plataformas(self.plataformas)
                self.personaje.detectar_colision_con_plataformas_moviles(self.plataformas_moviles)
                self.personaje.detectar_colision_con_cajas(self.cajas)
                self.personaje.detectar_colision_con_portal(self.portal)

    def pantalla_perder(self):
        fuente = pygame.font.SysFont("Arial",30)  
        self._slave.blit(self.img_perder, (0,0))
        texto_renderizado = fuente.render(f"PERDISTE", True, "black")
        puntaje_renderizado = fuente.render(f"Puntuación: {self.personaje.puntos + self.tiempo_limite}", True, "white")
        self._slave.blit(texto_renderizado, (615, 480))
        self._slave.blit(puntaje_renderizado, (580, 570))
        # self._slave.blit(texto_renderizado, (800, 480))
        self.parar_cronometro = True

    def pantalla_ganar(self):
        fuente = pygame.font.SysFont("Arial",30)  
        self._slave.blit(self.img_ganar, (0,0))
        texto_renderizado = fuente.render(f"GANASTE", True, "black")
        puntaje_renderizado = fuente.render(f"Puntuación: {self.personaje.puntos + self.tiempo_limite}", True, "white")
        self._slave.blit(texto_renderizado, (615, 600))
        self._slave.blit(puntaje_renderizado, (580, 670))
        self.parar_cronometro = True

    def reiniciar_nivel(self):
        self.__init__(self._slave)

    def timer(self):
        self.contador_segundos += 1
        if self.parar_cronometro != True:
            if self.contador_segundos == 15:
                if self.tiempo != self.tiempo_limite:
                    self.tiempo_limite -= 1
                    self.contador_segundos = 0
                else:
                    self.tiempo_limite = 0
                    # self.reiniciar_nivel()

    def actualizar_ui_personaje(self):
        minutos = self.tiempo_limite // 60
        segundos = self.tiempo_limite % 60
        tiempo = self.fuente.render(f"Tiempo: {minutos:02}:{segundos:02}", True, "black")
        self._slave.blit(tiempo, (10, 110))
        texto_puntaje = self.fuente.render(f"Puntaje: {self.personaje.puntos}", True, "black")
        self._slave.blit(texto_puntaje, (10, 70))
        self.personaje.mostrar_vida(self._slave)

    def Terminar_juego(self):
        if self.personaje.visible == False and self.tiempo_limite > 0:
            self.parar_cronometro = True
            self.jugando = False    
            self.pasar_nivel = True
            self.guardar_puntaje_del_nivel()
            self.pantalla_ganar()
        elif self.personaje.vidas == 0 or self.tiempo_limite <= 0 or self.personaje.rect_principal.y > 768:
            self.pantalla_perder()
            self.pasar_nivel = False
            self.jugando = False 

    def guardar_puntaje_del_nivel(self):
        nivel_corriendo = lambda lista: lista.index(True)

        posicion = nivel_corriendo(self.nivel_actual) + 1

        self.jugador["puntaje"] = int(self.personaje.puntos + self.tiempo_limite)
        actualizar_datos_de_bd(self.jugador["nombre"], posicion, self.jugador["puntaje"])