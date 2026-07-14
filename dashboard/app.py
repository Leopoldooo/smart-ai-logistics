from streamlit_autorefresh import st_autorefresh

import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Smart AI Logistics",
    page_icon="🚛",
    layout="wide"
)

st_autorefresh(interval=5000, key="refresh")

st.title("🚛 Smart AI Logistics Dashboard")

st.caption(
    "Real-time monitoring of driver behavior using FastAPI, Machine Learning, SQLite, and n8n."
)

conn = sqlite3.connect("logistics.db")

df = pd.read_sql_query(
    "SELECT * FROM driver_logs",
    conn
)

conn.close()

if df.empty:
    st.warning("No driver data found.")
    st.stop()

total_logs = len(df)

risky = len(df[df["prediction"] == "Risky Driver"])

safe = len(df[df["prediction"] == "Safe Driver"])

average = round(df["risk_score"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Logs", total_logs)

col2.metric("Risky Drivers", risky)

col3.metric("Safe Drivers", safe)

col4.metric("Average Risk Score", average)

st.divider()

st.subheader("Driver Logs")

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Risk Score")

fig = px.bar(
    df,
    x="id",
    y="risk_score",
    color="prediction",
    title="Risk Score per Driver"
)

st.plotly_chart(fig, use_container_width=True)