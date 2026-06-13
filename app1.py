import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ad_revenue_model.pkl")

st.title("📊 YouTube Ad Revenue Predictor")

st.write("Enter video performance details:")

views = st.number_input("Views", min_value=0)
likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
watch_time = st.number_input("Watch Time (minutes)", min_value=0.0)
video_length = st.number_input("Video Length (minutes)", min_value=0.0)
subscribers = st.number_input("Subscribers", min_value=0)

engagement_rate = (likes + comments) / views if views > 0 else 0

input_data = pd.DataFrame({
    "views": [views],
    "likes": [likes],
    "comments": [comments],
    "watch_time_minutes": [watch_time],
    "video_length_minutes": [video_length],
    "subscribers": [subscribers],
    "engagement_rate": [engagement_rate]
})

if st.button("Predict Revenue"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Ad Revenue: ${prediction[0]:.2f}")
