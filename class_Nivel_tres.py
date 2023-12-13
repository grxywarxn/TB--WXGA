from configuraciones import *
from Modo import *
import random
from class_Personaje import Personaje
from class_Plataforma import Plataforma
from class_Plataforma_movil import Plataforma_movil
from class_Piso import Piso
from class_Enemigo import Enemigo
from class_Trampa import Trampa
from class_Item import Item
from class_Nivel import Nivel
from class_Boss import Boss
from class_Explosion import Explosion
from class_Flama import Flama
from class_Portal import Portal
from pygame.locals import *

class Nivel_Tres(Nivel):
    def __init__(self, pantalla):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        #FONDO
        fondo = pygame.image.load(r"Todoroki sprites\fallen-city-s.jpg")
        fondo = pygame.transform.scale(fondo, (W, H))
        #PERSONAJE
        s_todoroki = Personaje(animaciones_st, (40,64), 100, 200, 12)
        #PISO
        pisos_n1 = []
        pisos_n1.append(Piso(piso_img, 0, H - 20, (W, 20)))


        #PLATAFORMAS
        plataformas_n3 = []
        plataformas_n3.append(Plataforma(piso_s_img, 50, 300, (143,25)))
        plataformas_n3.append(Plataforma(piso_s_img, 1173, 300, (143,25)))
        plataformas_n3.append(Plataforma(piso_s_img, 193, 450, (143,25)))
        plataformas_n3.append(Plataforma(piso_s_img, 1030, 450, (143,25)))
        plataformas_n3.append(Plataforma(piso_s_img, 336, 600, (143,25)))
        plataformas_n3.append(Plataforma(piso_s_img, 887, 600, (143,25)))
        # plataformas_n1.append(Plataforma(piso_img, 0, -10, (1920, 10)))

        plataformas_n3.append(Plataforma(piso_s_img, 0, 450, (50, 25)))
        plataformas_n3.append(Plataforma(piso_s_img, 50, 600, (50, 25)))
        plataformas_n3.append(Plataforma(piso_s_img, 0, 750, (50, 25)))
        # plataformas_n3.append(Plataforma(piso_s_img, 50, 700, (50, 25)))
        #PLATAFORMAS MOVILES
        plataformas_moviles_n3 = []

        #ENEMIGOS
        enemigos_n3 = []

        enemigos_disparo = []
        #TRAMPAS
        trampas_n3 = []
        trampas_n3.append(Trampa(trap_animaciones, 0,650, (455, 228), "Fuego"))
        trampas_n3.append(Trampa(trap_animaciones, 455,650, (455, 228), "Fuego"))
        trampas_n3.append(Trampa(trap_animaciones, 910,650, (455, 228), "Fuego"))

        
        #ITEMS
        items_n3 = []
        items_n3.append(Item(heart, 15, 400, (20, 20), "vida"))
        items_n3.append(Item(heart, 65, 550, (20, 20), "vida"))
        items_n3.append(Item(heart, 254.5, 400, (20, 20), "vida"))
        items_n3.append(Item(fire_ball, 397.5, 550, (20,20), "bola_fuego"))



        #CAJAS
        cajas_n3 = []
        
        #MUSICA
        pygame.mixer.init()

        pygame.mixer.music.load(r"Musica\Rumbling.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)

        portal = [Portal(portal_animaciones, (40, 100), 663, 450)]
        d_todoroki = Boss(dt_animaciones, (40, 67), 1225, 233, 3)

        nivel_1 = False
        nivel_2 = False
        nivel_3 = True

        self.nivel_actual = [nivel_1, nivel_2, nivel_3]

        super().__init__(pantalla, fondo, s_todoroki, portal, pisos_n1, plataformas_n3, plataformas_moviles_n3, enemigos_n3, enemigos_disparo, trampas_n3, items_n3, cajas_n3, d_todoroki, self.nivel_actual)