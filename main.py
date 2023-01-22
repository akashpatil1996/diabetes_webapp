import pickle
import streamlit as st

model = pickle.load(open('diabetes_model.sav','rb'))

st.markdown("<h1 style='text-align: center; color: white;'>Welcome to Diabetes Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: grey;'>Enter the following details</h5>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
with col2:
    Glucose = st.text_input('Glucose Level')
with col1:
    BloodPressure = st.text_input('Blood Pressure')
with col2:
    SkinThickness = st.text_input('Skin Thickness')
with col1:
    Insulin = st.text_input('Insulin Level')
with col2:
    BMI = st.text_input('BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
with col2:
    Age = st.text_input('Age')

if st.button('Check Result'):
    pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if pred[0] == 1:
        st.error('You are Diabetic. Do not panic as this model is only 76% accurate')
    else:
        st.success('You are not Diabetic')

