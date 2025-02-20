import streamlit as st
from PIL import Image


st.title("Welcome to Customer Churn Prediction App")

# Load an image
image = Image.open('images/customer-churn.jpg')

# Display the image
st.image(image, use_container_width=True)
