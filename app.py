try:
    from sklearn.compose._column_transformer import _RemainderColsList
except ImportError:
    class _RemainderColsList:
        def __init__(self, *args, **kwargs):
            pass
        pass

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder

@st.cache_resource
def load_model():
    return joblib.load("xgb_regressor_model.pkl")

model = load_model()


st.set_page_config(page_title="Air Quality Prediction Dashboard", layout="wide")
st.title("🌫️ Air Quality Prediction (PM2.5)")
st.write("Enter environmental conditions and city to forecast PM2.5 concentration.")


cities = [
    "Denver", "Los Angeles", "New York", "Chicago", "Houston", "Phoenix", "San Antonio",
    "San Diego", "Dallas", "San Jose", "Washington", "Austin", "Boston", "Seattle"
]

with st.form("prediction_form"):
    city_name = st.selectbox("Select City", cities)

    temperature_max = st.number_input("🌡️ Temperature Max (°C)", value=25.0)
    temperature_min = st.number_input("🌡️ Temperature Min (°C)", value=15.0)
    precipitation_sum = st.number_input("🌧️ Precipitation Sum (mm)", value=0.5)
    rain_sum = st.number_input("🌦️ Rain Sum (mm)", value=0.3)
    snowfall_sum = st.number_input("❄️ Snowfall Sum (mm)", value=0.0)
    precipitation_hours = st.number_input("🌧️ Precipitation Hours", value=0.0)
    wind_speed_max = st.number_input("💨 Max Wind Speed (km/h)", value=20.0)
    wind_gusts_max = st.number_input("🌬️ Max Wind Gusts (km/h)", value=28.0)
    wind_direction_dominant = st.number_input("🧭 Wind Direction (°)", value=180.0)

    submit_btn = st.form_submit_button("🔮 Predict PM2.5 Level")


if submit_btn:
    
    rain_sum_log = np.log1p(rain_sum)
    precipitation_hours_log = np.log1p(precipitation_hours)
    wind_speed_max_log = np.log1p(wind_speed_max)
    snowfall_sum_log = np.log1p(snowfall_sum)
    precipitation_sum_log = np.log1p(precipitation_sum)
    wind_gusts_max_log = np.log1p(wind_gusts_max)

    input_df = pd.DataFrame([{
        "city_name": city_name,
        "temperature_max": temperature_max,
        "temperature_min": temperature_min,
        "wind_direction_dominant": wind_direction_dominant,
        "precipitation_sum": precipitation_sum, 
        "rain_sum": rain_sum,                  
        "snowfall_sum": snowfall_sum,           
        "precipitation_hours": precipitation_hours, 
        "wind_speed_max": wind_speed_max,           
        "wind_gusts_max": wind_gusts_max,           
        "log_rain_sum": rain_sum_log,
        "log_precipitation_hours": precipitation_hours_log,
        "log_wind_speed_max": wind_speed_max_log,
        "log_snowfall_sum": snowfall_sum_log,
        "log_precipitation_sum": precipitation_sum_log,
        "log_wind_gusts_max": wind_gusts_max_log,
    }])
    
    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.warning("The model failed during prediction. Please check your input columns and model structure.")
        st.stop() 

    st.subheader("🎯 Predicted PM2.5 Concentration")
    st.metric("PM2.5 Value", f"{prediction:.2f} µg/m³")

    if prediction <= 12.0:
        status = "Good 😊"
        color = "green"
    elif prediction <= 35.4:
        status = "Moderate 😐"
        color = "gold"
    elif prediction <= 55.4:
        status = "Unhealthy for Sensitive Groups 😷"
        color = "orange"
    elif prediction <= 150.4:
        status = "Unhealthy 🤢"
        color = "red"
    else:
        status = "Hazardous ☠️"
        color = "purple"

    st.markdown(
        f"""
        <div style='background-color:{color}; padding:15px; border-radius:8px'>
        <h3 style='color:white; text-align:center;'>Air Quality Status: {status}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )