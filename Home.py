import streamlit as st
import psycopg2
import bcrypt

# Database connection
DB_CONFIG = {
    "dbname": "project_streamlit",
    "user": "postgres",
    "password": "23121618",
    "host": "localhost",
    "port": "5433"
}

# Function to connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Function to create users table
def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Function to hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Function to verify password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Function to register a user
def register_user(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    hashed_pw = hash_password(password)
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()
        st.success("Registration successful! You can now log in.")
    except psycopg2.IntegrityError:
        conn.rollback()
        st.error("Username already exists. Choose another one.")
    finally:
        cur.close()
        conn.close()

# Function to authenticate a user
def authenticate_user(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    
    if user and check_password(password, user[0]):
        return True
    return False

# Initialize Streamlit App
st.title("🔐 Login System with PostgreSQL")

# Create users table
create_users_table()

# Sidebar Navigation
menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if menu == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success(f"Welcome, {username}!")
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
        else:
            st.error("Invalid username or password.")

elif menu == "Register":
    st.subheader("Create a New Account")
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")

    if st.button("Register"):
        if new_username and new_password:
            register_user(new_username, new_password)
        else:
            st.warning("Please enter a username and password.")

# Logout Button
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["user"] = None
        st.success("Logged out successfully!")

