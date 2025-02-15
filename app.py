import streamlit as st
import pandas as pd

# Title of the app
st.title("🌍 Land Area Calculator")

st.write("Enter a value and select the unit to convert it into different land measurement units.")

# Conversion factors (relative to square feet)
conversion_factors = {
    "Square Feet (sq ft)": 1,
    "Square Meters (sq m)": 0.092903,
    "Acres": 2.2957e-5,
    "Hectares": 9.2903e-6,
    "Dismil": 0.000918274,
    # "Bigha (Assam)": 0.000729,  # Approximate conversion, varies by state
    # "Bigha (West Bengal)": 0.000600,
    # "Katha (West Bengal)": 0.006,
    # "Katha (Bihar)": 0.001361,
    # "Gunta": 0.00022957,
    # "Ankanam": 0.111111
}

# Function to convert area
def convert_area(value, from_unit):
    base_value = value / conversion_factors[from_unit]  # Convert to square feet
    converted_values = {unit: base_value * factor for unit, factor in conversion_factors.items()}
    return converted_values

# User Inputs
value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=1.0)
unit = st.selectbox("Select Unit:", list(conversion_factors.keys()))

# Perform conversion on button click
# Perform conversion on button click
if st.button("Convert"):
    converted_values = convert_area(value, unit)
    df = pd.DataFrame(list(converted_values.items()), columns=["Unit", "Converted Value"])
    
    st.write("### 📊 Converted Values:")
    st.dataframe(df.set_index("Unit"))  # Removes the default index numbers

# Footer
st.write("🔹 Supports Indian Land Measurement Units")
# st.write("🔹 Bigha, Katha, Gunta, Ankanam units included")
