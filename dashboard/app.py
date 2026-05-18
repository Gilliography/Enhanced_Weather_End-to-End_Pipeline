import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


set__page_config = st.set_page_config(
    page_title="Real-Time Weather Dashboard",
    layout="wide",
)

set_title = st.title("🌦️ Real-Time Weather Dashboard")

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

query =
    """
    SELECT city *
    FROM weather_data
    ORDER BY time DESC
    LIMIT 200;
    """
df = pd.read_sql_query(query, engine)
if df.empty:
    st.warning("No weather data available.")
    st.stop()

metric = st.sidebar.selectbox(
    "Select metric",
    [
        "temperature_2m",
        "relative_humidity_2m",
        "pressure_msl",
    ]
)

st.metric(
    "latest value",
    f"{df[metric].iloc[0]:.2f}",
)

st.line_chart(df[metric]
)
st.dataframe(df)