import pandas as pd
from battleship_variables import barco_icon, agua_icon, shoot_icon
from IPython.display import HTML, display


class mostrar_tablero:
    def __init__(self):
        pass
        
    def mostrar(self, tablero):
        self.tablero=tablero
        tablero_df=pd.DataFrame(tablero)
        tablero_bonito= tablero_df.style.apply(lambda x: ["background: yellow" if v == shoot_icon
                             else "background: white" if v == " "
                             else "background: lightblue" if v == agua_icon
                             else "background: gray" if v in barco_icon.values()
                             else "" for v in x], axis = 1)
        return tablero_bonito
        
tablero_mostrar=mostrar_tablero()


tabla=[["🚣"," ","🚢"," ","🌊"," "," "],
       ["🚣"," ","🚢"," "," "," "," "],
       ["🚣"," ","🚢"," ","🌊"," "," "],
       ["🚣","💥","🚢"," "," "," "," "],
       ["🚣"," ","🚢","💥"," "," "," "],
       ["🚣"," ","🚢"," "," "," "," "],
       [" "," "," "," "," "," "," "]]

mt = mostrar_tablero() 

display(HTML(mt.mostrar(tabla).render()))

# Create an instance of the mostrar_tablero class

 # Call the mostrar method on the instance and pass the tabla as an argument