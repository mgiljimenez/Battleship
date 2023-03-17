import numpy as np
import pandas as pd
import random
from IPython.display import display
from battleship_variables import TAM_TABLERO, TAM_BARCOS, barco_icon, agua_icon, shoot_icon
class usuario:
    def __init__(self, TAM_BARCOS, TAM_TABLERO, barco_icon):
        self.TAM_BARCOS = TAM_BARCOS
        self.TAM_TABLERO = TAM_TABLERO
        self.barco_icon = barco_icon
    def generar_tablero(self, tipo):
        if tipo=="jugador":
            tablero_input=np.full((TAM_TABLERO, TAM_TABLERO), " ")
            barcos = []
            for tam_barco in self.TAM_BARCOS:
                colocado = False
                while not colocado:
                    import numpy
                    fila, col = numpy.random.randint(self.TAM_TABLERO), numpy.random.randint(self.TAM_TABLERO)
                    direccion = numpy.random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
                    if direccion == 'arriba':
                        posiciones = [(fila-i, col) for i in range(tam_barco)]
                    elif direccion == 'abajo':
                        posiciones = [(fila+i, col) for i in range(tam_barco)]
                    elif direccion == 'izquierda':
                        posiciones = [(fila, col-i) for i in range(tam_barco)]
                    else:
                        posiciones = [(fila, col+i) for i in range(tam_barco)]
                    if all(0<=fila<self.TAM_TABLERO and 0<=col<self.TAM_TABLERO and tablero_input[fila, col]==" " for fila, col in posiciones):
                        barco = {"tam": tam_barco, "posiciones": posiciones}
                        barcos.append(barco)
                        for fila, col in posiciones:
                            tablero_input[fila, col] = self.barco_icon[tam_barco]
                        colocado = True
            return tablero_input
        else:
            return np.full((TAM_TABLERO, TAM_TABLERO), " ")

    def disparar(self,tablero_maquina, tablero_interactivo):
        while True:
            try:
                fila = int(input("Ingrese la fila (número entre 0 y {}): ".format(TAM_TABLERO-1)))
                col = int(input("Ingrese la columna (número entre 0 y {}): ".format(TAM_TABLERO-1)))
                if (fila < 0 or fila >=(TAM_TABLERO)) or (col < 0 or col >= (TAM_TABLERO)):
                    print("Coordenadas fuera de rango. Inténtelo nuevamente")
                    continue
                else:
                    pass
            except ValueError:
                print("Inténtelo nuevamente")
                continue
            coordenada_disparo = tablero_maquina[fila][col]
            if (coordenada_disparo==agua_icon) or (coordenada_disparo==shoot_icon):
                print("Ya has disparado aquí. Vuelve a tirar")
                return("vuelve_tocar")
            elif coordenada_disparo == " ":
                print("¡Has disparado al agua!")
                tablero_maquina[fila][col] = agua_icon
                tablero_interactivo[fila][col] = agua_icon
                print(tablero_maquina)
                print(tablero_interactivo)
                return("pierde_turno")
            else:
                tablero_maquina[fila][col] = shoot_icon
                tablero_interactivo[fila][col] = shoot_icon
                print("¡Has disparado en un barco!")
                print(tablero_interactivo)
                return("barco")


class maquina:
    def __init__(self, TAM_BARCOS, TAM_TABLERO, barco_icon):
        self.TAM_BARCOS = TAM_BARCOS
        self.TAM_TABLERO = TAM_TABLERO
        self.barco_icon = barco_icon
    def generar_tablero(self, tipo):
        if tipo=="maquina":
            tablero_input=np.full((TAM_TABLERO, TAM_TABLERO), " ")
            barcos = []
            for tam_barco in self.TAM_BARCOS:
                colocado = False
                while not colocado:
                    import numpy
                    fila, col = numpy.random.randint(self.TAM_TABLERO), numpy.random.randint(self.TAM_TABLERO)
                    direccion = numpy.random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
                    if direccion == 'arriba':
                        posiciones = [(fila-i, col) for i in range(tam_barco)]
                    elif direccion == 'abajo':
                        posiciones = [(fila+i, col) for i in range(tam_barco)]
                    elif direccion == 'izquierda':
                        posiciones = [(fila, col-i) for i in range(tam_barco)]
                    else:
                        posiciones = [(fila, col+i) for i in range(tam_barco)]
                    if all(0<=fila<self.TAM_TABLERO and 0<=col<self.TAM_TABLERO and tablero_input[fila, col]==" " for fila, col in posiciones):
                        barco = {"tam": tam_barco, "posiciones": posiciones}
                        barcos.append(barco)
                        for fila, col in posiciones:
                            tablero_input[fila, col] = self.barco_icon[tam_barco]
                        colocado = True
            return tablero_input
        else:
            return np.full((TAM_TABLERO, TAM_TABLERO), " ")
    def disparar(self, tablero_del_jugador, tablero_del_jugador_comprobar):
        while True:
            fila=random.randint(0, 9) 
            columna=random.randint(0, 9)
            coordenada_disparo=tablero_del_jugador[fila][columna]
            #Defino la variable "terminar": tiene como objeto que si cambia a True significa que ha derrivado todos los objetivos
            #Por lo que puede finalizar el juego
            terminar=False
            if (coordenada_disparo==agua_icon) or (coordenada_disparo==shoot_icon):
                #Si dispara donde ya había disparado antes vuele a ejecutar el bucle
                return("vuelve_tocar")

            elif coordenada_disparo==" ":
                #Si dispara donde hay un espacio " " cambialo por el símbolo de agua y sal del bucle
                print("La máquina ha disparado en agua")
                tablero_del_jugador[fila][columna]=agua_icon
                tablero_del_jugador_comprobar[fila][columna]=agua_icon
                print(tablero_del_jugador)
                return("pierde_turno")
            else:
                #Si dispara donde hay un barco cambia al icono del fuego y comprueba si siguen quedando más barcos en el tablero
                print("La máquina ha disparado en un barco")
                tablero_del_jugador[fila][columna]=shoot_icon
                tablero_del_jugador_comprobar[fila][columna]=shoot_icon
                print(tablero_del_jugador)
                return("barco")
             