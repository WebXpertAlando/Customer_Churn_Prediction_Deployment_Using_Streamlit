import streamlit as st
from PIL import Image

# Load an image
image = Image.open('images/customer-retention.jpg')

# Display the image
st.image(image, use_container_width=True)

st.markdown(""'
A customer retention strategy helps you keep your customers around longer, which helps you avoid having to go out and find new ones.

- Get to the root of the Churn.
- Customer Segmentation.
- Monitor User Engagement.
- Create an intuitive user onboarding process.
- Offer personalized and proactive customer communication.
- Reward customer loyalty .
- Follow up with customers.
- Develop a data roadmap and stick to it.
""")
