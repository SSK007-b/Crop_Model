import json 
import requests 
import streamlit as st 
from streamlit_lottie import st_lottie
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="Crop Recommendation",
    page_icon=""
)

crop_name = []

st.markdown("# MultiCrop Recommendation")
st.sidebar.header("MultiCrop Recommendation")

with open('Home.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)


def load_utils():
    model = joblib.load("Dump_Files/grain.pkl")
    scalar = joblib.load("Dump_Files/gscalar.pkl")
    return model , scalar

def load_data():
    model1 = joblib.load("Dump_Files/medicine.pkl")
    scalar1 = joblib.load("Dump_Files/mscalar.pkl")
    return model1 , scalar1

def load_data1():
    model2 = joblib.load("Dump_Files/fruit.pkl")
    scalar2 = joblib.load("Dump_Files/fscalar.pkl")
    return model2 , scalar2

def load_data2():
    model3 = joblib.load("Dump_Files/veg.pkl")
    scalar3 = joblib.load("Dump_Files/vscalar.pkl")
    return model3 , scalar3

url = requests.get( 
    "https://lottie.host/c294a57d-bd70-4672-a6b0-8ed5e76d211c/piTlNWKdp7.json") 
url_json = dict() 
  
if url.status_code == 200: 
    url_json = url.json() 
else: 
    print("Error in the URL") 

with st.container():
    st.write("---")
    left_col , right_col = st.columns((3 , 4))
    with left_col:
        ph = st.number_input("Enter the ph of the soil")
        n = st.number_input("Enter the nitrogen present in soil")
        p = st.number_input("Enter the phosphrous present in soil")
        k = st.number_input("Enter the potassium present in soil")
        temp = st.number_input("Enter the temprature of the area")
        hum = st.number_input("Enter the humidity in percentage of the area")
        rain = st.number_input("Enter the Annual rainfall in mm")
    with right_col:
        st_lottie(url_json)

button = st.button("Predict crop")
if(button):
    model , scalar = load_utils()
    model1 , scalar1 = load_data()
    model2 , scalar2 = load_data1()
    model3 , scalar3 = load_data2()

    res1 = scalar.inverse_transform(model.predict([[n,p,k,ph,temp,hum,rain]]))
    res2 = scalar1.inverse_transform(model1.predict([[n,p,k,ph,temp,hum,rain]]))
    res3 = scalar2.inverse_transform(model2.predict([[n,p,k,ph,temp,hum,rain]]))
    res4 = scalar3.inverse_transform(model3.predict([[n,p,k,ph,temp,hum,rain]]))
    display = ""
    for i in res1:
        display = i + display
    display1 = ""
    for i in res2:
        display1 = i + display1
    display2 = ""
    for i in res3:
        display2 = i + display2
    display3 = ""
    for i in res4:
        display3 = i + display3
    st.header('The Predicted crop are ')
    with st.container():
        st.write("---")
        col1 , col2 , col3 , col4 = st.columns(4)
        col1.metric(label="  Crop1  " , value=display)
        col2.metric(label="Crop2" , value=display1)
        col3.metric(label="Crop3" , value=display2)
        col4.metric(label="Crop4" , value=display3)
        with open('styling\crop.css') as f:
            st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)


    


