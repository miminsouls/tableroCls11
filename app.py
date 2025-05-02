import streamlit as st
from PIL import Image
import numpy as np
import cv2  # Necesario para el manejo de imágenes y dibujo

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

# Cargar imagen relacionada con Lana del Rey desde un archivo local
image_path = "lana del rey american flag.jpg"  # Ruta del archivo de imagen en tu directorio

# Cargar la imagen
image = Image.open(image_path)

# Mostrar la imagen
st.image(image, caption='Lana del Rey', use_column_width=True)

# Agregar una pequeña descripción de Lana del Rey
st.subheader("Sobre Lana del Rey")
st.write("""
Lana Del Rey es una cantante, compositora y productora estadounidense conocida por sus letras melancólicas, su estilo musical que fusiona pop, rock y música electrónica, y su estética retro inspirada en la cultura americana. Sus canciones están llenas de nostalgia, romance y un toque de tragedia.

Algunos de sus álbumes más conocidos incluyen "Born to Die", "Ultraviolence" y "Norman Fucking Rockwell!".
""")

# Ahora, implementamos el tablero de dibujo

# Configuración del lienzo
st.subheader("¡Haz tu propio dibujo!")
canvas_width = 700
canvas_height = 500

# Usar la funcionalidad de dibujo (canvas)
drawing = st.empty()

# Crear un lienzo en blanco para que el usuario pueda dibujar
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Mostrar el lienzo en la aplicación
st.image(canvas, caption="Tu dibujo", use_column_width=True)

# Establecer el lápiz de dibujo
color = (255, 0, 0)  # color rojo para el lápiz
brush_size = 10  # tamaño de pincel

# Función para dibujar en el lienzo
def draw_on_canvas(x, y, color, brush_size):
    cv2.circle(canvas, (x, y), brush_size, color, -1)

# Obtener las coordenadas de clic en el lienzo (esto se logra con una interacción con la app)
x, y = st.slider("Posición X", 0, canvas_width), st.slider("Posición Y", 0, canvas_height)
draw_on_canvas(x, y, color, brush_size)

# Ejemplo de cómo guardar el dibujo en un archivo
if st.button("Guardar mi dibujo"):
    Image.fromarray(canvas).save("mi_dibujo.png")
    st.write("¡Tu dibujo ha sido guardado!")
