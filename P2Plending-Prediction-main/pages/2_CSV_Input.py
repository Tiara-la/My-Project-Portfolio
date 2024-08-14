import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
import joblib

from PIL import Image

st.set_page_config(page_title="CSV Input", page_icon="📤")
icon = Image.open("Icon\logo.png")
st.sidebar.image(icon)
st.sidebar.header("CSV Input")


st.markdown('## Default Risk Prediction P2P Lending')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    df = dataframe.drop(['Unnamed: 0'], axis=1)
    st.write(df)


#Predict button
if st.button('Predict'):
    model = joblib.load('Model\model3.joblib')
    y_pred = model.predict(df)
    # st.write(y_pred)

    chart_data = pd.DataFrame(y_pred, columns=['y_pred'])
    pred = chart_data.value_counts()
    data_pred = pd.DataFrame(pred, columns=['prediksi'])
    # Menambahkan kolom baru
    data_pred['label'] = ['0','1']

    hasil = pd.concat([df, chart_data], axis=1)
    st.write(hasil)


    height = chart_data.value_counts()
    labels = ( '0', '1')
    y_pos = np.arange(len(labels))

    fig = plt.figure(figsize=(7,4), dpi=80)
    plt.ylim(0,150000)
    plt.title('Hasil Prediksi', fontweight='bold')
    plt.xlabel('loan status', fontweight='bold')
    plt.ylabel('count', fontweight='bold')
    plt.bar(y_pos, height, color=['deepskyblue', 'royalblue'])
    def addlabels(y_pos,height):
        for i in range(len(y_pos)):
            plt.text(i,height[i],height[i])
    addlabels(y_pos, height)
    plt.xticks(y_pos, labels)
    st.pyplot(fig)
 