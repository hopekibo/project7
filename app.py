# This is your app.py file
import os
print('Hello from app.py')

import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de datos de vehículos')
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)