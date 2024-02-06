import streamlit as st
from pages.test_1 import test
from pages.asignaturas_2 import mostrar_asignaturas

st.set_page_config(
    page_title="EmotutorIA",
    page_icon= "🤖"
)

asignaturas = mostrar_asignaturas()

st.title("¡Bienvenido a la Aplicación de Apoyo a Estudiantes!")
st.write("Esta aplicación te ayudará a mejorar tus habilidades de aprendizaje.")
st.write("Por favor, selecciona una opción en el menú lateral.")