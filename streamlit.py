import streamlit as st
import pandas as pd
from battleship_config import usuario, maquina, mostrar_tablero
from battleship_variables import TAM_TABLERO, TAM_BARCOS,barco_icon,agua_icon,shoot_icon,instrucciones


#Inicializamos a los dos jugadores
jugador_usuario=usuario(TAM_BARCOS,TAM_TABLERO,barco_icon)
jugador_maquina=maquina(TAM_BARCOS,TAM_TABLERO, barco_icon)

#Generamos los cuatro tableros necesarios para el juego
tablero_del_jugador=jugador_usuario.generar_tablero("jugador")
tablero_interactivo=jugador_maquina.generar_tablero("interactivo")

#Definimos la clase que da formato al tablero para mostrarlo por pantalla
class MostrarTablero:
    def __init__(self, tablero):
        self.tablero = tablero
    def estilo_celda(self, valor):
        if valor.strip() == "":
            return "background-color: lightgray"
        elif valor.isnumeric():
            return "background-color: lightblue"
        else:
            return ""
    def mostrar(self):
        df_tablero = pd.DataFrame(self.tablero)
        estilo = df_tablero.style.applymap(self.estilo_celda).set_properties(**{'font-size': '5px', 'text-align': 'center'})
        return(estilo)


st.set_page_config(page_title="Battleship", page_icon="ship", layout="centered")

st.sidebar.title("Battleship 🚢")
st.sidebar.info("ℹ Información de la partida")
st.sidebar.warning("Tu turno")
with st.sidebar.form("my_form"):
   st.write("Dispara al tablero de tu oponente")
   fila = st.number_input("Fila:", min_value=0, max_value=9)
   columna= st.number_input('Columna:', min_value=0, max_value=9)

   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write(f"Disparo en fila {fila}, columna {columna}")
st.sidebar.success("💥 Has disparado en un barco!!")



col1, col2 = st.columns(2)

with col1:
   st.warning("TABLERO DE TU OPONENTE")
   mostrar_tablero = MostrarTablero(tablero_interactivo)
   st.write(mostrar_tablero.mostrar(), width=400)
   

with col2:
   st.warning("TU TABLERO")
   mostrar_tablero = MostrarTablero(tablero_del_jugador)
   st.write(mostrar_tablero.mostrar())
