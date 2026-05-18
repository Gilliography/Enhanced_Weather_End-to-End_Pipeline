import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Real-Time Weather Dashboard",
    layout="wide"
)

st.title("🌦️ Real-Time Weather Dashboard")

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

query = """
SELECT *
FROM weather_data
ORDER BY time DESC
LIMIT 200
"""

df = pd.read_sql(query, engine)

if df.empty:
    st.warning("No weather data found.")
    st.stop()

df["time"] = pd.to_datetime(df["time"])

metric = st.sidebar.selectbox(
    "Select Metric",
    [
        "temperature_2m",
        "relative_humidity_2m",
        "pressure_msl"
    ]
)

st.metric(
    "Latest Value",
    f"{df[metric].iloc[0]:.2f}"
)

st.line_chart(
    df.set_index("time")[metric]
)

st.dataframe(df)