import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import requests
import validators


df = pd.read_csv('vehiculos-de-segunda-mano-sample.csv')

marcas = list(df['make'].unique())


#Representamos la informacion obtenida

st.title("¿Por cuánto puedes anunciar tu vehículo?")
st.markdown('Con nuestra aplicacion puedes saber el precio óptimo para vender tu coche')
st.markdown('**¡Introduce los datos!**')

image = Image.open("coches.jpeg")
st.image(image, caption=None, width=400, output_format="JPEG")

marca = st.selectbox('Elige una marca', marcas)     
km = st.slider('¿Cuántos kms tiene?', 0, 650000, 5000)
edad = st.slider('¿Cuántos años tiene?', 0, 60, 5)
fuel = st.selectbox('Tipo de combustible', list(df['fuel'].dropna().unique()))
shift = st.selectbox('Tipo de cambio', list(df['shift'].dropna().unique()))
power = st.slider('¿Cuántos caballos tiene?', 60, 200, 110)
st.markdown(f'Vehículo elegido: {marca}, Kms: {km}, Antigüedad: {edad}, Combustible: {fuel}, Cambio: {shift}, Caballos: {power}')

from sklearn import linear_model

def entrenar_modelo():
    reg = linear_model.Lasso(alpha=0.1)
    reg.fit([[0, 23], [2323, 9999]], [0, 345])
    return reg

entrenado = entrenar_modelo()

def prediccion(x, y):
    pred = entrenado.predict([[x, y]])
    return pred


st.title(f'Precio óptimo al que puedes anunciar tu coche')
#st.button("Reset", type="primary")
if st.button('Calcular:'):
    st.write(f'Predicción: {prediccion(power,edad)}')
else:
    st.write(' ')