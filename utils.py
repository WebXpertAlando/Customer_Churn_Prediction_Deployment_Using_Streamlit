import streamlit as st

import streamlit as st

def footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #333;
        }
        </style>
        <div class="footer">
            © 2024 Your Company | <a href="https://github.com/yourgithub" target="_blank">GitHub</a> | 
            <a href="mailto:your@email.com">Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Example Streamlit app
st.title("My Streamlit App")
st.write("Main content goes here.")

# Add sticky footer
footer()

