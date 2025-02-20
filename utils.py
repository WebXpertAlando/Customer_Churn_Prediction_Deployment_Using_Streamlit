import streamlit as st

def footer():
    st.markdown("---")
    st.markdown(
        "© 2025 DataAnalyticsXpert | Developed by [Vic Alando](https://github.com/WebXpertAlandob) "
        " | Contact: 0723 205 119 | Email: [vicadventist@gmail.com](mailto:your@email.com)",
        unsafe_allow_html=True,
    )

# Example Streamlit app
st.title("My Streamlit App")
st.write("Main content goes here.")

# Add footer
footer()

