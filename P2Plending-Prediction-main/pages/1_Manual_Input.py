import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
import joblib

from PIL import Image

st.set_page_config(page_title="Manual Input", page_icon="🔢")
icon = Image.open("Icon\logo.png")
st.sidebar.image(icon)
st.sidebar.header("Manual Input")


st.markdown('## Default Risk Prediction P2P Lending')
days_past_due = st.number_input('Days Past Due')
principal_balance = st.number_input('Principal Balance')
principal_paid = st.number_input('Principal Paid')

#Predict button
if st.button('Predict'):
    model = joblib.load('Model\model3.joblib')
    input = np.array([[days_past_due, principal_balance, principal_paid]])
    hasil = model.predict(input)
 
    if hasil == 0:
        st.header('Prediksi pinjaman ini adalah "Default"')
    else:
        st.header('Prediksi pinjaman ini adalah "Non-default"')
        
