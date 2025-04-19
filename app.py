import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('best_model.joblib')

st.title("🌾 Agricultural Yield Predictor")

# Create input fields for user
st.header("Enter Farm Details")

farm_area = st.number_input("Farm Area (acres)", min_value=0.0)
fertilizer = st.number_input("Fertilizer Used (tons)", min_value=0.0)
pesticide = st.number_input("Pesticide Used (kg)", min_value=0.0)
water = st.number_input("Water Usage (cubic meters)", min_value=0.0)
crop_type = st.selectbox("Crop Type", ['Wheat', 'Rice', 'Corn', 'Barley'])  # Customize based on your dataset
irrigation = st.selectbox("Irrigation Type", ['Drip', 'Sprinkler', 'Flood'])
soil = st.selectbox("Soil Type", ['Loamy', 'Sandy', 'Clay'])
season = st.selectbox("Season", ['Rabi', 'Kharif', 'Zaid'])

# Derived features
water_eff = 0 if water == 0 else 1 / water
fert_eff = 0 if fertilizer == 0 else 1 / fertilizer

# Collect data
data = pd.DataFrame([{
    'Farm_Area(acres)': farm_area,
    'Fertilizer_Used(tons)': fertilizer,
    'Pesticide_Used(kg)': pesticide,
    'Water_Usage(cubic meters)': water,
    'Water_Efficiency': farm_area / (water + 1),
    'Fertilizer_Efficiency': farm_area / (fertilizer + 1),
    'Crop_Type': crop_type,
    'Irrigation_Type': irrigation,
    'Soil_Type': soil,
    'Season': season
}])

# Predict
if st.button("Predict Yield"):
    yield_pred = model.predict(data)[0]
    st.success(f"🌾 Predicted Yield: {yield_pred:.2f} tons")
