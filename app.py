import streamlit as st
import pandas as pd
import plotly.express as px

# Leemos el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Vehículos en Venta')

# Checkbox para el histograma
show_hist = st.checkbox('Mostrar Histograma de Odómetro')

if show_hist:
    st.write('Histograma de kilometraje de los vehículos') # mensaje
    fig = px.histogram(car_data, x='odometer') # creamos un histograma
    st.plotly_chart(fig, use_container_width=True)  # mostramos un gráfico Plotly interactivo

# Checkbox para gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión Precio vs Odómetro')

if show_scatter:
    st.write('Relación entre el kilometraje y el precio') # mensaje
    fig2 = px.scatter(car_data, x='odometer', y='price') # creamos un gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)  # mostramos un gráfico Plotly interactivo
    