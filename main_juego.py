from configuraciones import *
from Modo import *
from class_Nivel_uno import Nivel_Uno
from class_Nivel_dos import Nivel_Dos
from class_Nivel_tres import Nivel_Tres
from pygame.locals import *
from GUI_form_prueba import FormPrueba



#########################################

ANCHO = 1366
ALTO = 768
TAMAÑO_PANTALLA = (ANCHO, ALTO)
FPS = 30

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
FUENTE = pygame.font.Font(r"Fuente\PixelifySans.ttf", 30)

form_principal = FormPrueba(PANTALLA, 433, 300, 500, 350, "Black", (32,42,212), 5, True)

# nivel_actual = Nivel_Tres(PANTALLA)

while True:
    RELOJ.tick(FPS)

    pygame.time.delay(60)

    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    form_principal.update(eventos)
    # nivel_actual.update(eventos)

    pygame.display.update()