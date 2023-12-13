import pygame
from pygame.locals import *
from configuraciones import *
from Funciones_bd import *
from UI.GUI_button import *
from UI.GUI_slider import *
from UI.GUI_textbox import *
from UI.GUI_label import *
from UI.GUI_form import *
from UI.GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_menu_play import*


    
class FormPrueba(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)


        self.volumen = 0.05
        self.flag_play = True
        self.fondo = pygame.image.load(r"Todoroki sprites\fallen-city-s.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (1820,980))
        self.screen = screen
        
        self.tabla_puntaje = crear_base_de_datos()

        self.bandera_pass_level = False
        self.guardar_nombre = False
        self.Nombre_Jugador = " "
        self.fuente = pygame.font.Font(r"Fuente\PixelifySans.ttf", 120)

        pygame.mixer.init()

        pygame.mixer.music.load(r"Musica\YouSayRun.mp3")

        pygame.mixer.music.set_volume(self.volumen)

        pygame.mixer.music.play(-1)

        self.txt_nombre = TextBox(self._slave,
                                x, y,
                                300, 150,
                                150, 30,
                                "Gray", "White", (32,42,212), "Blue",2,
                                font="Comic Sans", font_size=15, font_color= "Black")
        
        self.boton_play = Button(self._slave,
                                x, y,
                                25, 270,
                                100, 50,
                                (32,42,212), (32,42,212),
                                self.btn_play_click, "Nombre", "Pausa",
                                font= "Comic Sans", font_color= "Black", font_size= 15
                                )

        self.slider_volumen = Slider(self._slave,
                                    x, y,
                                    150, 290,
                                    200, 7,
                                    self.volumen,
                                    (32,42,212), "White"
                                    )

        self.label_volumen = Label(self._slave,
                                    380, 270,
                                    100, 50,
                                    "5%",
                                    "Comic Sans", 15, (32,42,212),
                                    r"BTN\BGRounded.png")
        
        self.label_puntuaciones = Label(self._slave,
                                    50, 150,
                                    100, 50,
                                    "Puntuaciones",
                                    "Comic Sans", 15, (32,42,212),
                                    "BTN\BGRounded.png")
        
        self.boton_score = Button_Image(self._slave,
                                        x, y,
                                        170, 150,
                                        50, 50,
                                        "BTN\Levels.png",
                                        self.btn_tabla_click, "")
        
        self.btn_jugar = Button_Image(self._slave,
                                        x, y,
                                        200, 30,
                                        120, 70,
                                        r"BTN\Colored Large Buttons\Play col_Button.png",
                                        self.btn_jugar_click, "")

        self.btn_guardar_nombre = Button(self._slave,
                                        x, y,
                                        300, 190,
                                        150, 30,
                                        (32,42,212), (32,42,212),
                                        self.btn_guardar_nombre_click,
                                        "Nombre", "Confirmar",
                                        font = "Comic Sans",
                                        font_size = 15,
                                        font_color = "black")
        
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        
        self.lista_widgets.append(self.boton_score)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.label_puntuaciones)

        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_guardar_nombre)
        self.render()

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.blitear_fondo()
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        
    
    def btn_play_click(self, param):
        if self.flag_play == True:
            pygame.mixer.music.pause()
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.boton_play._color_background = (32,42,212)
            self.boton_play.set_text("Pausa")
        self.flag_play = not self.flag_play
        
    
    def btn_tabla_click(self, param):
        # diccionario = [{"Jugador":"Gio", "Score":5},
        #                 {"Jugador":"Marcos", "Score":7},
        #                 {"Jugador":"Lucas", "Score":3}]
        diccionario = ordenar_datos_de_bd()


        nuevo_form = FormMenuScore(screen=self._master,
                                    x = 433,
                                    y = 210,
                                    w = 500,
                                    h = 500,
                                    color_background = (220,0,220),
                                    color_border = "Black",
                                    active = True,
                                    path_image = "BTN\PanelBig.png",
                                    scoreboard = diccionario,
                                    margen_x = 10,
                                    margen_y = 100,
                                    espacio = 10)
        
        self.show_dialog(nuevo_form)

    def btn_jugar_click(self,param):
        try:
            form_jugar = FormMenuPlay(screen=self._master,
                        x=333,
                        y=220,
                        w = 700,
                        h = 400,
                        color_background=(220,0,220),
                        color_border= "Black",
                        active=True,
                        path_image="BTN\BGRounded.png")
            self.show_dialog(form_jugar)
        except IndexError as e:
            print(f"Para jugar debe registrar un nombre, error: {e}")

    def blitear_fondo(self):
        texto_renderizado = self.fuente.render(f"Todoroki's Battle", True, "black")
        self.screen.blit(self.fondo, (0,0))
        self.screen.blit(texto_renderizado, (180, 80))

    def btn_guardar_nombre_click(self, param):
        nombre_jugador = self.txt_nombre.get_text()
        try:
            insertar_datos_en_db(nombre_jugador,"0","0","0","0")
            self.btn_guardar_nombre.set_text("Confirmado")
            self.btn_guardar_nombre._font_color = "Black"
            self.btn_guardar_nombre._color_background = "red"
            self.guardar_nombre = True
        except UnboundLocalError as e:
            print(f"Debe ingresar un nombre, error: {e}")