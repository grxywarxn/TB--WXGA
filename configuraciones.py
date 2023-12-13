import pygame
import sys
# from class_Plataforma import Plataforma
# from class_Plataforma_movil import Plataforma_movil
###############################################################


# def reescalar_imagenes(diccionario_animaciones, ancho, alto):
#     for lista in diccionario_animaciones:
#         for i in range(len(lista)):
#             img = lista[i]
#             lista[i] = pygame.transform.scale(img, (ancho, alto))

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        img = pygame.transform.flip(imagen, flip_x, flip_y)
        lista_girada.append(img)
    return lista_girada


def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 15)

    return diccionario


def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave, lista in diccionario_animaciones.items():  # Utiliza .items() para iterar a través del diccionario.
        for i in range(len(lista)):
            img = lista[i]
            if isinstance(img, pygame.surface.Surface):  # Verifica si img es un objeto Surface.
                lista[i] = pygame.transform.scale(img, (ancho, alto))
            else:
                print(f"Advertencia: La imagen {i} en la animación {clave} no es un objeto Surface.")

###############################################################

st_idle_r = [pygame.image.load(r"Todoroki sprites\idle_right_0.png"),
            pygame.image.load(r"Todoroki sprites\idle_right_1.png"),
            pygame.image.load(r"Todoroki sprites\idle_right_2.png"),
            pygame.image.load(r"Todoroki sprites\idle_right_3.png")]

st_idle_l = [pygame.image.load(r"Todoroki sprites\idle_left_0.png"),
            pygame.image.load(r"Todoroki sprites\idle_left_1.png"),
            pygame.image.load(r"Todoroki sprites\idle_left_2.png"),
            pygame.image.load(r"Todoroki sprites\idle_left_3.png")]

st_run_r = [pygame.image.load(r"Todoroki sprites\run_right_0.png"),
            pygame.image.load(r"Todoroki sprites\run_right_1.png"),
            pygame.image.load(r"Todoroki sprites\run_right_2.png"),
            pygame.image.load(r"Todoroki sprites\run_right_3.png"),
            pygame.image.load(r"Todoroki sprites\run_right_4.png"),
            pygame.image.load(r"Todoroki sprites\run_right_5.png")]

st_run_l = [pygame.image.load(r"Todoroki sprites\run_left_0.png"),
            pygame.image.load(r"Todoroki sprites\run_left_1.png"),
            pygame.image.load(r"Todoroki sprites\run_left_2.png"),
            pygame.image.load(r"Todoroki sprites\run_left_3.png"),
            pygame.image.load(r"Todoroki sprites\run_left_4.png"),
            pygame.image.load(r"Todoroki sprites\run_left_5.png")]

st_jump_r = [pygame.image.load(r"Todoroki sprites\jump_right_2.png")]

st_fall_r = [pygame.image.load(r"Todoroki sprites\jump_right_3.png")]

st_jump_l = [pygame.image.load(r"Todoroki sprites\jump_left_2.png")]

st_fall_l = [pygame.image.load(r"Todoroki sprites\jump_left_3.png")]

st_punch_r = [pygame.image.load(r"Todoroki sprites\punch_right_0.png"),
            pygame.image.load(r"Todoroki sprites\punch_right_1.png"),
            pygame.image.load(r"Todoroki sprites\punch_right_2.png"),
            pygame.image.load(r"Todoroki sprites\punch_right_3.png")]

st_punch_l = [pygame.image.load(r"Todoroki sprites\punch_left_0.png"),
            pygame.image.load(r"Todoroki sprites\punch_left_1.png"),
            pygame.image.load(r"Todoroki sprites\punch_left_2.png"),
            pygame.image.load(r"Todoroki sprites\punch_left_3.png")]

st_take_dmg_r = [pygame.image.load(r"Todoroki sprites\take_damage_right_0.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_right_1.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_right_2.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_right_3.png")]

st_take_dmg_l = [pygame.image.load(r"Todoroki sprites\take_damage_left_0.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_left_1.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_left_2.png"),
                pygame.image.load(r"Todoroki sprites\take_damage_left_3.png"),]

st_shoot_r = [pygame.image.load(r"Todoroki sprites\shoot_0.png"),
            pygame.image.load(r"Todoroki sprites\shoot_1.png"),
            pygame.image.load(r"Todoroki sprites\shoot_2.png"),
            pygame.image.load(r"Todoroki sprites\shoot_3.png"),
            pygame.image.load(r"Todoroki sprites\shoot_4.png"),
            pygame.image.load(r"Todoroki sprites\shoot_5.png"),
            pygame.image.load(r"Todoroki sprites\shoot_6.png"),
            pygame.image.load(r"Todoroki sprites\shoot_7.png"),
            pygame.image.load(r"Todoroki sprites\shoot_8.png"),
            pygame.image.load(r"Todoroki sprites\shoot_9.png")]

st_shoot_l = [pygame.image.load(r"Todoroki sprites\shoot_l_0.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_1.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_2.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_3.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_4.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_5.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_6.png"),
            pygame.image.load(r"Todoroki sprites\shoot_l_7.png")]

animaciones_st = {}

animaciones_st["Idle_r"] = st_idle_r
animaciones_st["Idle_l"] = st_idle_l
animaciones_st["Run_r"] = st_run_r
animaciones_st["Run_l"] = st_run_l
animaciones_st["Jump_r"] = st_jump_r
animaciones_st["Fall_r"] = st_fall_r
animaciones_st["Jump_l"] = st_jump_l
animaciones_st["Fall_l"] = st_fall_l
animaciones_st["Punch_r"] = st_punch_r
animaciones_st["Punch_l"] = st_punch_l
animaciones_st["Take_dmg_r"] = st_take_dmg_r
animaciones_st["Take_dmg_l"] = st_take_dmg_l
animaciones_st["Shoot_r"] = st_shoot_r
animaciones_st["Shoot_l"] = st_shoot_l

# print(animaciones_st)

###############################################################

nomu_idle_r =  [pygame.image.load(r"Nomu sprites\idle_0.png"),
                pygame.image.load(r"Nomu sprites\idle_1.png"),
                pygame.image.load(r"Nomu sprites\idle_2.png"),
                pygame.image.load(r"Nomu sprites\idle_3.png"),
                pygame.image.load(r"Nomu sprites\idle_4.png"),
                pygame.image.load(r"Nomu sprites\idle_5.png"),
                pygame.image.load(r"Nomu sprites\idle_6.png"),
                pygame.image.load(r"Nomu sprites\idle_7.png")]

nomu_idle_l = girar_imagenes(nomu_idle_r, True, False)

nomu_walk_r =  [pygame.image.load(r"Nomu sprites\walk_r_0.png"),
                pygame.image.load(r"Nomu sprites\walk_r_1.png"),
                pygame.image.load(r"Nomu sprites\walk_r_2.png"),
                pygame.image.load(r"Nomu sprites\walk_r_3.png"),
                pygame.image.load(r"Nomu sprites\walk_r_4.png"),
                pygame.image.load(r"Nomu sprites\walk_r_5.png"),
                pygame.image.load(r"Nomu sprites\walk_r_6.png"),
                pygame.image.load(r"Nomu sprites\walk_r_7.png"),
                pygame.image.load(r"Nomu sprites\walk_r_8.png"),
                pygame.image.load(r"Nomu sprites\walk_r_9.png"),
                pygame.image.load(r"Nomu sprites\walk_r_10.png"),
                pygame.image.load(r"Nomu sprites\walk_r_11.png"),
                pygame.image.load(r"Nomu sprites\walk_r_12.png"),
                pygame.image.load(r"Nomu sprites\walk_r_13.png"),
                pygame.image.load(r"Nomu sprites\walk_r_14.png"),
                pygame.image.load(r"Nomu sprites\walk_r_15.png")]

nomu_walk_l = girar_imagenes(nomu_walk_r, True, False)


nomu_attack_r =  [pygame.image.load(r"Nomu sprites\punch_rain_0.png"),
                pygame.image.load(r"Nomu sprites\punch_rain_1.png"),
                pygame.image.load(r"Nomu sprites\punch_rain_2.png"),
                pygame.image.load(r"Nomu sprites\punch_rain_3.png"),
                pygame.image.load(r"Nomu sprites\punch_rain_4.png")]

nomu_attack_l = girar_imagenes(nomu_attack_r, True, False)

nomu_fall_down_r  =  [pygame.image.load(r"Nomu sprites\fall_down_0.png"),
                    pygame.image.load(r"Nomu sprites\fall_down_1.png"),
                    pygame.image.load(r"Nomu sprites\fall_down_2.png"),
                    pygame.image.load(r"Nomu sprites\fall_down_3.png"),
                    pygame.image.load(r"Nomu sprites\fall_down_4.png"),
                    pygame.image.load(r"Nomu sprites\fall_down_5.png")]

nomu_fall_down_l = girar_imagenes(nomu_fall_down_r, True, False)

animaciones_nomu = {}

animaciones_nomu["Idle_r"] = nomu_idle_r
animaciones_nomu["Idle_l"] = nomu_idle_l
animaciones_nomu["Walk_r"] = nomu_walk_r
animaciones_nomu["Walk_l"] = nomu_walk_l
animaciones_nomu["Attack_r"] = nomu_attack_r
animaciones_nomu["Attack_l"] = nomu_attack_l
animaciones_nomu["Fall_down_r"] = nomu_fall_down_r
animaciones_nomu["Fall_down_l"] = nomu_fall_down_l

saw_trap = [pygame.image.load(r"Trap sprites\rotating_saw_01.png"),
            pygame.image.load(r"Trap sprites\rotating_saw_02.png"),
            pygame.image.load(r"Trap sprites\rotating_saw_03.png"),
            pygame.image.load(r"Trap sprites\rotating_saw_04.png"),
            pygame.image.load(r"Trap sprites\rotating_saw_05.png"),
            pygame.image.load(r"Trap sprites\rotating_saw_06.png")]

fuego_piso  =  [pygame.image.load(r"Dabi sprites\piso\fuego_0.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_1.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_2.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_3.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_4.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_5.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_6.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_7.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_8.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_9.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_10.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_11.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_12.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_13.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_14.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_15.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_16.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_17.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_18.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_19.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_20.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_21.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_22.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_23.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_24.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_25.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_26.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_27.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_28.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_29.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_30.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_31.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_32.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_33.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_34.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_35.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_36.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_37.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_38.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_39.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_40.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_41.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_42.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_43.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_44.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_45.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_46.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_47.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_48.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_49.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_50.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_51.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_52.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_53.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_54.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_55.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_56.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_57.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_58.png"),
                pygame.image.load(r"Dabi sprites\piso\fuego_59.png")]



#######################################################################
#PLATAFORMAS

plat_img = pygame.image.load(r"lvl sprites\145.png")
piso_img = pygame.image.load(r"lvl sprites\Piso.png")
piso_s_img = pygame.image.load(r"lvl sprites\207.png")
caja_img = pygame.image.load(r"lvl sprites\Crate_d.png")

#######################################################################
#TRAMPAS

portal_open = [pygame.image.load(r"lvl sprites\open_1.png"),
                pygame.image.load(r"lvl sprites\open_2.png"),
                pygame.image.load(r"lvl sprites\open_3.png"),
                pygame.image.load(r"lvl sprites\open_4.png"),
                pygame.image.load(r"lvl sprites\open_5.png"),
                pygame.image.load(r"lvl sprites\open_6.png"),
                pygame.image.load(r"lvl sprites\open_7.png"),
                pygame.image.load(r"lvl sprites\open_8.png")]

portal_idle = [pygame.image.load(r"lvl sprites\Idle_1.png"),
                pygame.image.load(r"lvl sprites\Idle_2.png"),
                pygame.image.load(r"lvl sprites\Idle_3.png"),
                pygame.image.load(r"lvl sprites\Idle_4.png"),
                pygame.image.load(r"lvl sprites\Idle_5.png"),
                pygame.image.load(r"lvl sprites\Idle_6.png"),
                pygame.image.load(r"lvl sprites\Idle_7.png"),
                pygame.image.load(r"lvl sprites\Idle_8.png")]

portal_animaciones = {}
portal_animaciones["Abrir"] = portal_open
portal_animaciones["Idle"] = portal_idle

trap_animaciones = {}
trap_animaciones["Saw"] = saw_trap
trap_animaciones["Fuego"] = fuego_piso
#######################################################################
#ITEMS

heart = pygame.image.load(r"Items_sprites\Full_heart.png")

ice_ball = pygame.image.load(r"Items_sprites\balls_0.png")

fire_ball = pygame.image.load(r"Items_sprites\balls_1.png")

speed_boost = pygame.image.load(r"Items_sprites\bolt_5.png")

bonus_gem = pygame.image.load(r"Items_sprites\gem_0.png")

#######################################################################
#DISPARO

fireball = [pygame.image.load(r"Todoroki sprites\fire_ball_0.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_1.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_2.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_3.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_4.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_5.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_6.png"),
            pygame.image.load(r"Todoroki sprites\fire_ball_7.png")]

fireball_l = girar_imagenes(fireball, True, False)


ice_spike = [pygame.image.load(r"Todoroki sprites\ice_spike_0.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_1.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_2.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_3.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_4.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_5.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_6.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_7.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_8.png"),
            pygame.image.load(r"Todoroki sprites\ice_spike_9.png"),]

ice_spike_l = girar_imagenes(ice_spike, True, False)

disparos_fuego = {}
disparos_fuego["Fuego"] = fireball
disparos_fuego["Fuego_l"] = fireball_l

disparos_hielo = {}
disparos_hielo["Hielo"] = ice_spike
disparos_hielo["Hielo_l"] = ice_spike_l

dark_wave_r = [pygame.image.load(r"Nomu sprites\dark_power_0.png"),
            pygame.image.load(r"Nomu sprites\dark_power_1.png"),
            pygame.image.load(r"Nomu sprites\dark_power_2.png"),
            pygame.image.load(r"Nomu sprites\dark_power_3.png"),
            pygame.image.load(r"Nomu sprites\dark_power_4.png"),
            pygame.image.load(r"Nomu sprites\dark_power_5.png")]

dark_wave_l = girar_imagenes(dark_wave_r, True, False)

firewall_r = [pygame.image.load(r"Nomu sprites\fire_wall_0.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_1.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_2.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_3.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_4.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_5.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_6.png"),
            pygame.image.load(r"Nomu sprites\fire_wall_7.png")]

firewall_l = girar_imagenes(firewall_r, True, False)

disparos_wave = {}
disparos_wave["Wave_r"] = dark_wave_r
disparos_wave["Wave_l"] = dark_wave_l

disparos_firewall = {}
disparos_firewall["Firewall_r"] = firewall_r
disparos_firewall["Firewall_l"] = firewall_l

#####################################################################################
vidas = [pygame.image.load(r"Items_sprites\0_vidas.png"),
        pygame.image.load(r"Items_sprites\1_vidas.png"),
        pygame.image.load(r"Items_sprites\2_vidas.png"),
        pygame.image.load(r"Items_sprites\3_vidas.png"),
        pygame.image.load(r"Items_sprites\4_vidas.png"),
        pygame.image.load(r"Items_sprites\5_vidas.png")]

vidas_boss  =  [pygame.image.load(r"Dabi sprites\boss_0_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_1_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_2_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_3_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_4_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_5_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_6_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_7_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_8_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_9_vida.png"),
                pygame.image.load(r"Dabi sprites\boss_10_vida.png")]

#####################################################################################
explosion = [pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_0.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_1.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_2.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_3.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_4.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_5.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_6.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_7.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_8.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_9.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_10.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_11.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\explosion_12.png")]

fire_punch  =  [pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_0.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_1.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_2.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_3.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_4.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_5.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_6.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_7.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_8.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_9.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_10.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_11.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_12.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_13.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_14.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_15.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_16.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_17.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_18.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_19.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_20.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_21.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_22.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_23.png"),
                pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_punch_24.png")]

flame = [pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_0.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_1.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_2.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_3.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_4.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_5.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_6.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_7.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_8.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_9.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_10.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_11.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flame_12.png")]

zap  = [pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_0.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_1.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_2.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_3.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_4.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_5.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\zap_6.png")]

tornado =  [pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_0.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_1.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_2.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_3.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_4.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_5.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_6.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_7.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_8.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_9.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_10.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_11.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_12.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_13.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_14.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_15.png"),
            pygame.image.load(r"Dabi sprites\Dabi_attacks\tornado_16.png")]

tornado_l = girar_imagenes(tornado, True, False)

flash = [pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_0.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_1.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_2.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_3.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_4.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_5.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\flash_6.png")]

animaciones_ataque_dabi = {}
animaciones_ataque_dabi["Explosion"] = explosion
animaciones_ataque_dabi["Punch"] = fire_punch
animaciones_ataque_dabi["Flame"] = flame
animaciones_ataque_dabi["Zap"] = zap
animaciones_ataque_dabi["Tornado"] = tornado_l
animaciones_ataque_dabi["Flash"] = flash

# dt_teleport = [pygame.image.load(r"Dabi sprites\teleport_0.png"),
#             pygame.image.load(r"Dabi sprites\teleport_1.png"),
#             pygame.image.load(r"Dabi sprites\teleport_2.png"),
#             pygame.image.load(r"Dabi sprites\teleport_3.png"),
#             pygame.image.load(r"Dabi sprites\teleport_4.png"),
#             pygame.image.load(r"Dabi sprites\teleport_5.png"),
#             pygame.image.load(r"Dabi sprites\teleport_6.png"),
#             pygame.image.load(r"Dabi sprites\teleport_7.png")]

dt_teleport_r = [pygame.image.load(r"Dabi sprites\teleport_0.png"),
            pygame.image.load(r"Dabi sprites\teleport_1.png"),
            pygame.image.load(r"Dabi sprites\teleport_2.png"),
            pygame.image.load(r"Dabi sprites\teleport_3.png"),
            pygame.image.load(r"Dabi sprites\teleport_4.png"),
            pygame.image.load(r"Dabi sprites\teleport_5.png"),
            pygame.image.load(r"Dabi sprites\teleport_6.png"),
            pygame.image.load(r"Dabi sprites\teleport_7.png"),
            pygame.image.load(r"Dabi sprites\cast_0.png"),
            pygame.image.load(r"Dabi sprites\cast_1.png"),
            pygame.image.load(r"Dabi sprites\cast_2.png"),
            pygame.image.load(r"Dabi sprites\cast_3.png"),
            pygame.image.load(r"Dabi sprites\cast_4.png")]

dt_idle_r = [pygame.image.load(r"Dabi sprites\Idle_0.png"),
            pygame.image.load(r"Dabi sprites\Idle_1.png"),
            pygame.image.load(r"Dabi sprites\Idle_2.png")] 

dt_idle_l = girar_imagenes(dt_idle_r, True, False)

dt_run_r = [pygame.image.load(r"Dabi sprites\run_0.png"),
            pygame.image.load(r"Dabi sprites\run_1.png"),
            pygame.image.load(r"Dabi sprites\run_2.png")]

dt_run_l = girar_imagenes(dt_run_r, True, False)

dt_cast_r = [pygame.image.load(r"Dabi sprites\cast_0.png"),
            pygame.image.load(r"Dabi sprites\cast_0.png"),
            pygame.image.load(r"Dabi sprites\cast_1.png"),
            pygame.image.load(r"Dabi sprites\cast_1.png"),
            pygame.image.load(r"Dabi sprites\cast_2.png"),
            pygame.image.load(r"Dabi sprites\cast_2.png"),
            pygame.image.load(r"Dabi sprites\cast_3.png"),
            pygame.image.load(r"Dabi sprites\cast_3.png"),
            pygame.image.load(r"Dabi sprites\cast_4.png"),
            pygame.image.load(r"Dabi sprites\cast_4.png")]

dt_cast_l = girar_imagenes(dt_cast_r, True, False)

dt_cast_ex_r = [pygame.image.load(r"Dabi sprites\cast_expl_0.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_0.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_0.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_0.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_1.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_1.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_1.png"),
                pygame.image.load(r"Dabi sprites\cast_expl_1.png")]

dt_cast_ex_l = girar_imagenes(dt_cast_ex_r, True, False)

dt_shoot_r  =  [pygame.image.load(r"Dabi sprites\shoot_0.png"),
                pygame.image.load(r"Dabi sprites\shoot_1.png"),
                pygame.image.load(r"Dabi sprites\shoot_2.png")]

dt_shoot_l = girar_imagenes(dt_shoot_r, True, False)

dt_wait_r = [pygame.image.load(r"Dabi sprites\wait_0.png"),
            pygame.image.load(r"Dabi sprites\wait_1.png")]

dt_wait_l = girar_imagenes(dt_wait_r, True, False)
dt_teleport = girar_imagenes(dt_teleport_r, True, False)

dt_animaciones = {}
dt_animaciones["Idle_r"] = dt_idle_r
dt_animaciones["Idle_l"] = dt_idle_l
dt_animaciones["Run_r"] = dt_run_r
dt_animaciones["Run_l"] = dt_run_l
dt_animaciones["Wait_r"] = dt_wait_r
dt_animaciones["Wait_l"] = dt_wait_l
dt_animaciones["Shoot_r"] = dt_shoot_r
dt_animaciones["Shoot_l"] = dt_shoot_l
dt_animaciones["Cast_r"] = dt_cast_r
dt_animaciones["Cast_l"] = dt_cast_l
dt_animaciones["Cast_ex_r"] = dt_cast_ex_r
dt_animaciones["Cast_ex_l"] = dt_cast_ex_l
dt_animaciones["Teleport"] = dt_teleport

flama = [pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_0.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_1.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_2.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_3.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_4.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_5.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_6.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_7.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_8.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_9.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_10.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_11.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_12.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_13.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_14.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_15.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_16.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_17.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_18.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_19.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_20.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_21.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_22.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_23.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_24.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_25.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_26.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_27.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_28.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_29.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_30.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_31.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_32.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_33.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_34.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_35.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_36.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_37.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_38.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_39.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_40.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_41.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_42.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_43.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_44.png"),
        pygame.image.load(r"Dabi sprites\Dabi_attacks\fire_rain_45.png")]

animaciones_lluvia = {}
animaciones_lluvia["Flama"] = flama
