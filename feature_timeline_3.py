#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:07:42 2021

@author: jamesopacich
"""

### IMPORTS ###

import pandas as pd
import streamlit as st
import datetime
import plotly.express as px

### Name Dashboard and Give it a Description ###

st.title("Art Drop Project Delivery Schedule")
st.write("Identifying Feature Importance and Creating Timelines for Accountability.")

### All Initiatives Dataframe ###

df = pd.DataFrame([
    dict(Task="Social Marketplace App Development", Start= st.sidebar.date_input('Social Marketplace Start Date', 
        datetime.date(2021,7,15) ), Finish = st.sidebar.date_input('Social Marketplace Finish Date', datetime.date(2021,9,28) ), Resource = "App"),
    dict(Task="App User Recruitment and Marketing", Start= st.sidebar.date_input('User Marketing Start Date', datetime.date(2021,8,15) ), 
         Finish = st.sidebar.date_input('User Marketing Finish Date', datetime.date(2021,10,28) ) , Resource="App"),
    dict(Task="Initial Exhibiting", Start= st.sidebar.date_input('Initial Exhibiting Start Date', datetime.date(2021,9,5) ), 
         Finish = st.sidebar.date_input('Initial Exhibiting Finish Date', datetime.date(2021,12,15) ) , Resource="Global Art Gallery"),
    dict(Task="QR Code Functionality", Start= st.sidebar.date_input('QR Start Date', datetime.date(2021,8,7) ), 
         Finish = st.sidebar.date_input('QR Finish Date', datetime.date(2021,9,5) ) , Resource="App"),
    dict(Task="Retail Flagship", Start= st.sidebar.date_input('Retail Flagship Start Date', datetime.date(2021,8,15) ), 
         Finish = st.sidebar.date_input('Retail Flagship Finish Date', datetime.date(2022,2,28) ) , Resource="Art_Drop Hub"),
    dict(Task="Classrooms", Start= st.sidebar.date_input('Classroom Start Date', datetime.date(2021,12,5) ), 
         Finish = st.sidebar.date_input('Classroom Finish Date', datetime.date(2022,1,15) ) , Resource="Art_Drop Hub"),
    dict(Task="3D print center", Start='2021-09-30', Finish='2021-10-30', Resource="Art_Drop Hub"),
])

### Create an option to show dataframe ###
if st.checkbox('Show dataframe'):
    st.write(df)

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", title='All Initiatives')
fig.update_yaxes(autorange="reversed")
fig.show()

# output to streamlit
st.plotly_chart(fig)

# option to output plotly to html by uncommenting below. 
# fig.write_html("path/to/file.html")
