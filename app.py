
import streamlit as st
import pandas as pd
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime

st.set_page_config(page_title="Universal IoT Dashboard", page_icon="📊", layout="wide")

st.markdown("<style>.stMetric {background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}</style>", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Timestamp', 'Temperature', 'Humidity', 'Signal'])

MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC = "python/iot/dashboard/demo"

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        payload['Timestamp'] = datetime.now().strftime("%H:%M:%S")
        new_row = pd.DataFrame([payload])
        st.session_state.history = pd.concat([st.session_state.history, new_row], ignore_index=True).tail(50)
    except:
        pass

if 'mqtt_client' not in st.session_state:
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.subscribe(MQTT_TOPIC)
    client.loop_start()
    st.session_state.mqtt_client = client

st.title("🌐 Universal Real-Time IoT Dashboard")
m1, m2, m3 = st.columns(3)

if not st.session_state.history.empty:
    last = st.session_state.history.iloc[-1]
    m1.metric("Temperature", f"{last['Temperature']} °C")
    m2.metric("Humidity", f"{last['Humidity']} %")
    m3.metric("Signal", f"{last['Signal']} dBm")

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("📈 Environmental Trends")
    if not st.session_state.history.empty:
        st.line_chart(st.session_state.history.set_index('Timestamp')[['Temperature', 'Humidity']])
with c2:
    st.subheader("📋 Raw Data Feed")
    st.dataframe(st.session_state.history.sort_index(ascending=False), use_container_width=True)

time.sleep(2)
st.rerun()
