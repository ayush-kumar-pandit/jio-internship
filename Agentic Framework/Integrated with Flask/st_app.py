import streamlit as st
import requests
import pandas as pd



st.header('Dashboard')

dump_metrics = 'http://127.0.0.1:5000/metrics/dump'

cur_metrics = 'http://127.0.0.1:5000/metrics/data'

health = 'http://127.0.0.1:5000/health'

action = 'http://127.0.0.1:5000/tasks/action'


response = requests.get(cur_metrics)  
data = response.json()
# st.write("CPU:", data["cpu"])
# st.write("Memory:", data["memory"])
# st.write("Disk:", data["disk"])
st.dataframe(data)


if st.button("Get old Stats"):
    try:
        dump_response = requests.get(dump_metrics, timeout = 10)
        if dump_response.status_code == 200:
            data = dump_response.json()

            df = pd.DataFrame(data)
            st.subheader('From DB')
            st.dataframe(df)
        else:
            st.error("Failed to get data.")
    except Exception as e:
        st.error(f"Error: {e}")
