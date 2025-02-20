import streamlit as st

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "password":
                st.session_state.authenticated = True
            else:
                st.error("Incorrect Username or Password")
        return False
    return True

if check_password():
    st.title("Secure Streamlit App")
    st.write("You have successfully logged in!")
