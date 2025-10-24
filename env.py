import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Environmental Footprint Analyzer", layout="centered")
st.title("🌍 Environmental Footprint Analyzer")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Enter Your Daily Activities")

# Energy & Transport
electricity = st.sidebar.number_input("Electricity usage (kWh/day)", min_value=0.0, max_value=100.0, value=10.0)
transport = st.sidebar.selectbox("Transport Type", ["Car", "Bus", "Bicycle", "Walk"])
distance = st.sidebar.number_input("Distance traveled (km/day)", min_value=0.0, max_value=100.0, value=10.0)

# Water & Waste
water = st.sidebar.number_input("Water usage (liters/day)", min_value=0.0, max_value=500.0, value=60.0)
waste = st.sidebar.number_input("Waste produced (kg/day)", min_value=0.0, max_value=10.0, value=1.0)

# Lifestyle Factors
meat_meals = st.sidebar.number_input("Meat meals per day", min_value=0, max_value=5, value=1)
smoking = st.sidebar.selectbox("Smoking?", ["No", "Yes"])
plastic_items = st.sidebar.number_input("Plastic items used per day", min_value=0, max_value=50, value=5)

# -----------------------------
# Constants for footprint calculations
# -----------------------------
transport_factors = {"Car": 0.21, "Bus": 0.05, "Bicycle": 0.0, "Walk": 0.0}  # kg CO2 per km
electricity_factor = 0.475  # kg CO2 per kWh
water_factor = 1.0  # liter = 1 liter footprint
waste_factor = 2.0  # kg CO2 per kg waste
meat_factor = 5.0  # kg CO2 per meat meal
smoking_factor = 0.5 if smoking=="Yes" else 0.0  # kg CO2 per cigarette per day (example)
plastic_factor = 0.1  # kg CO2 per plastic item

# -----------------------------
# Calculations
# -----------------------------
carbon_transport = distance * transport_factors[transport]
carbon_electricity = electricity * electricity_factor
carbon_waste = waste * waste_factor
carbon_meat = meat_meals * meat_factor
carbon_smoking = smoking_factor
carbon_plastic = plastic_items * plastic_factor

total_carbon = carbon_transport + carbon_electricity + carbon_waste + carbon_meat + carbon_smoking + carbon_plastic
total_water = water * water_factor

# -----------------------------
# Display Key Metrics
# -----------------------------
st.subheader("Your Daily Environmental Footprint")
col1, col2, col3 = st.columns(3)
col1.metric("Total Carbon Footprint (kg CO₂/day)", f"{total_carbon:.2f}")
col2.metric("Total Water Usage (liters/day)", f"{total_water:.2f}")
col3.metric("Total Waste Impact (kg CO₂/day)", f"{carbon_waste:.2f}")

# Optional additional metrics
col4, col5, col6 = st.columns(3)
col4.metric("Meat Impact (kg CO₂/day)", f"{carbon_meat:.2f}")
col5.metric("Plastic Impact (kg CO₂/day)", f"{carbon_plastic:.2f}")
col6.metric("Smoking Impact (kg CO₂/day)", f"{carbon_smoking:.2f}")

# -----------------------------
# DataFrame for visualization
# -----------------------------
footprint_df = pd.DataFrame({
    "Component": ["Transport", "Electricity", "Waste", "Water", "Meat", "Plastic", "Smoking"],
    "Value": [carbon_transport, carbon_electricity, carbon_waste, total_water, carbon_meat, carbon_plastic, carbon_smoking]
})

# -----------------------------
# Pie Chart
# -----------------------------
st.subheader("Footprint Contribution")
fig1, ax1 = plt.subplots(figsize=(4,4))  # smaller size
ax1.pie(footprint_df['Value'],
        labels=footprint_df['Component'],
        autopct='%1.1f%%',
        colors=sns.color_palette("Set2"))
ax1.axis('equal')
st.pyplot(fig1)

# -----------------------------
# Bar Chart
# -----------------------------
st.subheader("Footprint Details")
fig2, ax2 = plt.subplots(figsize=(6,4))  # smaller size
sns.barplot(x="Value", y="Component", data=footprint_df, palette="viridis", ax=ax2)
ax2.set_xlabel("Impact")
ax2.set_ylabel("Component")
st.pyplot(fig2)

# -----------------------------
# Optional Correlation Heatmap
# -----------------------------
st.subheader("Correlation Between Daily Activities")
example_df = pd.DataFrame({
    "Electricity": [electricity],
    "Distance": [distance],
    "Water": [water],
    "Waste": [waste],
    "Meat": [meat_meals],
    "Plastic": [plastic_items],
    "Smoking": [1 if smoking=="Yes" else 0],
    "Total_Carbon": [total_carbon]
})
fig3, ax3 = plt.subplots(figsize=(6,5))
sns.heatmap(example_df.corr(), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

st.info("This analyzer gives insight into your daily environmental impact. Small changes in lifestyle can significantly reduce your footprint! 🌱")
