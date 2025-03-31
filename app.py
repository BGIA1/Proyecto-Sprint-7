import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de venta de coches en EE. UU.')

# Casilla para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión odómetro vs precio')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
