from configuraciones import *
from Modo import *
from class_Personaje import Personaje
from class_Plataforma import Plataforma
from class_Plataforma_movil import Plataforma_movil
from class_Piso import Piso
from class_Enemigo import Enemigo
from class_Trampa import Trampa
from class_Item import Item
from class_Nivel import Nivel
from class_Portal import Portal
from pygame.locals import *

class Nivel_Uno(Nivel):
    def __init__(self, pantalla):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        #FONDO
        fondo = pygame.image.load(r"Todoroki sprites\ua_bg.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        #PERSONAJE
        s_todoroki = Personaje(animaciones_st, (40,64), 100, H - 104, 12)
        #PISO
        pisos_n1 = []
        pisos_n1.append(Piso(piso_img, 0, H - 40, (W, 40)))
        #PLATAFORMAS
        plataformas_n1 = []
        plataformas_n1.append(Plataforma(plat_img, 200, H - 150, (271, 25)))
        plataformas_n1.append(Plataforma(plat_img, W - 36, H - 150, (36, 25)))
        plataformas_n1.append(Plataforma(plat_img, W - 72, H - 250, (36, 25)))
        plataformas_n1.append(Plataforma(plat_img, 950, H - 250, (272, 25)))
        plataformas_n1.append(Plataforma(plat_img, 150, H - 400, (321, 25)))
        plataformas_n1.append(Plataforma(plat_img, 600, 200, (286, 25)))
        plataformas_n1.append(Plataforma(plat_img, 450, 200, (36, 25)))
        plataformas_n1.append(Plataforma(plat_img, 300, 200, (36, 25)))
        plataformas_n1.append(Plataforma(plat_img, 720, 100, (71, 25)))
        plataformas_n1.append(Plataforma(plat_img, 0, -10, (W, 10)))

        #PLATAFORMAS MOVILES
        plataformas_moviles_n1 = []
        plataformas_moviles_n1.append(Plataforma_movil(plat_img, 600, 418, (179, 25), 418, 618, "y"))
        #ENEMIGOS
        enemigos_n1 = []
        enemigos_n1.append(Enemigo(animaciones_nomu, 500, 660, (49, 70), True, 500,700))
        enemigos_n1.append(Enemigo(animaciones_nomu, 220, 300, (49, 70), True, 220, 420))
        enemigos_n1.append(Enemigo(animaciones_nomu, 600, 135, (49, 70), True, 600, 800))
        enemigos_disparo = []
        #TRAMPAS
        trampas_n1 = []
        trampas_n1.append(Trampa(trap_animaciones, 200, 698, (52,30), "Saw", True, 200, 405, "x"))
        trampas_n1.append(Trampa(trap_animaciones, 800, 698, (52,30), "Saw", True, 800, 1314, "x", 12))
        trampas_n1.append(Trampa(trap_animaciones, 235, 590, (52,30), "Saw", True, 235, 380, "x"))
        trampas_n1.append(Trampa(trap_animaciones, 950, 490, (52,30), "Saw", True, 950, 1175, "x", 7))
        #ITEMS
        items_n1 = []
        items_n1.append(Item(speed_boost, 700, 660, (20,30), "rayo"))
        items_n1.append(Item(heart, 160, 250, (20, 20), "vida"))
        items_n1.append(Item(ice_ball, 1300, 450, (20,20), "bola_hielo"))
        items_n1.append(Item(fire_ball, 440, 510, (20,20), "bola_fuego"))
        items_n1.append(Item(bonus_gem, 750, 60, (20,20), "diamante"))

        #CAJAS
        cajas_n1 = []
        cajas_n1.append(Plataforma(caja_img, 200, 583, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 435, 583, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 435, 548, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 185, 335, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 150, 300, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 150, 335, (35,35)))
        cajas_n1.append(Plataforma(caja_img, 850, 165, (35,35)))
        #MUSICA

        boss = None

        portal = [Portal(portal_animaciones, (40, 100), 1150, 350)]
        pygame.mixer.init()

        pygame.mixer.music.load(r"Musica\MightU.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        nivel_1 = True
        nivel_2 = False
        nivel_3 = False

        self.nivel_actual = [nivel_1, nivel_2, nivel_3]

        super().__init__(pantalla, fondo, s_todoroki, portal, pisos_n1, plataformas_n1, plataformas_moviles_n1, enemigos_n1, enemigos_disparo, trampas_n1, items_n1, cajas_n1, boss, self.nivel_actual)