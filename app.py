import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Peak Trading Dashboard 📈")

st.write("Supports US 🇺🇸 and Saudi 🇸🇦 stocks")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

# Saudi fix
if ticker.isdigit():
    ticker = ticker + ".SR"

data = yf.download(ticker, period="1y")

if not data.empty:

    st.subheader("Price Chart")
    st.line_chart(data["Close"])

    # Moving averages
    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()

    st.line_chart(data[["Close", "MA20", "MA50"]])

    # Prediction
    if len(data) > 50:
        if data["MA20"].iloc[-1] > data["MA50"].iloc[-1]:
            st.success("Prediction: Stock may go UP 📈")
        else:
            st.error("Prediction: Stock may go DOWN 📉")

    st.metric("Current Price", round(data["Close"].iloc[-1], 2))

else:
    st.warning("Stock ticker not found.")

st.divider()

# Watchlist (no extra libraries needed)
st.subheader("⭐ Watchlist")

watchlist = st.text_input("Enter tickers separated by commas", "AAPL,TSLA,2222")

if watchlist:
    tickers = [t.strip() for t in watchlist.split(",")]

    for t in tickers:
        if t.isdigit():
            t = t + ".SR"

        d = yf.download(t, period="5d")

        if not d.empty:
            price = round(d["Close"].iloc[-1], 2)
            st.write(f"{t}: {price}")
