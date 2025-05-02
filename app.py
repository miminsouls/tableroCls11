import streamlit as st
from PIL import Image
import numpy as np

# Título y descripción
st.title("Tablero de Dibujo - Lana Del Rey")
st.write("¡Bienvenido! Usa el tablero para dibujar y expresarte al estilo de Lana Del Rey.")

# Cargar y mostrar la imagen de fondo
image_path = "lana del rey american flag.jpg"  # Imagen de fondo
image = Image.open(image_path)
st.image(image, use_column_width=True)

# Configuración del lienzo
st.sidebar.header("Configuración del Lienzo")
brush_color = st.sidebar.color_picker("Color del pincel", "#000000")
brush_size = st.sidebar.slider("Tamaño del pincel", 1, 10, 5)
clear_button = st.sidebar.button("Limpiar Lienzo")

# Crear el lienzo con un fondo blanco
canvas_width = 700
canvas_height = 400

# Establecer el lienzo
if 'drawn_image' not in st.session_state:
    # Crear una imagen blanca de fondo en formato RGBA (con canal alfa)
    blank_image = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 255))
    st.session_state.drawn_image = blank_image

# Mostrar el lienzo
st.image(st.session_state.drawn_image, width=canvas_width)

# Funcionalidad para dibujar en el lienzo
def draw_on_canvas(image, color, size):
    # Crear una imagen sobre la que se dibuja
    img_array = np.array(image)
    brush = np.array([int(x, 16) for x in color[1:]]).reshape((1, 1, 3))
    img_array[:size, :size] = brush
    return Image.fromarray(img_array)

# Limpiar el lienzo
if clear_button:
    st.session_state.drawn_image = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 255))

