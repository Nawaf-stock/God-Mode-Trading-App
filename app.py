import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Peak Trading App 📈")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if ticker:
    data = yf.download(ticker, period="1y")

    st.subheader("Stock Price Chart")
    st.line_chart(data["Close"])

    st.subheader("Recent Data")
    st.write(data.tail())
