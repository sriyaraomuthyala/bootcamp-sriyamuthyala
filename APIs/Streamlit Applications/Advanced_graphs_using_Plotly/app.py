import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Plotly Scatter Plot")

df = pd.DataFrame({
    "x": np.random.rand(100),
    "y": np.random.rand(100),
    "category": np.random.choice(["A", "B", "C"], 100)
})

fig = px.scatter(df, x="x", y="y", color="category", title="Random Scatter Plot")
st.plotly_chart(fig)
