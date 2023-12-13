import pygame
from pygame.locals import*
from UI.GUI_form import*
from UI.GUI_button_image import*
from GUI_form_contenedor_nivel import *
from manejador_niveles import Manejador_niveles
from Funciones_bd import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))

        self.lista_jugadores = leer_datos_de_bd()
        self.jugador = self.lista_jugadores[-1]
        self.nombre_jugador = self.jugador["nombre"]
        print(self.jugador)

        self._slave = aux_image
        self._btn_level_1 = Button_Image(screen=self._slave,
                                        x=41,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.entrar_nivel,
                                        onclick_param="nivel_uno",
                                        path_image=r"BTN\n1.jpg")
        
        self._btn_level_1_locked = Button_Image(screen=self._slave,
                                        x=41,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.nivel_bloqueado,
                                        onclick_param="nivel_uno",
                                        path_image=r"BTN\n1_blocked.jpg")
        
        self._btn_level_2 = Button_Image(screen=self._slave,
                                        x=261,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.entrar_nivel,
                                        onclick_param="nivel_dos",
                                        path_image=r"BTN\n2.jpg")
        
        self._btn_level_2_locked = Button_Image(screen=self._slave,
                                        x=261,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.nivel_bloqueado,
                                        onclick_param="nivel_dos",
                                        path_image=r"BTN\n2_blocked.jpg")
        
        self._btn_level_3 = Button_Image(screen=self._slave,
                                        x=481,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.entrar_nivel,
                                        onclick_param="nivel_tres",
                                        path_image=r"BTN\n3.jpg")
        
        self._btn_level_3_locked = Button_Image(screen=self._slave,
                                        x=481,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=179,
                                        h=250,
                                        onclick = self.nivel_bloqueado,
                                        onclick_param="nivel_tres",
                                        path_image=r"BTN\n3_blocked.jpg")
        
        self._btn_home = Button_Image(screen=self._slave,
                                    master_x=x,
                                    master_y=y,
                                    x=325,
                                    y=320,
                                    w=50,
                                    h=50,
                                    color_background=(255,0,0),
                                    color_border=(255,0,255),
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    path_image=r"BTN\Home.png")
        
        if self.jugador["nivel_1_desbloqueado"] == 1 and self.jugador["nivel_2_desbloqueado"] == 0 and self.jugador["nivel_3_desbloqueado"] == 0:
            self.lista_widgets.append(self._btn_level_1)
            self.lista_widgets.append(self._btn_level_2_locked)
            self.lista_widgets.append(self._btn_level_3_locked)
        elif self.jugador["nivel_1_desbloqueado"] == 1 and self.jugador["nivel_2_desbloqueado"] == 1 and self.jugador["nivel_3_desbloqueado"] == 0:
            self.lista_widgets.append(self._btn_level_1)
            self.lista_widgets.append(self._btn_level_2)
            self.lista_widgets.append(self._btn_level_3_locked)
        elif self.jugador["nivel_1_desbloqueado"] == 1 and self.jugador["nivel_2_desbloqueado"] == 1 and self.jugador["nivel_3_desbloqueado"] == 1:
            self.lista_widgets.append(self._btn_level_1)
            self.lista_widgets.append(self._btn_level_2)
            self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        
    def on(self,parametro):
        print("hola",parametro) 
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
            
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContendorNivel(self._master,nivel)

        self.show_dialog(form_contenedor_nivel)
        
    def btn_home_click(self,param):
        self.end_dialog()

    def nivel_bloqueado(self, param):
        print("Nivel bloqueado")
