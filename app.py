import streamlit as st
from PIL import Image

# Definir una función para cambiar el tema
def set_lana_del_rey_theme():
    # Cambiar el fondo de la aplicación (puedes agregar tu propia imagen aquí)
    st.markdown("""
        <style>
        body {
            background-image: url('https://www.example.com/lanadelrey-background.jpg');
            background-size: cover;
            background-position: center;
            color: white;
        }
        .streamlit-expanderHeader {
            font-family: 'Cinzel', serif;
        }
        .css-1v3fvcr {
            font-family: 'Lobster', cursive;
            color: #F5B7B1;
        }
        .stButton > button {
            background-color: #6C3483;
            color: white;
            font-family: 'Cinzel', serif;
            border: 2px solid #F5B7B1;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #F5B7B1;
            color: #6C3483;
            border: 2px solid #6C3483;
        }
        </style>
    """, unsafe_allow_html=True)

# Cargar fuente de Google Fonts (si es necesario)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Lobster&family=Cinzel&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Aplicar el tema
set_lana_del_rey_theme()

# Cargar el título y descripción
st.title("Lana del Rey Inspired App")
st.write("Bienvenido a mi aplicación con la vibra de Lana del Rey. Disfruta de la magia y el glamour de sus canciones.")

# Tu código existente aquí
st.write("Este es un ejemplo de personalización manteniendo la funcionalidad.")
