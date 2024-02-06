import streamlit as st
preguntas = [
    "Una página web tiene un vídeo que muestra cómo hacer un gráfico o una tabla especial. Aprendería más:",
    "Prefiero un presentador o un profesor que utilice:",
    "Quiero aprender a tomar mejores fotos. Yo:",
    "Quiero aprender sobre un nuevo proyecto. Me gustaría pedir:",
    "Quiero aprender a jugar un nuevo juego de mesa o de cartas. Yo:",
    
]

opciones = [
    ["Escuchando.", "Viendo los diagramas.", "Leyendo las palabras.", "Viendo las acciones."],
    ["Preguntas y respuestas, charlas, discusiones en grupo u oradores invitados.", "Diagramas, cuadros, mapas o gráficos.", "Folletos, libros o lecturas.",  "Demostraciones, modelos o sesiones prácticas.", ],
    ["Comunicarme con otros a través del diálogo.", "Utilizar ejemplos visuales.", "Utilizar bien las palabras en las comunicaciones escritas.", "Trabajar con diseños, mapas o gráficos."],
    ["Una conversación sobre el proyecto.", "Diagramas que muestren las etapas del proyecto con gráficos de beneficios y costes.", "Un informe escrito que describa las principales características del proyecto.", "Ejemplos en los que el proyecto se haya utilizado con éxito."],
    ["Hablaría con alguien que haya jugado antes.", "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.",  "Leería las instrucciones.", "Observaría a otros jugar antes de unirme al juego."],

]

def mostrar_pregunta(pregunta, opciones):
    form = st.form(key='my_form')
    form.title("Test VARK para Estudiantes")
    form.write(f"Por favor, responde la siguiente pregunta:")
    form.write(pregunta)
    respuesta = form.radio("Selecciona una opción:", opciones)
    submit_button = form.form_submit_button(label='Siguiente')
    return respuesta

def calcular_perfil(respuestas):
    puntuacion = {"auditivo": 0, "visual": 0, "lector": 0, "kinestésico": 0}
    valores_respuestas = {
        "auditivo": ["a"],
        "visual": ["c"],
        "lector": ["b"],
        "kinestésico": ["d"]
    }

    for respuesta in respuestas:
        for perfil, opciones in valores_respuestas.items():
            if respuesta in opciones:
                puntuacion[perfil] += 1
                break

    perfil = max(puntuacion, key=puntuacion.get)
    return perfil
    

def test():
    
    if 'indice_pregunta' not in st.session_state:
        st.session_state.indice_pregunta = 0

    indice_pregunta = st.session_state.indice_pregunta
    respuestas = []

    if indice_pregunta < len(preguntas):
        respuesta = mostrar_pregunta(preguntas[indice_pregunta], opciones[indice_pregunta])
        respuestas.append(respuesta)
        st.session_state.indice_pregunta += 1

    
    
    if indice_pregunta == len(preguntas):

    #if st.session_state.indice_pregunta == len(preguntas):
        st.title("¡Test finalizado!")
        st.write("Haz clic en el botón para comprobar el resultado.")
        
        if st.button("Comprobar Resultado"):
            #if len(respuestas) == len(preguntas):
            if None not in respuestas: 
                perfil = calcular_perfil(respuestas)
                #st.title("¡Test completado!")
                st.write(f"Tu perfil de aprendizaje según el test VARK es: {perfil}")
            
            



if __name__ == "__main__":
    test()