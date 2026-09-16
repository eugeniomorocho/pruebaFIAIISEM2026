# pip install streamlit (ejecutar en la terminal)
import streamlit as st
import numpy as np

st.title("Prueba de Streamlit")
st.write("Esta es una prueba de Streamlit para mostrar un mensaje en la aplicación web.")   

# PLot the sine wave of the frequency input by a slider
frequency = st.slider("Select a frequency", 1, 10, 5)
x = np.linspace(0, 10, 100)
y = np.sin(frequency * x)
st.line_chart(y)

# Para ejecutar la aplicación, guarda este código en un archivo llamado pruebaFIA.py y luego ejecuta el siguiente comando en la terminal:
# streamlit run pruebaFIA.py