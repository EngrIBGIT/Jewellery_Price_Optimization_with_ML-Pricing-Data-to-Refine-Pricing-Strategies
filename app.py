import streamlit as st

# ✅ Set page configuration as the first Streamlit command
st.set_page_config(page_title="Jewelry Price Prediction", layout="wide")

import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from sklearn.preprocessing import StandardScaler

# Load the trained model
try:
    model = pickle.load(open("jewelry_price_model.pkl", "rb"))
except FileNotFoundError:
    st.error("🔴 Error: Model file 'jewelry_price_model.pkl' not found. Please upload the correct model.")

# ---- Header ----
st.image("jewelry_logo.png", width=250)  # Ensure this file exists in the correct directory
st.title("💎 Jewelry Price Prediction App")
st.write("Upload jewelry details and get an estimated price instantly!")

# ---- Sidebar Inputs ----
st.sidebar.header("Jewelry Attributes")
category = st.sidebar.selectbox("Category", ["Necklace", "Ring", "Bracelet", "Earring"])
brand_id = st.sidebar.number_input("Brand ID", min_value=1, max_value=100, step=1)
target_gender = st.sidebar.selectbox("Target Gender", ["Male", "Female", "Unisex"])
main_color = st.sidebar.selectbox("Main Color", ["Gold", "Silver", "Rose Gold"])
main_metal = st.sidebar.selectbox("Main Metal", ["Gold", "Silver", "Platinum"])
main_gem = st.sidebar.selectbox("Main Gem", ["Diamond", "Ruby", "Sapphire", "None"])
order_month = st.sidebar.slider("Order Month", 1, 12, step=1)
order_day = st.sidebar.slider("Order Day", 1, 31, step=1)

# Process Input Data
input_data = pd.DataFrame(
    [[category, brand_id, target_gender, main_color, main_metal, main_gem, order_month, order_day]],
    columns=["Category", "Brand_ID", "Target_Gender", "Main_Color", "Main_Metal", "Main_Gem", "Order Month", "Order Day"]
)

# Button for Prediction
if st.sidebar.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Predicted Jewelry Price: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

# ---- File Upload for Bulk Prediction ----
st.subheader("📤 Upload a Dataset for Bulk Prediction")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        predictions = model.predict(df)
        df["Predicted Price"] = predictions
        st.write(df)

        # File Download Options
        st.download_button("Download Predictions (CSV)", df.to_csv(index=False).encode('utf-8'), "predictions.csv", "text/csv")
        st.download_button("Download Predictions (Excel)", df.to_excel(index=False, engine='openpyxl'), "predictions.xlsx")
    except Exception as e:
        st.error(f"❌ File Processing Error: {e}")

# ---- Data Visualization ----
st.subheader("📊 Jewelry Price Distribution")

if uploaded_file:
    fig = px.histogram(df, x="Predicted Price", title="Price Distribution", nbins=30)
    st.plotly_chart(fig)

# ---- Footer ----
st.write("🔗 **Developed by Ibrahim Ismaila** | st.markdown("[GitHub](https://github.com/EngrIBGIT/Jewellery_Price_Optimization_with_ML-Pricing-Data-to-Refine-Pricing-Strategies)")
