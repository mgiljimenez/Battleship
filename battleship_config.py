import numpy
class tablero:
    def __init__(self, TAM_BARCOS, TAM_TABLERO, barco_icon):
        self.TAM_BARCOS=TAM_BARCOS
        self.TAM_TABLERO=TAM_TABLERO
        self.barco_icon=barco_icon
    def generar_tablero(self, tablero_input):
        self.tablero_input=tablero_input
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

#Variables generales del juego:
TAM_TABLERO = 10 # Tamaño del tablero
TAM_BARCOS=[1,1,1,1,2,2,2,3,3,4]  #se define como una lista de los tamaños/ el número de barcos es el len(TAM_BARCOS)
barco_icon = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"}
agua_icon= "🌊"
shoot_icon="💥"