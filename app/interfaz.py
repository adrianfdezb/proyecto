import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from PIL import Image
import requests
import pickle
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

marcas = ['Opel', 'Tesla', 'SsangYong', 'KIA', 'Lexus', 'Mitsubishi',
       'Nissan', 'Renault', 'SEAT', 'Skoda', 'Jeep', 'Abarth', 'Volvo',
       'Maserati', 'Dacia', 'Infiniti', 'Toyota', 'Land Rover', 'Jaguar',
       'Iveco', 'Citroen', 'Audi', 'Alfa Romeo', 'DS', 'BMW', 'Alpine',
       'Peugeot', 'Bentley', 'CUPRA', 'Honda', 'Hyundai', 'Mercedes-Benz',
       'Fiat', 'Ford', 'Volkswagen', 'Porsche', 'Mazda', 'Subaru',
       'Suzuki', 'Aston Martin', 'MG', 'Cadillac', 'Mahindra', 'Dodge',
       'KTM', 'Ferrari', 'Lamborghini', 'Rover', 'MINI', 'Saab',
       'Renault Trucks', 'Hummer', 'Tata', 'Galloper', 'Lancia',
       'Daihatsu', 'Daewoo', 'Chevrolet', 'Chrysler', 'Corvette',
       'McLaren', 'Lada', 'Isuzu', 'Santana', 'VAZ', 'Lotus']

#Representamos la informacion obtenida

st.title('Estimador de precios')
st.subheader('¿Por cuánto puedes anunciar tu vehículo?')

st.markdown('Con nuestra aplicacion puedes saber el precio óptimo para vender tu coche')
st.markdown('¡Introduce los datos!')

img= Image.open('utils/coches.jpeg')
st.image(img)

#image = Image.open("coches.jpeg")
#st.image(image, caption=None, width=400, output_format="JPEG")

marca = st.selectbox('Elige una marca', marcas)
km = st.slider('¿Cuántos kms tiene?', 10000, 350000, 100000)
edad = st.slider('¿Cuántos años tiene?', 0, 20, 5)
fuel = st.selectbox('Tipo de combustible', ['Gasolina', 'Diésel', 'Eléctrico', 'Otros'])
shift = st.selectbox('Tipo de cambio', ['manual', 'automatic'])
st.markdown(f'Vehículo elegido: {marca}, Kms: {km}, Antigüedad: {edad}, Combustible: {fuel}, Cambio: {shift}' )

x_test = {"make": marca, "fuel": fuel, "kms": km, "shift":shift,  "antiguedad": edad}

x_test = pd.DataFrame([x_test])

#LOAD MODEL

from utils.auxiliar import obtener_clase 

mi_instancia = obtener_clase()

prediccion = mi_instancia.predict(x_test)

#st.text(f'Precio sugerido al que puedes anunciar tu coche')

st.markdown("*Pulsa para conocer el precio sugerido al que puedes anunciar tu* ***coche***.")

#st.button("Reset", type="primary")
if st.button('Calcular:'):

    st.markdown(f'Estimación: {int(prediccion[0])} €')
    st.markdown('''¡Mucha suerte! :money_with_wings:''')

else:
    st.write(' ')

st.divider()

st.title('Radiografía del mercado en España')
st.components.v1.html("""<iframe title="Report Section" width="850" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiOWRjNWVmOGYtMzMwMy00YzY5LTliNTItZmVjYTVmMTNhY2FjIiwidCI6ImJiYjEzOGJhLWZjMDYtNDM2ZS04ODhlLTAyYmVjMzFlYTIzYSIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>""", width=850, height=1000, scrolling=False)
