from tabulate import tabulate

class mostrar_tablero:
    def __init__(self):
        pass
        
    def mostrar(self, tablero):
        print(tabulate(tablero, headers="keys",showindex="always", tablefmt='fancy_grid'))
    
df = [[1,2,3],[4,6,7],[4,6,4]]
tablero_mostrar = mostrar_tablero()
tablero_mostrar.mostrar(df)