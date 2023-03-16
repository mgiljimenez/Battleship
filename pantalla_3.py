import streamlit as st
import pandas as pd
import numpy as np

TAM_TABLERO = 10 # Tamaño del tablero
TAM_BARCOS=[1,1,1,1,2,2,2,3,3,4]  #se define como una lista de los tamaños/ el número de barcos es el len(TAM_BARCOS)
barco_icon = {1: "🚣", 2: "🚢", 3: "🛳️", 4: "🚤"}
agua_icon= "🌊"
shoot_icon="💥"

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
                    tablero_input[fila, col] = barco_icon[tam_barco]
                colocado = True
    
    return tablero_input

tablero_del_jugador = generar_tablero(np.full((TAM_TABLERO, TAM_TABLERO), " "))
tablero_de_maquina = generar_tablero(np.full((TAM_TABLERO, TAM_TABLERO), " "))
tablero_interactivo=np.full((TAM_TABLERO, TAM_TABLERO), " ")
#--------------------------------------------------------------



#Código para la página web:
st.set_page_config(page_title="Battleship", page_icon="ship")

def estilo_celda(valor):
    if valor.strip() == "":
        return "background-color: lightgray"
    elif valor.isnumeric():
        return "background-color: lightblue"
    else:
        return ""
df_tablero_jugador = pd.DataFrame(tablero_del_jugador)
estilo_jugador = df_tablero_jugador.style.applymap(estilo_celda).set_properties(**{'font-size': '12px', 'text-align': 'center'})
df_tablero_maquina = pd.DataFrame(tablero_de_maquina)
estilo_maquina = df_tablero_maquina.style.applymap(estilo_celda).set_properties(**{'font-size': '12px', 'text-align': 'center'})



st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")

col1, col2 = st.columns([4,2])

with col1:
   st.info("TABLERO MAQUINA")
   st.write(estilo_maquina.render(), height=500, style={"font-size": "12px"}, unsafe_allow_html=True)


with col2:
   st.info(" TU TABLERO ")
   st.write(estilo_jugador.render(), height=500, style={"font-size": "12px"}, unsafe_allow_html=True)


st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")


barquito=st.success("Has dado en un barco")
fallito=st.error("Has dado en agua")





# Crear un formulario
with st.form("my_form"):
    # Definir el primer input
    valor_1 = st.number_input("Ingrese la fila", min_value=0, max_value=9, value=0, step=1)
    
    # Definir el segundo input
    valor_2 = st.number_input("Ingrese la columna", min_value=0, max_value=9, value=0, step=1)
    
    # Agregar un botón para enviar los valores
    enviar = st.form_submit_button("Enviar")

# Mostrar los valores ingresados cuando se hace clic en el botón "Enviar"
if enviar:
    st.write("Valores ingresados:", valor_1, "y", valor_2)







