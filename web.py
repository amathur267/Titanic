# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:47:20 2021

@author: hp
"""

import streamlit as st
import pandas as pd
import numpy as np
import random as rd
import pickle
import os 
st.write("""# Would you have survived the Titanic Disaster?""")
st.image('https://res.cloudinary.com/dk-find-out/image/upload/q_70,c_pad,w_1200,h_630,f_auto/MA_00079563_yvu84f.jpg')
with open('C:/Users/hp/Downloads/ml/titanic/model.pkl', 'rb') as file:  
    m = pickle.load(file)

name= st.text_input("Your Name")
pid=st.number_input("Your Passenger Id",step=1)
age = st.slider("Your Age", 1,75,30)
Sex = st.selectbox("Select your Gender",["Male","Female"])
SibSp = st.number_input("How many siblings or spouses are travelling with you?",min_value=0,max_value=8)
Parch = st.number_input("How many parents or children are travelling with you?",min_value=0,max_value=8)
fare = st.slider("Fare in 1912 $",0,600,40)
male = 0 if Sex == "Female" else 1
Pclass = st.selectbox("Which Class is your ticket from?", [1,2,3])
boarding = st.selectbox("Where did you board the Titanic?", ["Cherbourg","Queenstown","Southampton"])
Embarked_C = 1 if boarding == "Cherbourg" else 0; Embarked_Q = 1 if boarding == "Queenstown" else 0; Embarked_S = 1 if boarding == "Southampton" else 0
data = {"PassengerId":pid,"Pclass":Pclass,"Age":age,"SibSp":SibSp,"Parch":Parch,"Fare":fare,"male":male,"Q":Embarked_Q,"S":Embarked_S}
data = pd.DataFrame(data, index = [0])
pred=m.predict(data)
if st.button('Predict'):
    if(pred==0):
        st.write("""# Uh Oh! You donot survive """ +name+"""!!!""" )
        st.markdown("![Alt Text](https://media.giphy.com/media/OJw4CDbtu0jde/giphy.gif)")
    else:
        st.write("""# Yay, You get to live another day """ +name+"""!!!""")
        st.markdown("![Alt Text](https://media.giphy.com/media/kBIChwCximu5gfIlXW/giphy.gif)")
