import streamlit as st # type: ignore
import pickle
import streamlit_authenticator as stauth # type: ignore
from pathlib import Path


st.set_page_config(
    page_title="",
    page_icon="door-arrow-right",
    layout='wide'
)

# --- USER AUTHENTICATION ---
names = ['Visitor', 'Admin']
username = ['user', 'admin']

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, username, hashed_passwords,
                                    'churn_app', 'abcdefg')


# --- LANDING PAGE ---
col1,col2 = st.columns(2)
with col2:
    name, authentication_status, username = authenticator.login('Login','main')
    st.session_state['name'] = name
    st.session_state['authentication_status'] = authentication_status
    st.session_state['username'] = username

    if authentication_status == None:
        st.info('Please Log in to continue')
        st.markdown('### **credentials**')
        st.write('Username: user')
        st.write('Password: abc123')
        st.markdown('''
                    <style>
                    [data-testid="stSidebar"] {
                        visibility: hidden;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
            
with col1:
    if authentication_status == None:
        st.title('This is a binary classification model built in practice within the Lux Dev Academy Data Science Bootcamp \n'
                'It has been developed  by [Victor alando](https://github.com/WebXpertAlando) \n\n')
        st.write('See something you like? Leave me a star on [github](https://github.com/WebXpertAlando).⭐️😍 \n\n'
                'See something I can improve on or help you out with?\n\n'
                'Connect with me on [LinkedIn](https://www.linkedin.com/in/victor-alando/) and let us make magic happen :smiley:\n\n\n'
                )
        

# -- Main app section --
if authentication_status == False:
    with col1:
        st.title('This is a binary classification model built in practice within the [Lux Dev](https://azubiafrica.org) Data Science Bootcamp\n'
                'It has been developed with love and sweat by [Rama_Mwenda](https://github.com/Rama-Mwenda) \n\n')
        st.write('See something you like? Leave me a star on [github](https://github.com/Rama-Mwenda).⭐️😍 \n\n'
                'See something I can improve on or help you out with?\n\n'
                'Connect with me on [LinkedIn](https://www.linkedin.com/in/rama-mwenda/) and let us make magic happen :smiley:\n\n\n'
                )
    with col2:
        st.error('Wrong username / password')
        st.info('Please try again with the credentials below')
        st.markdown('### **Demo credentials**')
        st.write('Username: user')
        st.write('Password: abc123')
        st.markdown('''
        <style>
        [data-testid="stSidebar"] {
            visibility: hidden;
        }
        </style>
        ''', unsafe_allow_html=True)


# --- HOME PAGE ---
if authentication_status:
    st.button(f'{st.session_state["name"]} logged in')
    st.title(f'Welcome {st.session_state["username"]} to the Customer Churn Prediction App')
    
    
    st.markdown('### ================================================ ')
    authenticator.logout('Logout','main')
    
    