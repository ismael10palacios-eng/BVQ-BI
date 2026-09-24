import streamlit as st
import pandas as pd
st.title("Bolsa de Valores Quito BI")
st.sidebar.title("parametros")
st.write("Elaborado por: Adrian Encalada")

archivo = st.file_uploader("Cargue su archivo")
if archivo is not None:
 tabla = pd.read_csv(archivo)
 st.write(tabla)
