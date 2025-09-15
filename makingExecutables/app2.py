# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Summary Reporter")
st.title("CSV Summary Reporter (Protected)")

# Simple password (use secrets if set, else fallback)
PASSWORD = st.secrets.get("APP_PASSWORD", "letmein")

if "authed" not in st.session_state:
    st.session_state.authed = False

if not st.session_state.authed:
    pwd = st.text_input("Enter password", type="password")
    if st.button("Unlock"):
        if pwd == PASSWORD:
            st.session_state.authed = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()

if st.button("Lock"):
    st.session_state.authed = False
    st.rerun()

uploaded = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Dataset Preview", df.head())
    desc = df.describe()
    st.write("Summary Statistics", desc)
    desc.to_csv("summary_report.csv", index=True)
    st.success("Summary saved as summary_report.csv")
