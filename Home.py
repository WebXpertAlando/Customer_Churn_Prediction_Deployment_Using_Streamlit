import streamlit as st
from PIL import Image



st.title("Welcome to Customer Churn Prediction App")

# Load an image
image = Image.open('images/customer-churn.jpg')

# Display the image
st.image(image, use_container_width=True)

st.write('''<h1 style="color:#000">Empowering Users, Democratizing Data</h1>
Our app goes beyond predictive analytics, democratizing data and putting the power in your hands")
Make data-driven decisions, reduce churn rates, and drive business success".

 <div style="background-color:#ffd700;padding:10px;border-radius:10px">
    <h1 style="color:#000">GET STARTED TODAY!</h1>
    <p style="color:#000">Explore this app and discover the value of accurate churn prediction.</p>
    </div>
''',  unsafe_allow_html=True)


from utils import footer

# Google AdSense Ad Code 
adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-5686744668296213"
     data-ad-format="auto"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

# Embed Ad Code in Streamlit
st.markdown(adsense_code, unsafe_allow_html=True)
