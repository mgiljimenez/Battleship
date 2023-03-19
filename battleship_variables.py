TAM_TABLERO = 10 # Tamaño del tablero
TAM_BARCOS=[1,1,1,1,2,2,2,3,3,4]  #se define como una lista de los tamaños/ el número de barcos es el len(TAM_BARCOS)
barco_icon = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"}
agua_icon= "🌊"
shoot_icon="💥"
instrucciones="""
En este clásico juego de estrategia naval, tendrás la oportunidad de poner a prueba tus
habilidades para hundir los barcos de tu oponente mientras proteges los tuyos.
El tamaño del tablero es 10 x 10 y los barcos se posicionan aleatoriamente en el mismo.
Una vez que los barcos han sido posicionados, comienza el juego en turnos alternados entre tú y tu oponente.
En cada turno, intentarás adivinar la posición de los barcos enemigos para hundirlos antes de que él hunda los tuyos.
Para adivinar la posición de los barcos enemigos debes indicar las coordenadas en las que crees que se encuentra el barco en el tablero.
Gana el jugador que logre hundir todos los barcos del oponente primero.
¡Que empiece el juego!
======================================================================================================================================"""