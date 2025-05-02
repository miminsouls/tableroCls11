import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

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

# Propiedades del Tablero de Dibujo
with st.sidebar:
    st.subheader("Propiedades del Tablero")
    drawing_mode = st.sidebar.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=300,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Limpiar el lienzo
if clear_button:
    canvas_result.clear()

