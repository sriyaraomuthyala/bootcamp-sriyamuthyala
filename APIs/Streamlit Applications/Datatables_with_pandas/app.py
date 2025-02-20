import streamlit as st
import pandas as pd

st.title("Interactive Data Table")

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "Score": [85, 90, 95]}
df = pd.DataFrame(data)

st.write(df)
