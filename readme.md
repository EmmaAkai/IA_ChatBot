# Deploy


# Mi ChatBot 🤖

Este proyecto implementa un chatbot interactivo utilizando **Streamlit** y la API de **Groq**. El chatbot permite a los usuarios interactuar con modelos avanzados de lenguaje para tareas de comprensión, generación de texto, y más.

## Características

- **Interfaz interactiva:** Diseñada con Streamlit para una experiencia de usuario intuitiva.
- **Modelos avanzados:** Elige entre tres modelos de lenguaje preentrenados para diferentes tipos de tareas:
  - `llama3-8b-8192`: Tareas generales.
  - `llama3-70b-8192`: Tareas complejas.
  - `mixtral-8x7b-32768`: Comprensión y generación avanzada de texto.
- **Historial de mensajes:** Registra y muestra las conversaciones pasadas.
- **Configuración personalizable:** Cambia fácilmente entre modelos desde la barra lateral.

## Requisitos

- Python 3.8 o superior
- Paquetes de Python:
  - `streamlit`
  - `groq`
- Una clave de API válida para el servicio **Groq** (almacenada en `st.secrets['API_KEY']`).
