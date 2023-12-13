import pygame
from pygame.locals import*
from UI.GUI_form import*
from UI.GUI_button_image import*
from GUI_form_contenedor_nivel import *
from manejador_niveles import Manejador_niveles
from Funciones_bd import *

class FormMenuPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        
        self._btn_resume = Button_Image(screen=self._master,
                                    master_x=x,
                                    master_y=y,
                                    x=325,
                                    y=320,
                                    w=50,
                                    h=50,
                                    color_background=(255,0,0),
                                    color_border=(255,0,255),
                                    onclick=self.btn_resume_click,
                                    onclick_param="",
                                    path_image=r"BTN\Colored Large Buttons\Back.png")

        self.lista_widgets.append(self._btn_resume)
        
    def on(self,parametro):
        print("hola",parametro) 
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_resume_click(self,param):
        self.end_dialog()
