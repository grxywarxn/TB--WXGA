from configuraciones import *
from Modo import *
from class_Personaje import Personaje
from class_Plataforma import Plataforma
from class_Plataforma_movil import Plataforma_movil
from class_Piso import Piso
from class_Enemigo import Enemigo
from class_Trampa import Trampa
from class_Enemigo_disparo import Enemigo_disparo
from class_Item import Item
from class_Nivel import Nivel
from class_Portal import Portal
from pygame.locals import *

class Nivel_Dos(Nivel):
    def __init__(self, pantalla):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        #FONDO
        fondo = pygame.image.load(r"Todoroki sprites\ambg.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        #PERSONAJE
        s_todoroki = Personaje(animaciones_st, (40,64), 100, H - 104, 12)
        #PISO
        pisos_n2 = []
        pisos_n2.append(Piso(piso_img, 0, 728, (408, 40)))
        pisos_n2.append(Piso(piso_s_img, 470, 728, (35, 40)))
        pisos_n2.append(Piso(piso_s_img, 567, 728, (35, 40)))
        pisos_n2.append(Piso(piso_s_img, 664, 728, (35, 40)))
        pisos_n2.append(Piso(piso_s_img, 761, 728, (35, 40)))
        pisos_n2.append(Piso(piso_s_img, 858, 728, (35, 40)))
        pisos_n2.append(Piso(piso_img, 958, 728, (408, 40)))
        #PLATAFORMAS
        plataformas = []
        plataformas.append(Plataforma(piso_img, 360, 380, (143, 25)))
        plataformas.append(Plataforma(piso_img, 863, 380, (143, 25)))
        plataformas.append(Plataforma(piso_img, 160, 280, (143, 25)))
        plataformas.append(Plataforma(piso_img, 1063, 280, (143, 25)))
        plataformas.append(Plataforma(piso_img, 383, 150, (600, 25)))
        plataformas.append(Plataforma(piso_img, 633, 480, (100, 25)))

        plataformas.append(Plataforma(piso_img, 0, -10, (1366, 10)))
        # plataformas.append(Plataforma(piso_img, 0, 1080 - 30, (1920, 30)))

        plataformas.append(Plataforma(piso_s_img, 1316, 200, (50, 25)))
        plataformas.append(Plataforma(piso_s_img, 0, 300, (50, 25)))
        plataformas.append(Plataforma(piso_s_img, 1316, 400, (50, 25)))
        plataformas.append(Plataforma(piso_s_img, 0, 500, (50, 25)))
        plataformas.append(Plataforma(piso_s_img, 1316, 600, (50, 25)))
        plataformas.append(Plataforma(piso_s_img, 0, 100, (50, 25)))

        plataformas_moviles = []

        #ENEMIGOS
        enemigos = []
        enemigos.append(Enemigo(animaciones_nomu, 383, 80, (49, 70), True, 383, 930))
        enemigos.append(Enemigo(animaciones_nomu, 930, 80, (49, 70), True, 383, 930))

        enemigos_disparo = []
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 0, 430, (49, 70), "Derecha"))
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 0, 230, (49, 70), "Derecha"))
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 0, 30, (49, 70), "Derecha"))
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 1317, 530, (49, 70), "Izquierda"))
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 1317, 330, (49, 70), "Izquierda"))
        enemigos_disparo.append(Enemigo_disparo(animaciones_nomu, 1317, 130, (49, 70), "Izquierda"))
        #TRAMPAS
        trampas = []
        trampas.append(Trampa(trap_animaciones, 413, 738, (52,30), "Saw"))
        trampas.append(Trampa(trap_animaciones, 510, 738, (52,30), "Saw"))
        trampas.append(Trampa(trap_animaciones, 607, 738, (52,30), "Saw"))
        trampas.append(Trampa(trap_animaciones, 704, 738, (52,30), "Saw"))
        trampas.append(Trampa(trap_animaciones, 801, 738, (52,30), "Saw"))
        trampas.append(Trampa(trap_animaciones, 898, 738, (52,30), "Saw"))

        #ITEMS
        items = []
        items.append(Item(heart, 215, 250, (20, 20), "vida"))
        items.append(Item(heart, 673, 530, (20, 20), "vida"))
        items.append(Item(speed_boost, 673, 420, (20,30), "rayo"))
        items.append(Item(ice_ball, 1125, 220, (20,20), "bola_hielo"))
        items.append(Item(fire_ball, 200, 665, (20,20), "bola_fuego"))
        items.append(Item(bonus_gem, 673, 40, (20,20), "diamante")) 
        #CAJAS
        cajas = []
        cajas.append(Plataforma(caja_img, 373, 693, (35,35)))

        cajas.append(Plataforma(caja_img, 470, 658, (35,35)))
        cajas.append(Plataforma(caja_img, 470, 693, (35,35)))

        cajas.append(Plataforma(caja_img, 567, 693, (35,35)))
        cajas.append(Plataforma(caja_img, 567, 658, (35,35)))
        cajas.append(Plataforma(caja_img, 567, 623, (35,35)))

        cajas.append(Plataforma(caja_img, 664, 693, (35,35)))
        cajas.append(Plataforma(caja_img, 664, 658, (35,35)))
        cajas.append(Plataforma(caja_img, 664, 623, (35,35)))
        cajas.append(Plataforma(caja_img, 664, 588, (35,35)))

        cajas.append(Plataforma(caja_img, 761, 693, (35,35)))
        cajas.append(Plataforma(caja_img, 761, 658, (35,35)))
        cajas.append(Plataforma(caja_img, 761, 623, (35,35)))

        cajas.append(Plataforma(caja_img, 858, 693, (35,35)))
        cajas.append(Plataforma(caja_img, 858, 658, (35,35)))

        cajas.append(Plataforma(caja_img, 957, 693, (35,35)))

        boss = None

        portal = [Portal(portal_animaciones, (40, 100), 663, 350)]
        #MUSICA
        pygame.mixer.init()

        pygame.mixer.music.load(r"Musica\AshesonTheFire.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        nivel_1 = False
        nivel_2 = True
        nivel_3 = False

        self.nivel_actual = [nivel_1, nivel_2, nivel_3]

        super().__init__(pantalla, fondo, s_todoroki, portal, pisos_n2, plataformas, plataformas_moviles, enemigos, enemigos_disparo, trampas, items, cajas, boss, self.nivel_actual)