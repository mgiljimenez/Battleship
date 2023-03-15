import numpy as np
import pandas as pd
import random
from time import sleep
from battleship_config import usuario, maquina
from battleship_variables import TAM_TABLERO, TAM_BARCOS,barco_icon,agua_icon,shoot_icon,instrucciones


#Inicializamos a los dos jugadores
jugador_usuario=usuario(TAM_BARCOS,TAM_TABLERO,barco_icon)
jugador_maquina=maquina(TAM_BARCOS,TAM_TABLERO, barco_icon)

#Generamos los tres tableros necesarios para el juego
tablero_del_jugador=jugador_usuario.generar_tablero()
tablero_maquina=jugador_maquina.generar_tablero("maquina")
tablero_interactivo=jugador_maquina.generar_tablero("interactivo")

#Iniciamos el juego preguntando al usuario su nombre y mostrando las instrucciones
nombre_jugador=input("Bienvenido a Battleship. ¿Cuál es su nombre?:")
print(f"Bienvenido {nombre_jugador}!! A continuación te dejo las intrucciones. Mucha suerte!")
print(instrucciones)

#Comieza el juego (Explicar bien)
print("Tu tablero:")
print(tablero_del_jugador)
print("Tablero de la máquina")
print(tablero_interactivo)

while True:
    while True:
        turno_jugador=jugador_usuario.disparar(tablero_maquina,tablero_interactivo)
        if turno_jugador=="pierde_turno":
            break
        elif turno_jugador=="vuelve_tocar":
            continue
        elif turno_jugador=="barco":
            if jugador_usuario.comprobar_final(tablero_maquina)==False:
                break
            else:
                print("Vuelve a ser tu turno:")
                continue
        break
        
    while True:
        sleep(3)
        turno_maquina=disparo_de_maquina=jugador_maquina.disparar(tablero_del_jugador)
        if turno_maquina=="pierde_turno":
            break
        elif turno_maquina=="vuelve_tocar":
            continue
        elif turno_maquina=="barco":
            if jugador_maquina.comprobar_final(tablero_del_jugador)==True:
                print("Vuelve a tirar la máquina:")
                continue
            else:
                break
        break