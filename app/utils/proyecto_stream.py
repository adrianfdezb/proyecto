import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt


df = pd.read_csv('vehiculos-de-segunda-mano-sample.csv')

marcas = list(df['make'].unique())


#Representamos la informacion obtenida

st.title("¿Por cuánto puedes anunciar tu vehículo?")
st.markdown('Con nuestra aplicacion puedes saber el precio óptimo para vender tu coche')
st.markdown('**¡Introduce los datos!**')

image = Image.open("coches.jpeg")
st.image(image, caption=None, width=400, output_format="JPEG")

marca = st.selectbox('Elige una marca', marcas)

for m in marcas:
    if marca == m:
        modelos = list(df.model[df['make'] == m].unique())
        modelo = st.selectbox('Elige un modelo', modelos)

      

st.markdown(f'Vehículo elegido: {marca} {modelo}')
km = st.slider('¿Cuántos kms tiene?', 0, 650000, 5000)
edad = st.slider('¿Cuántos años tiene?', 0, 60, 5)
fuel = st.selectbox('Tipo de combustible', list(df['fuel'].dropna().unique()))
shift = st.selectbox('Tipo de cambio', list(df['shift'].dropna().unique()))





