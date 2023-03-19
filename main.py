from time import sleep
from battleship_config import usuario, maquina, mostrar_tablero
from battleship_variables import TAM_TABLERO, TAM_BARCOS,barco_icon,agua_icon,shoot_icon,instrucciones



#Inicializamos a los dos jugadores
jugador_usuario=usuario(TAM_BARCOS,TAM_TABLERO,barco_icon)
jugador_maquina=maquina(TAM_BARCOS,TAM_TABLERO, barco_icon)

#Generamos los cuatro tableros necesarios para el juego
tablero_del_jugador=jugador_usuario.generar_tablero("jugador")
tablero_del_jugador_comprobar=jugador_usuario.generar_tablero("interactivo")
tablero_maquina=jugador_maquina.generar_tablero("maquina")
tablero_interactivo=jugador_maquina.generar_tablero("interactivo")


#Iniciamos el juego preguntando al usuario su nombre y mostrando las instrucciones
nombre_jugador=input("¿Cuál es tu nombre?   ")
print(f"""======================================================================================================================================
{nombre_jugador}, bienvenido al juego de Hundir la Flota!!""")
print(instrucciones)
tablero_mostrar=mostrar_tablero()
sleep(5)

#Mostramos por pantalla el tablero del jugador y el tablero de la máquina
print("ＴＵ Ｔ▲ＢＬＥＲＯ：")
tablero_mostrar.mostrar(tablero_del_jugador)
print("ＴΛＢＬΞＲＯ ＤΞ ＬΛ ＭÁＱＵＩＮΛ：")
tablero_mostrar.mostrar(tablero_interactivo)

#Inicializamos el bucle para que se repitan los disparos mientras que no termine el juego
while True:
    while True:
        #Este bucle se encarga del turno del jugador
        turno_jugador=jugador_usuario.disparar(tablero_maquina,tablero_interactivo)
        if turno_jugador=="pierde_turno":
            #Si ha disparado en agua pierde el turno y toca al oponente
            break
        elif turno_jugador=="vuelve_tocar":
            #Si dispara donde ya había disparado antes, se vuelve arriba del bucle, no se considera jugada válida
            continue
        elif turno_jugador=="barco":
            #Si dispara en un barco vuelve a ser su turno, siempre que no haya ganado y finalizado la partida
            if (tablero_maquina==tablero_interactivo).all():
                break
            else:
                print("Vuelve a ser tu turno:")
                continue
    if (tablero_maquina==tablero_interactivo).all():
        ganador="jugador"
        break
        
    while True:
        #Este bucle se encarga del turno de la máquina
        sleep(3)
        turno_maquina=disparo_de_maquina=jugador_maquina.disparar(tablero_del_jugador, tablero_del_jugador_comprobar)
        if turno_maquina=="pierde_turno":
            #Si ha disparado en agua pierde el turno y toca al oponente
            break
        elif turno_maquina=="vuelve_tocar":
            #Si dispara donde ya había disparado antes, se vuelve arriba del bucle, no se considera jugada válida
            continue
        elif turno_maquina=="barco":
            #Si dispara en un barco vuelve a ser su turno, siempre que no haya ganado y finalizado la partida
            if (tablero_del_jugador==tablero_del_jugador_comprobar).all():
                break
            else:
                print("La máquina vuelve a tirar:")
                continue
    if (tablero_del_jugador==tablero_del_jugador_comprobar).all():
        ganador="maquina"
        break
#Finalizamos el juego mostrando por pantalla quien ha sido el ganador
if ganador=="jugador":
    print(f"Enhorabuena {nombre_jugador}!! Has ganado la partida!!")
    print("F̵I̵N̵ ̵D̵E̵L̵ ̵J̵U̵E̵G̵O̵")
elif ganador=="maquina":
    print(f"Ups {nombre_jugador}, has perdido.")
    print("F̵I̵N̵ ̵D̵E̵L̵ ̵J̵U̵E̵G̵O̵")
