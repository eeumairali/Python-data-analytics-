# app.py
import streamlit as st
import pandas as pd

st.title("CSV Summary Reporter")
st.header("developed by chris")

uploaded = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Dataset Preview", df.head())
    desc = df.describe()
    st.write("Summary Statistics", desc)
    desc.to_csv("summary_report.csv", index=True)
    st.success("Summary saved as summary_report.csv")
