from configuraciones import *
class Disparo:
    def __init__(self, pos_x, pos_y, que_hace, direccion, elemento):

        self.animaciones_hielo = disparos_hielo
        reescalar_imagenes(disparos_hielo, 36,50)
        self.rect_p_hielo = self.animaciones_hielo["Hielo"][0].get_rect()

        self.animaciones_fuego = disparos_fuego
        reescalar_imagenes(disparos_fuego, 20,20)
        self.rect_p_fuego = self.animaciones_fuego["Fuego"][0].get_rect()

        self.contador_pasos = 0
        # self.animacion_actual = None
        self.rect_p_fuego.x = pos_x
        self.rect_p_fuego.centery = pos_y
        self.rect_p_hielo.x = pos_x
        self.rect_p_hielo.centery = pos_y
        self.que_hace = que_hace
        self.direccion = direccion
        self.elemento = elemento
        self.colision = False

        if self.elemento == "Hielo":
            self.rect_principal = self.rect_p_hielo
            self.animacion_actual = self.animaciones_hielo["Hielo"]
        else:
            self.rect_principal = self.rect_p_fuego
            self.animacion_actual = self.animaciones_fuego["Fuego"]


    def animar(self, pantalla):
        if self.colision == False:
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
            self.contador_pasos += 1

    def actualizar(self):
        if self.elemento == "Hielo":
            if (self.que_hace == "Derecha" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "Saltando") and self.direccion == "Derecha":
                self.animacion_actual = self.animaciones_hielo["Hielo"]

                self.rect_p_hielo.x += 15
            elif (self.que_hace == "Izquierda" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "Saltando") and self.direccion == "Izquierda":
                self.rect_p_hielo.x -= 15
                self.animacion_actual = self.animaciones_hielo["Hielo_l"]
        else:
            if (self.que_hace == "Derecha" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "Saltando") and self.direccion == "Derecha":
                self.animacion_actual = self.animaciones_fuego["Fuego"]
                self.rect_p_fuego.x += 30
            elif (self.que_hace == "Izquierda" or self.que_hace == "Quieto" or self.que_hace == "Dispara" or self.que_hace == "Saltando") and self.direccion == "Izquierda":
                self.rect_p_fuego.x -= 30
                self.animacion_actual = self.animaciones_fuego["Fuego_l"]