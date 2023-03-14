import numpy as np

TAM_TABLERO = 10
TAM_BARCOS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
EMOJIS = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"}



def generar_tablero(tablero_input):
    '''
    Esta función es la encargada de generar los tableros y de posicionar los barcos en ellos.
    '''
    # Diccionario que relaciona un número entero (que representa el tamaño de un barco) con un emoji correspondiente
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
            if all(0<=fila<TAM_TABLERO and 0<=col<TAM_TABLERO and tablero_input[fila, col]==" " for fila, col in posiciones):
                barco = {"tam": tam_barco, "posiciones": posiciones}
                barcos.append(barco)
                for fila, col in posiciones:
                    tablero_input[fila, col] = EMOJIS[tam_barco]
                colocado = True
    
    return tablero_input

tablero_jugador = generar_tablero(np.full((TAM_TABLERO, TAM_TABLERO), " "))
tablero_maquina = generar_tablero(np.full((TAM_TABLERO, TAM_TABLERO), " "))

print(tablero_jugador)
print()
print(tablero_maquina)
