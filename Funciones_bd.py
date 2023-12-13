import re
import sqlite3
import json


def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip()
    if re.search(r"-", numero_str):
        retorno = -2
    elif re.search(r"\d", numero_str):
        numero_int = int(numero_str)
        retorno = numero_int
    elif re.search(r"[a-zA-Z]", numero_str):
        retorno = -1
    else:
        retorno = -3
    return retorno

def sanitizar_string(valor_str: str):
    if len(valor_str) > 0:
        if re.search(r"[a-zA-Z]+", valor_str):
            retorno = valor_str.capitalize()
        else:
            retorno = "N/A"
    return retorno


def crear_base_de_datos():
    tabla_puntaje_creada = False
    with sqlite3.connect("tabla_puntos.db") as conexion:
        try:
            sentencia = '''
                        CREATE TABLE IF NOT EXISTS Leaderboard
                        (
                            nombre TEXT,
                            score_lvl_1 INTEGER,
                            score_lvl_2 INTEGER,
                            score_lvl_3 INTEGER,
                            score_total INTEGER,
                            nivel_1_desbloqueado BOOLEAN,
                            nivel_2_desbloqueado BOOLEAN,
                            nivel_3_desbloqueado BOOLEAN
                        )
                        '''
            conexion.execute(sentencia)
            print("Base de datos creada")

            # conexion.execute("INSERT OR IGNORE INTO Leaderboard (nombre, nivel_1_desbloqueado, nivel_2_desbloqueado, nivel_3_desbloqueado) VALUES (?, 1, 0, 0)",)

            tabla_puntaje_creada = True
        except sqlite3.Error as e:
            print(f"La base de datos ya ha sido creada anteriormente")

    return tabla_puntaje_creada


def verificar_nombre_en_bd(nombre_jugador, lista_jugadores):
    if lista_jugadores:
        for jugador in lista_jugadores:
            if nombre_jugador == jugador["nombre"]:
                print("Error, ese nombre ya está en la base de datos.")
                return True

        print("No está en la lista.")
        return False
    else:
        print("Lista no encontrada.")
        return False

def insertar_datos_en_db(nombre, score_lvl_1, score_lvl_2, score_lvl_3, score_total):
    nombre_confirmado = sanitizar_string(nombre)
    score_1 = sanitizar_entero(score_lvl_1)
    score_2 = sanitizar_entero(score_lvl_2)
    score_3 = sanitizar_entero(score_lvl_3)
    score_total = sanitizar_entero(score_total)
    lista_jugadores = leer_datos_de_bd()
    nombre_encontrado = verificar_nombre_en_bd(nombre_confirmado, lista_jugadores)

    if not nombre_encontrado:
        if nombre_confirmado != "N/A" and (score_1 >= 0 or score_2 >= 0 or score_3 >= 0):
            with sqlite3.connect("tabla_puntos.db") as conexion:
                try:
                    sentencia = '''
                    INSERT INTO Leaderboard (nombre, score_lvl_1, score_lvl_2, score_lvl_3, score_total, nivel_1_desbloqueado, nivel_2_desbloqueado, nivel_3_desbloqueado)
                    VALUES (?, ?, ?, ?, ?, 1, 0, 0)
                    '''
                    conexion.execute(sentencia, (nombre_confirmado, score_1, score_2, score_3, score_total))
                    print("Datos ingresados con éxito.")
                except Exception as e:
                    print(f"Error al insertar datos: {e}")
        else:
            print("Error al ingresar datos.")
    else:
        print("El nombre ya existe en la base de datos.")


def actualizar_datos_de_bd(nombre, nivel, score):
    with sqlite3.connect("tabla_puntos.db") as conexion:
        cursor = conexion.cursor()

        # Obtener el puntaje actual del nivel
        columna_score = f"score_lvl_{nivel}"
        cursor.execute(f"SELECT {columna_score} FROM Leaderboard WHERE nombre = ?", (nombre,))
        puntaje_actual = cursor.fetchone()

        if puntaje_actual is not None and puntaje_actual[0] < score:
            cursor.execute(f"UPDATE Leaderboard SET {columna_score} = ? WHERE nombre = ?", (score, nombre))

            cursor.execute("UPDATE Leaderboard SET score_total = score_lvl_1 + score_lvl_2 + score_lvl_3 WHERE nombre = ?", (nombre,))

            nivel_siguiente = nivel + 1

            if 1 <= nivel_siguiente <= 3:
                columna_desbloqueo = f"nivel_{nivel_siguiente}_desbloqueado"
                cursor.execute(f"SELECT {columna_desbloqueo} FROM Leaderboard WHERE nombre = ?", (nombre,))
                desbloqueo_actual = cursor.fetchone()

                if desbloqueo_actual is not None and desbloqueo_actual[0] == 0:
                    cursor.execute(f"UPDATE Leaderboard SET {columna_desbloqueo} = 1 WHERE nombre = ?", (nombre,))

                    conexion.commit()
                    print(f"Nivel {nivel_siguiente} desbloqueado para {nombre}")
                else:
                    print(f"No se desbloqueó el siguiente nivel para {nombre}")
        else:
            print(f"No se actualizó el puntaje del nivel {nivel} para {nombre}, puntaje record actual: {puntaje_actual[0] if puntaje_actual else None}")


def leer_datos_de_bd():
    lista_jugadores = []
    with sqlite3.connect("tabla_puntos.db") as conexion:
        try:
            sentencia = 'SELECT nombre, score_lvl_1, score_lvl_2, score_lvl_3, score_total, nivel_1_desbloqueado, nivel_2_desbloqueado, nivel_3_desbloqueado FROM Leaderboard'
            cursor = conexion.execute(sentencia)
            print("Datos ingresados con éxito.")
            for fila in cursor:
                jugador = {
                    "nombre": fila[0],
                    "score_lvl_1": fila[1],
                    "score_lvl_2": fila[2],
                    "score_lvl_3": fila[3],
                    "score_total": fila[4],
                    "nivel_1_desbloqueado": fila[5],
                    "nivel_2_desbloqueado": fila[6],
                    "nivel_3_desbloqueado": fila[7],
                }
                lista_jugadores.append(jugador)
        except sqlite3.Error as e:
            print(f"Error al leer datos: {e}")
    return lista_jugadores


# def leer_puntaje_total(nombre_jugador):
#     with sqlite3.connect("tabla_puntos.db") as conexion:
#         try:
#             sentencia = 'SELECT score_total FROM Leaderboard WHERE nombre = ?'
#             cursor = conexion.execute(sentencia, (nombre_jugador,))
#             print("Datos ingresados con éxito.")
#             fila = cursor.fetchone()
#             if fila:
#                 puntaje_total = fila[0]
#                 return puntaje_total
#             else:
#                 print(f"No se encontraron datos para el jugador {nombre_jugador}.")
#                 return None
#         except sqlite3.Error as e:
#             print(f"Error al leer datos: {e}")
#             return None

def ordenar_datos_de_bd():
    lista_jugadores = []
    with sqlite3.connect("tabla_puntos.db") as conexion:
        try:
            sentencia = 'SELECT nombre, score_total FROM Leaderboard ORDER BY score_total DESC LIMIT 3'
            cursor = conexion.execute(sentencia)
            for fila in cursor:
                jugador = {
                    "nombre": fila[0],
                    "score_total": fila[1]
                }
                lista_jugadores.append(jugador)
        except sqlite3.Error as e:
            print(f"Error al ordenar datos: {e}")
    return lista_jugadores