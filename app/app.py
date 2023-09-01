import streamlit as st
import pandas as pd

from utils.viz import *
from ml.inference import make_inference


st.title('Proyecto Codenotch')

st.write("Here's our first attempt at using data to create a table:")


chart_data = scatter_plot_price_distance()
st.line_chart(chart_data)