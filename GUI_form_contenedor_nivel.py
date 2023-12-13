import pygame
from pygame.locals import*

from UI.GUI_form import*
from UI.GUI_button_image import*
from GUI_form_menu_pausa import FormMenuPausa

class FormContendorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width() ,pantalla.get_height() , color_background = "Black")
        nivel._slave = self._slave
        self.nivel = nivel
        print(self.nivel.nivel_actual)
        self._btn_home = Button_Image(screen = self._slave,
                                    master_x = self._x,
                                    master_y = self._y,
                                    x = self._w - 50,
                                    y = self._h - 50,
                                    w = 35,
                                    h = 35,
                                    color_background = (255,0,0),
                                    color_border = (255,0,255),
                                    onclick=self.btn_home_click,
                                    onclick_param = "",
                                    path_image = r"BTN\Home.png")

        self._btn_reset = Button_Image(screen = self._slave,
                                    master_x = self._x,
                                    master_y = self._y,
                                    x = self._w - 100,
                                    y = self._h - 50,
                                    w = 35,
                                    h = 35,
                                    color_background = (255,0,0),
                                    color_border = (255,0,255),
                                    onclick=self.btn_reset_click,
                                    onclick_param = "",
                                    path_image = r"BTN\Repeat.png")
        
        # self._btn_pause = Button_Image(screen = self._slave,
        #                             master_x = self._x,
        #                             master_y = self._y,
        #                             x = self._w - 100,
        #                             y = self._h - 50,
        #                             w = 35,
        #                             h = 35,
        #                             color_background = (255,0,0),
        #                             color_border = (255,0,255),
        #                             onclick=self.btn_pause_click,
        #                             onclick_param = "",
        #                             path_image = r"BTN\Pause.png")
        
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_reset)
        # self.lista_widgets.append(self._btn_pause)

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        
    def btn_home_click(self,param):
        self.end_dialog()


    def btn_reset_click(self, param):
        self.nivel.reiniciar_nivel()

    # def btn_pause_click(self, param):
    #     try:
    #         form_pausa = FormMenuPausa(screen=self._slave,
    #                                     x=0,
    #                                     y=0,
    #                                     w = 1366,
    #                                     h = 768,
    #                                     color_background=(0,0,0),
    #                                     color_border= "Black",
    #                                     active=True,
    #                                     path_image="BTN\pause_f.jpg")
    #         self.show_dialog(form_pausa)
    #         print("pausa")
    #     except Exception as e:
    #         print(f"Error: {e}")