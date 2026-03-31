import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Peak Trading Dashboard", page_icon="📈")

st.title("Peak Trading Dashboard 📈")
st.write("Supports US 🇺🇸 and Saudi 🇸🇦 stocks")

# --- MAIN ANALYSIS ---
ticker = st.text_input("Enter Stock Ticker", "AAPL")

if ticker.isdigit():
    ticker = ticker + ".SR"

data = yf.download(ticker, period="1y")

if not data.empty:
    st.subheader(f"Price Chart: {ticker}")
    st.line_chart(data["Close"])

    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA50"] = data["Close"].rolling(50).mean()

    if len(data) > 50:
        st.subheader("Trend Indicators")
        st.line_chart(data[["Close", "MA20", "MA50"]])

        if data["MA20"].iloc[-1] > data["MA50"].iloc[-1]:
            st.success("Prediction: Stock may go UP 📈")
        else:
            st.error("Prediction: Stock may go DOWN 📉")

    st.metric("Current Price", round(float(data["Close"].iloc[-1]), 2))
else:
    st.warning("Stock ticker not found. Try another one.")

st.divider()

# --- WATCHLIST ---
st.subheader("⭐ Watchlist")
watchlist_input = st.text_input("Tickers (comma separated)", "AAPL, TSLA, 2222")

if watchlist_input:
    tickers = [t.strip() for t in watchlist_input.split(",")]
    cols = st.columns(len(tickers))
    
    for i, t in enumerate(tickers):
        symbol = t + ".SR" if t.isdigit() else t
        w_data = yf.download(symbol, period="1d")
        
        if not w_data.empty:
            price = round(float(w_data["Close"].iloc[-1]), 2)
            cols[i].metric(symbol, price)
        else:
            cols[i].write(f"{symbol} ❌")
