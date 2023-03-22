# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:51:38 2023

@author: Elias
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['Diabetes Prediction'],
                          
                          icons=['activity'],
                         
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Fname = st.text_input('Name')
        
    with col2:
        Email = st.text_input('Email Address')
        
    with col3:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col1:
        Glucose = st.text_input('Glucose Level')
    
    with col2:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col3:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col2:
        BMI = st.text_input('BMI value')
    
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col1:
        Age = st.text_input('Age of the Person')
        
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
#Email notification   
import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "elias.alam20@gmail.com"
sender_password = "eabr30102000"
receiver_email = Email

message = """\
Subject: Hi there

I'm sending an email through Python code.
"""

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)


    
