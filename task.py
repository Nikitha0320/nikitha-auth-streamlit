import pymysql
import streamlit as st
con=pymysql.connect(
    host="localhost",
    user="root",
    password="gujjuri@2006",
    database="student_db"
)
c=con.cursor()
c.execute("CREATE table IF NOT EXISTS user(email VARCHAR(30),username VARCHAR(20) PRIMARY KEY,password VARCHAR(20))")
con.commit()
def login_user(username,password):
    st.header("Login Page")
    c.execute("SELECT * FROM user WHERE username=%s AND password=%s",(username,password))
    data=c.fetchone()
    return data
def signup_user(email,username,password):
    query="select * from user where username=%s"
    if c.execute(query,(username,)):
        st.warning("Username already exists. Please choose a different username.")
    st.header("Signup Page")
    c.execute("INSERT INTO user(email,username,password) VALUES(%s,%s,%s)",(email,username,password))
    con.commit()

import streamlit as st
st.divider()
st.sidebar.title("Menu")
option = st.sidebar.radio(
"Choose page",
["Login", "Signup"]
)

if option == "Login":
    st.title("Login Page")
    with st.container():
        with st.form("login_form"):
            username=st.text_input("Username")
            password=st.text_input("Password",type="password")
            submit_button=st.form_submit_button("Login")
            if submit_button:
                user=login_user(username,password)
                if user:
                    st.success("Login Successful!")
                else:
                    st.error("Invalid Username or Password")

if option == "Signup":
    st.title("Signup Page")
    with st.container():
        with st.form("signup_form"):
            new_email=st.text_input("New Email")
            new_username=st.text_input("New Username")
            new_password=st.text_input("New Password",type="password")
            signup_button=st.form_submit_button("Signup")
            if signup_button:
                signup_user(new_email,new_username,new_password)
                st.success("Signup Successful! You can now login.")