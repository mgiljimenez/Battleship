# Battleship
Proyecto desarrollado por los alumnos de Data Science de The Bridge 2023_
-Cada un solo va a trabajar en su rama sin hacer push a develop hasta que hablemos

-Constantes (las vamos a llamar todos igual para que sea más fácil integrarlo):
    -tamaño del tablero: TAM_TABLERO     -> se define como un único número: por ejemplo TAM_TABLERO=10
    -tamaño de los barcos: TAM_BARCOS    ->se define como una LISTA de los tamaños: 
                                            p.e. TAM_BARCOS=[1,1,1,1,2,2,2,3,3,4]
                                            ojo!: el número de barcos es el len(TAM_BARCOS)


-Los archivos que vamos a entregar al final son:
    -1) README.mkd
        con todo explicado como lo hemos hecho, instrucciones, clases, funciones...
	-2) config.py:
			-Incluye constantes
	-3) clases.py:
			-Clases
	-4) main.py:
			-Código principal que usa las clases de clases.py y las constantes de config.py



INTRUCCIONES PARA EL DESARROLLO:

1) Mostrar foto de hundir la flota
2) Input que te pregunte el nombre
3) Bienvenida a la persona  y mostrar instrucciones

4) Mostrar el tablero del jugador con los barcos ya colocados
5) Mostrar el tablero de la máquina vacío
	-Tablero del jugador:
			-Donde hay barco sale el emoji del barco
			-Donde no hay barco sale " " (Espacio)
			-Si hay un disparo en agua: sale emoji agua
			-Si hay un disparo en barco: sale emoji explosion
	-Tablero de la máquina:
			-Al principio está entero con " "(Espacios)
			-Si hay un disparo en agua: sale emoji agua
			-Si hay un disparo en barco: sale emoji explosion

LO SIGUIENTE ES UN BUCLE WHILE(1):
	NUEVO BUCLE WHILE(2):
		6)Que le pida al jugador las coordenadas para disparar:	
			-Input para la fila (que especifique entre que valores)
			-Input para la columna (que especifique entre que valores)
			-Si introduce un valor no válido que vuelva a preguntar

		7)Comprobar el disparo del jugador en el tablero de la máquina:
			-Si no hay barco en esa coordenada: cambiar la celda por un emoji agua
			-Si hay barco en esa coordenada: cambiar la celda emoji explosion y comprobar si siguen quedando barcos en el tablero (sino ha finalizado el juego)
		8) Si ha acertado:mostrar tablero por pantalla volver al bucle (2) 
		   Si no ha acertado continuar (salir del bucle)
	

	NUEVO BUCLE WHILE (3):
		8)Genera unas coordenadas aleatorias que no hayan sido ya usadas para disparar en el tablero del jugador:

		9)Comprobar disparo de la máquina en el tablero del jugador:
			-Si no hay barco en esa coordenada: cambiar la celda por un emoji agua
			-Si hay barco en esa coordenada: cambiar la celda emoji explosion y comprobar si siguen quedando barcos en el tablero (sino ha finalizado el juego)
		10)Si ha acertado: mostrar tablero por pantalla y volver al bucle (3), 
		   si no ha acertado continuar (salir del bucle 3)


	10)Mostrar tablero del jugador para ver el resultado del tiro de la máquina
	11)Mostrar tablero de la máquina para ver el resultado de mi tiro y volver a tirar (vuelve a bucle 1)


ESTO NO ESTÁ DENTO DEL BUCLE 1:

12) Finalizar juego haciendo un print
