import numpy as np
import pandas as pd
import random 

TAM_TABLERO = 10 # Tamaño del tablero
TAM_BARCOS=[1,1,1,1,2,2,2,3,3,4] #se define como una lista de los tamaños
# el número de barcos es el len(TAM_BARCOS)


def generar_tablero():
    '''
    Esta función es la encargada de generar los tableros y de posicionar los barcos en ellos.
    '''
    # Diccionario que relaciona un número entero (que representa el tamaño de un barco) con un emoji correspondiente.
    EMOJIS = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"}
    tablero_jugador = np.full((TAM_TABLERO, TAM_TABLERO), " ")
    tablero_maquina = np.full((TAM_TABLERO, TAM_TABLERO), " ")

    barcos = []
    for tam_barco in TAM_BARCOS:
        colocado = False
        while not colocado:
            fila, col = np.random.randint(TAM_TABLERO), np.random.randint(TAM_TABLERO)
            direccion = np.random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
            if direccion == 'arriba':
                posiciones = [(fila-i, col) for i in range(tam_barco)]
            elif direccion == 'abajo':
                posiciones = [(fila+i, col) for i in range(tam_barco)]
            elif direccion == 'izquierda':
                posiciones = [(fila, col-i) for i in range(tam_barco)]
            else:
                posiciones = [(fila, col+i) for i in range(tam_barco)]
            if all(0<=fila<TAM_TABLERO and 0<=col<TAM_TABLERO and tablero_jugador[fila, col]==" " for fila, col in posiciones):
                barco = {"tam": tam_barco, "posiciones": posiciones}
                barcos.append(barco)
                for fila, col in posiciones:
                    tablero_jugador[fila, col] = EMOJIS[tam_barco]
                colocado = True
    
    return tablero_jugador, tablero_maquina, barcos

tablero = generar_tablero()
print(tablero)