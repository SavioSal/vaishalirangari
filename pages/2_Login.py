import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")
st.header("Login")

with st.form("login"):
    username = st.text_input("Username:")
    password = st.text_input("Password:")
    submitted = st.form_submit_button("Login")
    if submitted:
        if password =='savioglobal' and username =='vaishali':
            st.toast("Login Successful!")
        else:
            st.error("Incorrect username or password.")