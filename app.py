import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Proyecto Sprint 7")   # Título principal
st.header("🚗 Análisis de Vehículos")      # Encabezado grande
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.checkbox('Construir Histograma')  # Crear un boton
dis_button = st.checkbox('Construir Grafico de Dispersión')

if hist_button:  # al hacer click en el boton
    # Escribir mensaje
    st.write(
        'Creación de un Histograma para el conjunto de Datos de anuncios de ventas de coches')
    # Crear un histograma
    fig = px.histogram(car_data, x='odometer')
    # Mostrar el gráfico Ploty interactivo
    st.plotly_chart(fig, use_container_width=True)

if dis_button:  # al hacer click en el boton
    # Escribir mensaje
    st.write('Creación de un Gráfico de dispersión para el conjunto de Datos de anuncios de ventas de coches')
    # Crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico Ploty interactivo
    st.plotly_chart(fig, use_container_width=True)
