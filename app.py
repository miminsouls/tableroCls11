import os
import streamlit as st
from PIL import Image
import base64
import numpy as np
from openai import OpenAI

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")

# Configuración de Streamlit
st.set_page_config(page_title="Tablero de Dibujo y Análisis de Imagen", layout="centered", initial_sidebar_state="collapsed")
st.title("Tablero de Dibujo - Lana Del Rey y Análisis de Imagen 🤖🏞️")
ke = st.text_input('Ingresa tu Clave de OpenAI')
os.environ['OPENAI_API_KEY'] = ke

# Recuperar la clave de API de OpenAI
api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)

# Cargar la imagen de fondo para el tablero de dibujo
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

# Subir una imagen para análisis
uploaded_file = st.file_uploader("Sube una imagen para analizar", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Mostrar la imagen subida
    with st.expander("Imagen subida", expanded=True):
        st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)

# Toggle para mostrar detalles adicionales
show_details = st.checkbox("Añadir detalles sobre la imagen")

if show_details:
    additional_details = st.text_area("Añade contexto adicional sobre la imagen:")

# Botón para activar el análisis de la imagen
analyze_button = st.button("Analizar la imagen")

# Análisis de la imagen con OpenAI
if uploaded_file is not None and api_key and analyze_button:
    with st.spinner("Analizando..."):
        # Codificar la imagen en base64
        base64_image = encode_image(uploaded_file)
    
        prompt_text = "Describe lo que ves en la imagen en español"
    
        if show_details and additional_details:
            prompt_text += f"\n\nContexto adicional proporcionado por el usuario:\n{additional_details}"
    
        # Crear el payload para la solicitud
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                ],
            }
        ]
    
        # Realizar la solicitud a la API de OpenAI
        try:
            full_response = ""
            message_placeholder = st.empty()
            for completion in client.chat.completions.create(
                model="gpt-4o", messages=messages, max_tokens=1200, stream=True
            ):
                if completion.choices[0].delta.content is not None:
                    full_response += completion.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
    
        except Exception as e:
            st.error(f"Ha ocurrido un error: {e}")
else:
    # Advertencias para acciones del usuario
    if not uploaded_file and analyze_button:
        st.warning("Por favor sube una imagen para analizar.")
    if not api_key:
        st.warning("Por favor ingresa tu clave API de OpenAI.")
