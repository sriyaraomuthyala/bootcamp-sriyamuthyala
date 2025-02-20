import streamlit as st

st.title("Counter App")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter Value: {st.session_state.counter}")
