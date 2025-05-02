import streamlit as st
from PIL import Image

# Definir una función para cambiar el tema
def set_lana_del_rey_theme():
    # Cambiar el fondo de la aplicación (puedes agregar tu propia imagen aquí)
    st.markdown("""
        <style>
        body {
            background-image: url('https://www.example.com/lanadelrey-background.jpg'); /* Cambia por el enlace de la imagen */
            background-size: cover;
            background-position: center;
            color: white;
            font-family: 'Cinzel', serif;
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
        .stTextInput>label {
            color: #F5B7B1;
        }
        .stTextInput>div>input {
            background-color: rgba(255, 255, 255, 0.6);
            border-radius: 8px;
            color: #6C3483;
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

# Cargar imagen relacionada con Lana del Rey (si tienes una imagen propia, cámbiala)
image_url = "https://upload.wikimedia.org/wikipedia/commons/2/28/Lana_Del_Rey_2019_by_Glenn_Francis.jpg"
image = Image.open(image_url)
st.image(image, caption='Lana del Rey', use_column_width=True)

# Agregar una pequeña descripción de Lana del Rey
st.subheader("Sobre Lana del Rey")
st.write("""
Lana Del Rey es una cantante, compositora y productora estadounidense conocida por sus letras melancólicas, su estilo musical que fusiona pop, rock y música electrónica, y su estética retro inspirada en la cultura americana. Sus canciones están llenas de nostalgia, romance y un toque de tragedia.

Algunos de sus álbumes más conocidos incluyen "Born to Die", "Ultraviolence" y "Norman Fucking Rockwell!".
""")

# Ejemplo de una función interactiva manteniendo la funcionalidad del script original
st.subheader("Interacción con la app")
user_input = st.text_input("Escribe algo aquí... (ejemplo: 'Born to Die', 'Summertime Sadness')")

# Mostrar un mensaje dependiendo del input
if user_input:
    st.write(f"¡Has escrito: {user_input}!")
    if user_input.lower() == 'born to die':
        st.write("¡Qué bien! 'Born to Die' es uno de los discos más emblemáticos de Lana del Rey.")
    elif user_input.lower() == 'summertime sadness':
        st.write("¡Ah, 'Summertime Sadness' es todo un himno! Qué gran canción.")
    else:
        st.write("¡Buen gusto! Lana tiene muchas canciones increíbles.")
else:
    st.write("Escribe algo en el campo de texto para interactuar.")

# Puedes incluir más secciones aquí, como botones, gráficos, etc.
