import pandas as pd
import streamlit as st
import joblib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import math
import warnings
from PIL import Image


# load the regression model that we created
model = joblib.load("Completed_model1.joblib")
# caching the model for faster loading
@st.cache
# define the prediction function
def predict(gender,age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    #predict the price of the carat
    if gender == "Male":
        gender =0
    elif gender == "Female":
        gender =1
    elif gender == "Other":
        gender =2
   
    if ever_married == "Yes":
        ever_married = 0
    elif ever_married == "No":
        ever_married =1



    if hypertension == "Yes":
        hypertension = 0
    elif hypertension == "No":
        hypertension =1

    if heart_disease == "Yes":
        heart_disease = 0
    elif heart_disease == "No":
        heart_disease =1
    
    if work_type == "Children":
        work_type = 0
    elif work_type == "Government":
        work_type = 1
    elif work_type == "Never worked":
        work_type = 2
    elif work_type == "Private":
        work_type = 3
    elif work_type == "Self-employed":
        work_type = 4
    
    if Residence_type == "Rural":
        Residence_type =0
    elif Residence_type == "Urban":
        Residence_type =1

    if smoking_status == "formerly smoked":
        smoking_status = 0
    elif smoking_status == "never smoked":
        smoking_status = 1
    elif smoking_status == "Smokes":
        smoking_status = 2
    elif smoking_status == "Unknown":
        smoking_status = 3
    

    data = [[gender,age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]]
    df = pd.DataFrame(data
    , columns = ["gender","age", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"]
    )
    print(df)
    return  model.predict(df)


image = Image.open('Brain-Attack-Stroke.jpg')
new_image = image.resize((600, 400))
st.image(new_image)



st.header('Stroke Prediction in Patients')

st.subheader("Please enter patient's data below")


gender = st.selectbox(
     'Gender',
    ('Female', 'Male', 'Other'))

age = st.selectbox(
     'Age',
    (10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
100))

hypertension = st.selectbox(
     'Hypertension',
    ('Yes', 'No'))

heart_disease = st.selectbox(
     'Heart Disease',
    ('Yes', 'No'))

ever_married = st.selectbox(
     'Marrital Status',
    ('Yes', 'No'))

work_type = st.selectbox(
     'Work Type',
    ('Self-employed', 'Private', 'Government', 'Children', 'Never worked'))

Residence_type = st.selectbox(
     'Residence',
    ('Rural', 'Urban'))

avg_glucose_level = st.number_input('Enter your average glucose level in blood: ', min_value = 2, max_value = 15)

bmi = st.number_input('Enter your body mass index: ',  min_value = 15, max_value = 35)

smoking_status = st.selectbox(
     'Smoking Status',
    ('formerly smoked', 'never smoked', 'Smokes', 'Unknown'))

if st.button('Diagnose'):
    result = predict(gender,age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status)
    if round(result[0]) == 0:
        st.markdown(":green[The patient is not in risk for a stroke]")
    else: 
        st.markdown(":red[The patient is in risk for a stroke. Please perform further medical checks!]")


        #streamlit run "C:\Users\agnes\OneDrive\Desktop\Stroke Projekti\Stroke_Prediction_Application\python2.py"