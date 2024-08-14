import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)
icon = Image.open("Icon\logo.png")
st.sidebar.image(icon)
st.sidebar.header("Home")

icon = Image.open("Icon\sampul.png")
st.image(icon)
st.write("Sistem ini dibuat agar memudahkan pengguna dalam melakukan prediksi risiko gagal bayar P2P Lending dengan model machine learning. Model prediksi menggunakan model Stacking Ensemble dan Random Forest Feature Selection. Dalam sistem ini terdapat 2 pilihan input data yaitu Manual dan CSV. Manual Input bisa digunakan jika pengguna ingin memprediksi status pinjaman dengan cara menginputkan data satu persatu. Sedangkan untuk CSV Input dapat digunakan jika pengguna ingin memprediksi status pinjaman dengan banyak data sekaligus yang berformat csv. ")

