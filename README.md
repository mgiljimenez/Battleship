# HUNDIR LA FLOTA - JUEGO :collision::boat:

## Explicación del juego
En este clásico juego de estrategia naval, tendrás la oportunidad de poner a prueba tus habilidades para hundir los barcos de tu oponente mientras proteges los tuyos. 
El tamaño del tablero es 10 x 10 y los barcos se posicionan aleatoriamente en el mismo.
Una vez que los barcos han sido posicionados, comienza el juego en turnos alternados entre tú y tu oponente. 
En cada turno, intentarás adivinar la posición de los barcos enemigos para hundirlos antes de que él hunda los tuyos.
Para adivinar la posición de los barcos enemigos debes indicar las coordenadas en las que crees que se encuentra el barco en el tablero.
Gana el jugador que logre hundir todos los barcos del oponente primero.

## Variables Fijas
- **TAM_TABLERO** = 10 (*Tamaño del tablero*) 
- **TAM_BARCOS** = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] (*Contiene los tamaños de los barcos a colocar en el tablero*)
- **barco_icon** = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"} (*Diccionario que contiene los símbolos que se usarán para representar los barcos en el tablero, donde la clave es la longitud del barco y el valor es el símbolo correspondiente*)
- **shoot_icon**="💥" (*Disparo en barco*)


## Clase usuario
La clase usuario tiene 3 atributos (**TAM_BARCOS, TAM_TABLERO y barco_icon**) y 3 métodos:

	'__init__': Este es el método constructor de la clase usuario, que inicializa los atributos TAM_BARCOS, TAM_TABLERO y barco_icon.


	'generar_tablero': Este método genera un tablero con los barcos colocados de forma aleatoria. Se crea un tablero vacío y se van colocando los barcos uno por uno. Para cada barco se genera una posición y dirección aleatoria y se comprueba si se puede colocar en esa posición sin solaparse con otro barco o salirse del tablero. Si se puede colocar, se añade al tablero y se marca en las posiciones que ocupa el icono correspondiente.

	En particular, la función generar_tablero se encarga de crear y devolver un tablero de juego, ya sea para el jugador o para la máquina, según el parámetro tipo que recibe.

	1. El primer paso es verificar el parámetro 'tipo' que se recibe. Si es "jugador", entonces se debe crear un tablero de juego para el jugador, mientras que si es cualquier otra cosa (por ejemplo, "maquina"), se debe crear un tablero para la máquina.
   
	2. Si 'tipo' == 'jugador', se inicializa una matriz de TAM_TABLERO filas por TAM_TABLERO columnas, en la que todas las casillas están vacías (representadas por el caracter espacio en blanco: " ")
   
	3. Luego, se define una lista vacía 'barcos', que será utilizada para guardar los barcos que se coloquen en el tablero.
   
	4. A continuación, se realiza un bucle for que itera sobre los tamaños de barcos que se deben colocar en el tablero (estos tamaños están definidos en la variable self.TAM_BARCOS, que es un atributo de la clase 'usuario').
   
	5. Dentro del bucle for, se define una variable colocado que se inicializa en False. Esta variable será utilizada para indicar si se ha colocado correctamente un barco en el tablero.
   
	6. Se utiliza un bucle while que se ejecutará hasta que se coloque correctamente el barco en el tablero. En cada iteración, se genera aleatoriamente una fila y una columna en el tablero, así como una dirección en la que se debe colocar el barco (arriba, abajo, izquierda o derecha).
   
	7. A partir de la fila, la columna y la dirección generadas aleatoriamente, se calculan las posiciones que ocupará el barco en el tablero.
	Si la dirección es 'arriba', la variable posiciones será una lista de tuplas donde la fila disminuirá en 1 para cada posición en la lista (es decir, el barco se ubicará hacia arriba).
	Si la dirección es 'abajo', la variable posiciones será una lista de tuplas donde la fila aumentará en 1 para cada posición en la lista (es decir, el barco se ubicará hacia abajo).
	Si la dirección es 'izquierda', la variable posiciones será una lista de tuplas donde la columna disminuirá en 1 para cada posición en la lista (es decir, el barco se ubicará hacia la izquierda).
	Si la dirección es 'derecha', la variable posiciones será una lista de tuplas donde la columna aumentará en 1 para cada posición en la lista (es decir, el barco se ubicará hacia la derecha).

	
	'disparar': La función disparar permite al jugador disparar en una posición del tablero del oponente. Esta función tiene dos argumentos: tablero_máquina y tablero interactivo, que son los tableros de la máquina y el tablero donde el jugador puede ver los disparos realizados al tablero enemigo, respectivamente.
	Descripción del proceso:
    1. Se pide al usuario que ingrese una fila y una columna para realizar el disparo.
   
	2. Se comprueba si las coordenadas ingresadas están dentro del rango del tablero.
   
    3. Si las coordenadas son válidas, se comprueba si el jugador ya ha disparado en esa posición antes. Si es así, se le pide que vuelva a disparar.
   
	4. Si las coordenadas son válidas y el jugador no ha disparado en esa posición antes, se comprueba si la posición contiene un barco o está vacía.
   
	5. Se actualiza el tablero correspondiente con el resultado del disparo (agua/barco).


## Clase máquina
Sigue la misma lógica que la clase Jugador. Tiene 3 atributos de instancia (TAM_BARCOS, TAM_TABLERO y barco_icon) y 3 métodos:

	'__init__': es el constructor de la clase maquina que inicializa los 3 atributos mencionados anteriormente. Los argumentos que recibe son los valores que se asignarán a los atributos.


	'generar_tablero': Se utiliza para crear un tablero aleatorio para el juego. Si el argumento tipo es "maquina", se genera un tablero aleatorio que contiene barcos y devuelve ese tablero. De lo contrario, devuelve un tablero vacío.

	'disparar': Se utiliza para que la máquina dispare en el tablero del jugador. Recibe dos argumentos: tablero_del_jugador (es el que se va a imprimir) y tablero_del_jugador_comprobar (es un tablero auxiliar utilizado por la máquina para saber qué casillas ya han sido disparadas, y poder evitar disparar varias veces en la misma casilla). Por lo tanto, tablero_del_jugador se utiliza para el juego en sí, mientras que tablero_del_jugador_comprobar se utiliza para llevar un registro de los disparos realizados por la máquina y no permitir que en la misma casilla se dispare más de una vez. A continuación se elige una coordenada aleatoria y se comprueba si hay un barco en esa coordenada. Si hay un barco, se marca como tocado, si no hay un barco, se marca como agua. El método devuelve una cadena que indica si la máquina ha vuelto a tocar una posición previamente disparada, si ha tocado agua o si ha tocado un barco.


## Una vez, definidas ambas clases, vamos a proceder a integrarlas y a montar el juego:
En primer lugar importamos las bibliotecas necesarias y las clases que hemos definido previamente ('usuario' y 'maquina'). Luego se importan las variables que se utilizaran para el juego.

A continuación, se crean dos objetos: 'jugador_usuario' y 'jugador_maquina', a partir de las clases 'usuario' y 'maquina', respectivamente. De esta forma, inicializamos a los dos jugadores.

Seguidamente, iniciamos el juego preguntando al usuario su nombre mediante la función 'input()' y mostrando las instrucciones y los tableros iniciales del jugador, así como el tablero interactivo, que muestra aquellas posiciones que ya han sido atacadas por el jugador, es decir, muestra el tablero máquina actualizado con los disparos del jugador.

## Empieza el juego
**TURNO DEL JUGADOR**

Empezamos montando dos bucles 'while' anidados para que el jugador pueda realizar múltiples turnos consecutivos hasta que falle en su intento de golpear los barcos de la máquina.
En cada turno del jugador, se llama al método 'disparar' del objeto 'jugador_usuario', que toma como argumentos el tablero máquina y el tablero interactivo.
Dependiendo del resultado de este disparo, se toma una acción u otra: si el jugador falla en el disparo, pierde su turno, el bucle interior se rompe y el turno de la máquina ; si el jugador tira donde ya había tirado antes, se le dice que vuelva a intentarlo; y si el jugador acierta en un barco, se le vuelve a pedir un nuevo disparo.

Después de cada turno del jugador, se verifica si el tablero interactivo es igual al tablero máquina en todos sus elementos. Si son iguales significa que el jugador ha acertado todos los barcos de la máquina y ha ganado el juego. Por lo tanto, se rompe el bucle exterior y se establece como ganador al jugador.

**TURNO MÁQUINA**

En caso contrario, el juego continúa y le toca el turno a la máquina para disparar. Dentro de un bucle 'while', la máquina espera 3 segundos (gracias a la función sleep()) para simular la 'pausa' entre los turnos de los jugadores, y luego utiliza el método 'disparar' de la clase máquina para disparar al tablero del jugador. La máquina realiza su disparo y recibe una respuesta de acuerdo a la posición en la que impactó. Esta respuesta es almacenada en la variable 'turno_maquina'.
Si el resultado del disparo de la máquina es "pierde_turno", significa que ha impactado en una posición con un espacio en blanco. Por lo tanto, se termina el turno de la máquina con un break. 
Si el resultado del disparo de la máquina es "vuelve_tocar", significa que ha impactado en una posición ya disparada anteriormente. El bucle continúa.
Si el resultado del disparo de la máquina es "barco", significa que ha impactado en una posición con un barco enemigo. Se verifica si la máquina ha ganado el juego (es decir, si todos los barcos del jugador han sido destruidos), comparando 'tablero_del_jugador' con 'tablero_del_jugador_comprobar'. Si se han destruido todos los barcos del jugador, el bucle se termina con un break.
Si la máquina no ha ganado el juego y ha impactado en un barco, se imprime un mensaje de que la máquina volverá a tirar y se continúa con el bucle.
Si el bucle termina por completo, significa que la máquina ha ganado el juego y se establece el ganador como "maquina".