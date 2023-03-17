import streamlit as st

st.set_page_config(page_title="Hundir la Flota", page_icon="boat", layout='wide', initial_sidebar_state='auto')

st.sidebar.title('Hundir la Flota')
st.sidebar.image(r"img/hundir_flota.jpg", use_column_width=True)
option = st.sidebar.selectbox('Menu', ['Bienvenida','Instrucciones', 'Juego'])

if option == 'Bienvenida':
    st.markdown("""
        <style>
            @import url('https://use.fontawesome.com/releases/v5.15.3/css/all.css');
            .title {
                color: #1a5276;
                font-size: 60px;
                text-shadow: 2px 2px #34495e;
            }
            .ship-icon:before {
                content: "\f21a";
                font-family: 'Font Awesome 5 Free';
                font-weight: 900;
                font-size: 72px;
                color: #1a5276;
                margin-right: 10px
            }
            .wave-icon:before {
                content: "\f0eb";
                font-family: 'Font Awesome 5 Free';
                font-weight: 900;
                font-size: 72px;
                color: #1a5276;
                margin-left: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="title">
            <i class="fas fa-ship ship-icon"></i>
            Hundir la Flota
            <i class="fas fa-water wave-icon"></i>
        </div>
    """, unsafe_allow_html=True)

    st.image(r"img/hundir_flota.jpg", use_column_width=True)

    # Definimos la variable nombre del jugador
    nombre_jugador = st.text_input('Introduce tu nombre')
    # Creamos un botón para avanzar a la siguiente pantalla
    if len(nombre_jugador) < 1:
        st.warning('Introduce un nombre para continuar')
        st.button('Continuar', disabled=True)
    else:
        st.experimental_set_query_params(menu='Instrucciones')
        st.button('Continuar')
    
    
    
elif option == 'Instrucciones':
    
    st.markdown("""
        <style>
            @import url('https://use.fontawesome.com/releases/v5.15.3/css/all.css');
            .title {
                color: #1a5276;
                font-size: 60px;
                text-shadow: 2px 2px #34495e;
            }
            .ship-icon:before {
                content: "\f21a";
                font-family: 'Font Awesome 5 Free';
                font-weight: 900;
                font-size: 72px;
                color: #1a5276;
                margin-right: 10px
            }
            .wave-icon:before {
                content: "\f0eb";
                font-family: 'Font Awesome 5 Free';
                font-weight: 900;
                font-size: 72px;
                color: #1a5276;
                margin-left: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="title">
            <i class="fas fa-ship ship-icon"></i>
            Hundir la Flota
            <i class="fas fa-water wave-icon"></i>
        </div>
    """, unsafe_allow_html=True)
    

    st.image(r"img/image.jpg", use_column_width=True)
    
    st.write("""
        ¡Bienvenidos al juego de Hundir la Flota!
        
        En este clásico juego de estrategia naval, tendrás la oportunidad de poner a prueba tus
        habilidades para hundir los barcos de tu oponente mientras proteges los tuyos.
        
        El tamaño del tablero es 10 x 10 y los barcos se posicionan aleatoriamente en el mismo.
        Una vez que los barcos han sido posicionados, comienza el juego en turnos alternados entre tú y tu oponente. 
        En cada turno, intentarás adivinar la posición de los barcos enemigos para hundirlos antes de que él hunda los tuyos.
        Para adivinar la posición de los barcos enemigos debes indicar las coordenadas en las que crees que se encuentra el barco en el tablero.
        Gana el jugador que logre hundir todos los barcos del oponente primero.
        
        ¡Que empiece el juego!""")
    
    st.write("<div style='text-align: center;'><button>COMENZAR</button></div>", unsafe_allow_html=True)

    
    