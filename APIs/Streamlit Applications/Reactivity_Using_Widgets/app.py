import streamlit as st

st.title("Interactive Slider App")

value = st.slider("Choose a value:", 0, 100, 50)
st.write(f"Selected Value: {value}")
