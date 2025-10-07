import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import time

st_autorefresh(interval = 2000, key = 'auto_refresh')


st.header('Dashboard')

dump_metrics = 'http://127.0.0.1:5000/metrics/dump'

cur_metrics = 'http://127.0.0.1:5000/metrics/data'

health = 'http://127.0.0.1:5000/health'

action = 'http://127.0.0.1:5000/tasks/action'


response = requests.get(cur_metrics)  
data = response.json()

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("CPU usage", data["cpu"], border=True)
b.metric("Memory usage", data["memory"], border=True)

c.metric("Disk usage", data["disk"], border=True)
d.metric("Status", data["status"], border=True)




if st.button("Get old Stats"):
    try:
        dump_response = requests.get(dump_metrics, timeout = 10)
        if dump_response.status_code == 200:
            data = dump_response.json()

            df = pd.DataFrame(data)
            st.subheader('From DB')
            st.success('Data fetched successfully')
            st.dataframe(df)

        else:
            st.error("Failed to get data.")
    except Exception as e:
        st.error(f"Error: {e}")
