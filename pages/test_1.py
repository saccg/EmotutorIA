import streamlit as st
preguntas = [
    "Cuando estás aprendiendo algo nuevo, ¿cuál de las siguientes opciones encuentras más efectiva?:",
    "Al recibir enseñanza de un profesor o presentador, ¿qué enfoque prefieres?:",
    "¿Cómo mejorarías tus habilidades en fotografía?:",
    "¿Qué haces si quieres obtener más información sobre un nuevo proyecto?:",
    "Quiero aprender a jugar un nuevo juego de mesa o de cartas. Yo:",
    "Si quieres aprender a hacer algo en el ordenador,tú:",
    "¿Qué te importa más a la hora de elegir una carrera o área de estudio?:",
    "Quieres aprender a tocar una canción en un instrumento musical, ¿Qué método utilizarías?:",
    "Al explorar información en Internet,¿Qué formato de contenido encuentras más efectivo para aprender?:",
    "Cuando consideras tu estilo de aprendizaje en general,¿Qué enfoque se adapta mejor a ti?:",
    
]

opciones = [
    ["Escuchar a alguien que me explique.", "Ver vídeos o imágenes.", "Leer instrucciones o artículos.", "Practicar o hacer algo tú mismo."],
    ["Preguntas y respuestas, participar en charlas interactivas.", "Utilizar gráficos y mapas visuales.", "Explorar materiales de lectura atractivos.",  "Experimentar demostraciones prácticas.", ],
    ["Haciendo preguntas sobre la cámara.", "Viendo ejemplos visuales.", "Siguiendo instrucciones escritas.", "Utilizando ejemplos de fotos."],
    ["Participar en charlas sobre características clave.", "Observar esquemas visuales de éxito del proyecto.", "Un informe escrito que describa las principales características del proyecto.", "Experimentar con ejemplos prácticos referentes al proyecto."],
    ["Hablaría con alguien que haya jugado antes.", "Utilizaría los diagramas que explican las distintas fases, movimientos y estrategias del juego.",  "Leería las instrucciones.", "Observaría a otros jugar antes de unirme al juego."],
    ["Escuchas un podcast.", "Ves vídeos tutoriales en Youtube.", "Lees las instrucciones", "Participas en demostraciones prácticas."],
    ["Comunicarte con otros mediante conversaciones.", "Trabajar con diseños visuales.", "Comunicarte bien por escrito.", "Aplicar conocimientos en situaciones reales."],
    ["Recibir consejos de alguien con experiencia en música.", "Ver algún tutorial práctico en Youtube.", "Lerr explicaciones claras sobre la interpretación de la canción.", "Seguir las partituras o las tablaturas paso a paso."],
    ["Audios divertidos y educativos.", "Diseño visual atractivo.", "Textos explicativos interesantes.", "Vídeos prácticos y demostrativos."],
    ["Participando en discusiones y foros.", "Identificando patrones y conexiones.", "Leyendo materiales variados.", "Aplicando ejemplos y casos prácticos."],

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