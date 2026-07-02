import streamlit as st
import pandas as pd
import joblib

# -----------------------
# 🎨 Page Config
# -----------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------
# 💅 Custom CSS (UI Styling)
# -----------------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #7f8c8d;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
        .prediction-box {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #27ae60;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# 📦 Load Model
# -----------------------
model = joblib.load("house_price_model.pkl")

# ⚠️ IMPORTANT: Replace with your actual training columns
all_columns = model.feature_names_in_

# Default values (you can adjust based on dataset)
default_values = {col: 0 for col in all_columns}

# -----------------------
# 🏠 Title
# -----------------------
st.markdown('<div class="title">🏠 House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter key property details to estimate price</div>', unsafe_allow_html=True)

# -----------------------
# 🧾 User Inputs
# -----------------------
col1, col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality", 1, 10, 5)
    total_sf = st.number_input("Total Square Footage", value=1500)

with col2:
    exter_qual = st.selectbox("Exterior Quality", ["TA", "Gd", "Ex"])
    central_air = st.selectbox("Central Air", ["Y", "N"])

# -----------------------
# 🔮 Prediction
# -----------------------
if st.button("Predict Price 💰"):

    # Create full input with defaults
    input_data = pd.DataFrame(columns=all_columns)

    for col in input_data.columns:
        input_data[col] = default_values[col]

    # Override important features
    input_data['OverallQual'] = overall_qual
    input_data['ExterQual'] = exter_qual
    input_data['TotalSF'] = total_sf
    input_data['CentralAir'] = central_air

    # Predict
    prediction = model.predict(input_data)[0]

    # Display result
    st.markdown(
        f'<div class="prediction-box">Estimated Price: ${prediction:,.2f}</div>',
        unsafe_allow_html=True
    )