from configuraciones import *

class Disparo_enemigo:
    def __init__(self, pos_x, pos_y, direccion):

        self.animaciones_wave = disparos_wave
        reescalar_imagenes(disparos_wave, 30,50)
        self.rect_p_wave = self.animaciones_wave["Wave_r"][0].get_rect()

        self.animaciones_firewall = disparos_firewall
        reescalar_imagenes(disparos_firewall, 50,30)
        self.rect_p_firewall = self.animaciones_firewall["Firewall_l"][0].get_rect()

        self.contador_pasos = 0
        self.rect_p_firewall.x = pos_x
        self.rect_p_firewall.centery = pos_y
        self.rect_p_wave.x = pos_x
        self.rect_p_wave.centery = pos_y

        self.direccion = direccion

        self.colision = False

        if self.direccion == "Derecha":
            self.rect_principal = self.rect_p_wave
            self.animacion_actual = self.animaciones_wave["Wave_r"]
        else:
            self.rect_principal = self.rect_p_firewall
            self.animacion_actual = self.animaciones_firewall["Firewall_r"]


    def animar(self, pantalla):
        if self.colision == False:
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rect_principal)
            self.contador_pasos += 1

    def actualizar(self):
        if self.direccion == "Derecha":
            self.rect_p_wave.x += 10
            self.animacion_actual = self.animaciones_wave["Wave_r"]
        else:
            self.rect_p_firewall.x -= 10
            self.animacion_actual = self.animaciones_firewall["Firewall_l"]