import streamlit as st # type: ignore
from pathlib import Path
import streamlit_authenticator as stauth # type: ignore

st.set_page_config(
    page_title="About this App",
    page_icon="👋",
    layout= 'wide'
)

st.title('Customer Churn Prediction Model')
st.write('About this App')


st.write('''
    <br>
    </div>
    <div style="background-color:#000;padding:10px;border-radius:10px">
    <h1 style="color:#ffd700">Predicting Customer Churn</h1>
    <p style="color:#ffffff">Predicting customer churn marks a substantial advancement in customer retention analytics.</p>
    <p style="color:#ffffff">Our app is designed to help you anticipate customer churn and take proactive measures to retain your valuable customers.</p>

    <br>
    <div style="background-color:#000;padding:10px;border-radius:10px">
    <h1 style="color:#ffd700">Unlock the Power of Data-Driven Insights</h1>
    <p style="color:#ffffff">Our app leverages advanced machine learning algorithms to analyze customer data and identify patterns that indicate a high risk.</p>
    <p style="color:#ffffff">Review and analyze past predictions, and gain a deeper understanding of your customers' behavior.</p>
    <p style="color:#ffffff">Our intuitive design ensures a seamless and efficient experience.</p>
    <p style="color:#ffffff">Simply input your customer data, select from our robust machine learning models (AdaBoost, Logistic Regression, or Random Forest),</p>
    <p style="color:#ffffff">and get instant predictions on the likelihood of customer churn.</p>
    
    <h2 style="color:#ffd700">Key Features</h2>
    <ul>
        <li style="color:#ffff00"><b>Machine Learning Models:</b> Choose from AdaBoost, Logistic Regression, or Random Forest models to find the best fit for your dataset.</li>
        <li style="color:#ffffff"><b>Streamlined Prediction Process:</b> Get quick and accurate results with our efficient prediction process.</li>
        <li style="color:#ffff00"><b>Data Retrieval:</b> Access your prediction history anytime, stored in a convenient "history.csv" file.</li>
        <li style="color:#ffffff"><b>Data Display:</b> Easily review and analyze past predictions in a clear and organized tabular format.</li>
    </ul>
   
    <h2 style="color:#ffd700">Empowering Users, Democratizing Data</h2>
    <p style="color:#ffffff">Our app goes beyond predictive analytics, democratizing data and putting the power in your hands.</p>
    <p style="color:#ffffff">Make data-driven decisions, reduce churn rates, and drive business success.</p>

    <br>

    <div style="background-color:#ffd700;padding:10px;border-radius:10px">
    <h1 style="color:#000">GET STARTED TODAY!</h1>
    <p style="color:#000">Explore our app and discover the value of accurate churn prediction.</p>
    </div>
    ''', unsafe_allow_html=True)

from utils import footer
