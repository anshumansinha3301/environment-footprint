# 🌍 Environmental Footprint Analyzer

## Overview

The **Environmental Footprint Analyzer** is an interactive, single-file Python project designed to help users understand and reduce their daily environmental impact. Using **Python**, **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**, the application calculates a user's daily carbon footprint, water usage, and waste impact based on everyday activities. Unlike money-driven applications, this project emphasizes **sustainability and environmental awareness**, making it suitable for students, professionals, and general audiences interested in making a positive difference.

Users can input daily activities such as electricity usage, transportation type and distance, water consumption, waste produced, meat meals, smoking habits, and plastic usage. The app then computes environmental impact metrics and provides clear, visual insights through **pie charts, bar charts, and correlation heatmaps**.

---

## Features

- **Single Python File**: All computations and visualizations are contained in a single `.py` file.  
- **Interactive Inputs**: Users can input daily lifestyle activities through a sidebar.  
- **Carbon Footprint Calculation**: Computes carbon contributions from electricity, transport, waste, meat, plastic, and smoking.  
- **Water Usage Tracking**: Calculates daily water usage impact.  
- **Visualizations**:  
  - Pie chart showing contribution of each activity to total footprint.  
  - Bar chart detailing footprint of individual activities.  
  - Correlation heatmap to understand how different activities contribute to total carbon output.  
- **Metrics Display**: Shows daily totals for carbon footprint, water usage, waste impact, meat impact, plastic impact, and smoking impact.  
- **Lifestyle Awareness**: Encourages users to make small daily changes to reduce their environmental footprint.

---

## Inputs

Users can enter the following parameters through the Streamlit sidebar:

- **Electricity usage (kWh/day)**  
- **Transport type**: Car, Bus, Bicycle, Walk  
- **Distance traveled (km/day)**  
- **Water usage (liters/day)**  
- **Waste produced (kg/day)**  
- **Meat meals per day**  
- **Smoking**: Yes/No  
- **Plastic items used per day**

---

## Calculations

The app uses predefined factors to compute environmental impact:

- **Transport**: kg CO₂ per km based on transport type  
- **Electricity**: kg CO₂ per kWh  
- **Waste**: kg CO₂ per kg of waste  
- **Water**: footprint in liters  
- **Meat**: kg CO₂ per meat meal  
- **Plastic**: kg CO₂ per plastic item  
- **Smoking**: kg CO₂ per cigarette per day  

The total footprint is calculated by summing the contributions of all components.  

---
