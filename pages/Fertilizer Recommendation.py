import streamlit as st
import joblib
import requests
from streamlit_lottie import st_lottie
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.title(" Fertilizers Recommendation ")
def load_utils():
    model = joblib.load("Dump_Files\Fertilizer.pkl")
    scalar = joblib.load("Dump_Files\Ferti.pkl")
    return model , scalar

with open('styling\Home.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)

url = requests.get( 
    "https://lottie.host/192fc64f-66ea-45f9-8cae-eb6338a3fcbb/xYRrr9cAs6.json") 
url_json = dict() 
  
if url.status_code == 200: 
    url_json = url.json() 
else: 
    print("Error in the URL")

with st.container():
    st.write("---")
    left_col , right_col = st.columns((3 , 4))
    with left_col:
        crop = st.text_input("Enter the crop name ")
        N = st.number_input("Enter the nitrogen present in soil")
        P = st.number_input("Enter the phosphrous present in soil")
        K = st.number_input("Enter the potassium present in soil")
        button = st.button("Predict fertilizer")
    with right_col:
        st_lottie(url_json)

if(button):
    dataset = pd.read_csv(r"Dataset\crop.csv")
    cropname = dataset.iloc[: , 0:1]
    ratio = dataset.iloc[: , 1:]

    result = cropname.loc[cropname.eq(crop).any(axis=1)].index.values
    result = int(result)
    new_nitro = ratio._get_value(result , 'N') - N
    new_phop = ratio._get_value(result , 'P') - P
    new_potash = ratio._get_value(result , 'K') - K
    model , scalar = load_utils()

    res1 = scalar.inverse_transform(model.predict([[new_nitro,new_phop,new_potash]]))
    display = ""
    for i in res1:
        display = i + display
    st.write("# The Predicted Fertilizer is ")
    with st.container():
        st.write("---")
        col1 , col2 = st.columns(2)
        col1.metric(label="Fertilizer" , value=display)
        with open('styling\Fertilizer.css') as f:
            st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)
