import streamlit as st
import yfinance as yf
import pandas as pd

st.title("God Mode Trading App 📈")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

data = yf.download(ticker, period="1y")

if not data.empty:

    st.subheader("Price Chart")
    st.line_chart(data["Close"])

    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()

    if len(data) > 50:
        if data["MA20"].iloc[-1] > data["MA50"].iloc[-1]:
            st.success("Prediction: Stock may go UP 📈")
        else:
            st.error("Prediction: Stock may go DOWN 📉")

    st.subheader("Latest Data")
    st.write(data.tail())

else:
    st.warning("Stock ticker not found. Try another one.")
