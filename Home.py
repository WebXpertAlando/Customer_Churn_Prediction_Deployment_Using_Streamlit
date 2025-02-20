import streamlit as st
from PIL import Image

# Load an image
image = Image.open('images/customer-churn.jpg')

# Display the image
st.image(image, caption="Churn", use_column_width=True)
