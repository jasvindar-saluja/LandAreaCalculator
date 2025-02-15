import streamlit as st
import pandas as pd

# Title of the app
st.title("🌍 Land Area Calculator")

st.write("Enter a value and select the unit to convert it into different land measurement units.")

# Corrected Conversion factors (relative to square feet)
conversion_factors = {
    "Square Feet (sq ft)": 1,
    "Square Meters (sq m)": 10.7639,
    "Acres": 43560,
    "Hectares": 107639,
    "Dismil": 435.6,  # 1 dismil = 435.6 sq ft
    # "Bigha (Assam)": 14400,  # Approximate conversion, varies by state
    # "Bigha (West Bengal)": 1600,
    # "Katha (West Bengal)": 720,
    # "Katha (Bihar)": 1361,
    # "Gunta": 1089,
    # "Ankanam": 72
}

# Function to convert area
def convert_area(value, from_unit):
    # Convert input value to square feet first
    value_in_sqft = value * conversion_factors[from_unit]
    
    # Convert square feet to all other units
    converted_values = {unit: value_in_sqft / factor for unit, factor in conversion_factors.items()}
    return converted_values

# User Inputs
value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=1.0)
unit = st.selectbox("Select Unit:", list(conversion_factors.keys()))

# Perform conversion on button click
if st.button("Convert"):
    converted_values = convert_area(value, unit)
    df = pd.DataFrame(list(converted_values.items()), columns=["Unit", "Converted Value"])
    
    st.write("### 📊 Converted Values:")
    st.dataframe(df.set_index("Unit"))  # Removes the default index numbers

# Footer
st.write("🔹 Supports Indian Land Measurement Units")
# st.write("🔹 Bigha, Katha, Gunta, Ankanam units included")
