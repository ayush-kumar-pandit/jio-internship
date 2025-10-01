import streamlit as st

st.header('Dashboard')
name = st.text_input('Enter Your Name:')
st.text(f"Good evening, {name}")