import streamlit as st
import requests



st.header('Dashboard')
Data = requests.get('http://127.0.0.1:5000/')
st.form(Data)