import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us/vehicles_us.csv')


hist_checkbox = st.checkbox('Construir histograma') # crear un botón
    
if hist_checkbox: # al hacer clic en el botón
    # escribir un mensajepytho
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_checkbox = st.checkbox('Construir diagrama de dispersion') # crear un botón

if disp_checkbox:
    st.write('Diagrama de Dispersion')
    fig = px.scatter(car_data, x="price", y="odometer")
    st.plotly_chart(fig, use_container_width=True)
