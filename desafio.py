import streamlit as st
from groq import Groq

st.set_page_config(page_title='Mi ChatBot', page_icon='🤖', layout='centered')

def createUserGroq():
    scrt_key = st.secrets['API_KEY']
    return Groq(api_key=scrt_key)

##-------tareas generales///tareas complejas///comprension y generacion de texto
MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def setearPagina ():
    st.title('Desafio 9: Mi ChatBot.')
    st.sidebar.title('Configuracion del ChatBot.')
    elegirModelo = st.sidebar.selectbox('Elegi el modelo:', MODELOS)
    st.sidebar.write('Tareas generales:')
    st.sidebar.write('→→ llama3-8b-8192 ←←')
    st.sidebar.write('Tareas complejas:')
    st.sidebar.write('→→ llama3-70b-8192 ←←')
    st.sidebar.write('Comprension y generacion de texto:')
    st.sidebar.write('→→ mixtral-8x7b-32768 ←←')

    return elegirModelo


def modelConfig (cliente, modelo, inputMensaje):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role": "user", "content": inputMensaje}],
        stream = False
    )


# indica que en algún lugar del código se está tratando de acceder a un atributo choices
# de un objeto que es una tupla. Esto sugiere que la función modelConfig está devolviendo
# una tupla en lugar de una lista de objetos con el atributo choices.

#Comprueba si ya tenemos una lista de mensajes guardada en st.session_state.
#Si no la tenemos, crea una lista vacía para guardar nuestros mensajes.
def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        if frase.choices[0].delta.content:
            respuesta_completa += frase.choices[0].delta.content
        yield frase.choices[0].delta.content
    return respuesta_completa

def mostrar_historial():
        for mensaje in st.session_state.mensajes:
                with st.chat_message(mensaje["role"], avatar=mensaje["avatar"]):
                        st.markdown(mensaje["content"])

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def area_chat():
        contenedorDelChat = st.container(height=300,border=True)
        # Abrimos el contenedor del chat y mostramos el historial.
        with contenedorDelChat:
                mostrar_historial()

def main():
    modelo = setearPagina()
    clientUser = createUserGroq()
    inicializar_estado()

    mensaje = st.chat_input( placeholder="Escribi tu mensaje...")
    st._bottom.write(f'ChatBot desarrollado por Emanuel Marcello 🤖')
    area_chat()

    if mensaje:
        actualizar_historial("user", mensaje, "👤")
        chat_completo = modelConfig(clientUser, modelo, mensaje)
        actualizar_historial("assistant", chat_completo, "🤖")
    
    chat_completo = None    # inicializamo la variable chat_completo en None
                            # porque no hay mensajes en el chat todavía
    if chat_completo:
        with st.chat_message("assistant"):
            respuesta_completa = st.write_stream(generar_respuesta(chat_completo))
            actualizar_historial("assistant", respuesta_completa,"🤖")

    st.rerun()


if __name__ == "__main__":
    main()


#streamlit run desafio.py

