import numpy as np
import pandas as pd
import random
from time import sleep
from battleship_config import usuario, maquina, mostrar_tablero
from IPython.display import display
from battleship_variables import TAM_TABLERO, TAM_BARCOS,barco_icon,agua_icon,shoot_icon,instrucciones


#Inicializamos a los dos jugadores
jugador_usuario=usuario(TAM_BARCOS,TAM_TABLERO,barco_icon)
jugador_maquina=maquina(TAM_BARCOS,TAM_TABLERO, barco_icon)

#Generamos los tres tableros necesarios para el juego
tablero_del_jugador=jugador_usuario.generar_tablero("jugador")
tablero_del_jugador_comprobar=jugador_usuario.generar_tablero("interactivo")
tablero_maquina=jugador_maquina.generar_tablero("maquina")
tablero_interactivo=jugador_maquina.generar_tablero("interactivo")


#Iniciamos el juego preguntando al usuario su nombre y mostrando las instrucciones
nombre_jugador=input("𝓑𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 𝓪 𝓗𝓾𝓷𝓭𝓲𝓻 𝓛𝓪 𝓕𝓵𝓸𝓽𝓪 ¿Cuál es su nombre?:")
print(f"""======================================================================================================================================
{nombre_jugador}, bienvenido al juego de Hundir la Flota!!""")
print(instrucciones)
tablero_mostrar=mostrar_tablero()


#Comieza el juego (Explicar bien)
print("Tu tablero:")
tablero_mostrar.mostrar(tablero_del_jugador)
# tablero_mostrar.mostrar(tablero_del_jugador)
print("Tablero de la máquina")
tablero_mostrar.mostrar(tablero_interactivo)

while True:
    while True:
        turno_jugador=jugador_usuario.disparar(tablero_maquina,tablero_interactivo)
        if turno_jugador=="pierde_turno":
            break
        elif turno_jugador=="vuelve_tocar":
            continue
        elif turno_jugador=="barco":
            if (tablero_maquina==tablero_interactivo).all():
                break
            else:
                print("Vuelve a ser tu turno:")
                continue
    if (tablero_maquina==tablero_interactivo).all():
        ganador="jugador"
        break
        
    while True:
        sleep(3)
        turno_maquina=disparo_de_maquina=jugador_maquina.disparar(tablero_del_jugador, tablero_del_jugador_comprobar)
        if turno_maquina=="pierde_turno":
            break
        elif turno_maquina=="vuelve_tocar":
            continue
        elif turno_maquina=="barco":
            if (tablero_del_jugador==tablero_del_jugador_comprobar).all():
                break
            else:
                print("La máquina vuelve a tirar:")
                continue
    if (tablero_del_jugador==tablero_del_jugador_comprobar).all():
        ganador="maquina"
        break

if ganador=="jugador":
    print(f"Enhorabuena {nombre_jugador}!! Has ganado la partida!!")
    print("Fin del juego")
elif ganador=="maquina":
    print(f"Ups {nombre_jugador}, has perdido.")
    print("Fin del juego")
