import streamlit as st
import streamlit
import controlador
from streamlit_chat import message

streamlit.title("Modelo de Machine Learning del grupo invercasa ")
st.write("Puedes consultarme cualquier duda que tengas relacionada a Data Science!!")
st.write("Por favor, sé específico con tu pregunta, de lo contrario no podré ayudarte")

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = controlador.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

#Limpiar los campos
st.session_state.user = ''

with st.form('my-form'):
   query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
   submit_button = st.form_submit_button('Enviar',on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas)-1, -1, -1):
       message(st.session_state.respuestas[i], key=str(i))

    # Opción para continuar la conversación
     
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []


st.write("Chatbot developed by: xeppyz")
