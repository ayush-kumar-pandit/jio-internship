import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import time

st_autorefresh(interval = 2000, key = 'auto_refresh')


dump_metrics = 'http://127.0.0.1:5000/metrics/dump'

cur_metrics = 'http://127.0.0.1:5000/metrics/data'

health = 'http://127.0.0.1:5000/health'

action = 'http://127.0.0.1:5000/tasks/action'




buttons = st.container(horizontal=True, horizontal_alignment="right")
buttons.header('Dashboard')
if buttons.button('Start'):
    requests.post(url = action,data = {'action' : 'start'})
    buttons.success('Collector started collecting data!!')
    
if buttons.button('Stop'):
    requests.post(url = action,data = {'action' : 'stop'})
    buttons.success('Collector stoped collecting data!!')



with st.container():
    left, right = st.columns(2,vertical_alignment = 'top')

    response = requests.get(cur_metrics)  
    data = response.json()


    a, b = left.columns(2)
    c, d = left.columns(2)

    a.metric("CPU usage", data["cpu"], border=True)
    b.metric("Memory usage", data["memory"], border=True)

    c.metric("Disk usage", data["disk"], border=True)
    d.metric("Status", data["status"], border=True)



    try:
        dump_response = requests.get(dump_metrics, timeout = 10)
        if dump_response.status_code == 200:
            data = dump_response.json()

            df = pd.DataFrame(data)
            right.subheader('Previous Stats')
            right.dataframe(df,hide_index = True)

        else:
            st.error("Failed to get data.")
    except Exception as e:
        st.error(f"Error: {e}")
