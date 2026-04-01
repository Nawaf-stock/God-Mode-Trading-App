import streamlit as st
import yfinance as yf
import pandas as pd

st.title("God Mode Trading Dashboard 📈")
st.write("Supports US 🇺🇸 and Saudi 🇸🇦 stocks")

ticker_input = st.text_input("Enter Stock Ticker", "AAPL")

# Clean ticker
ticker = ticker_input.strip().upper()

# Auto-fix Saudi tickers (e.g., 2222 -> 2222.SR)
if ticker.isdigit():
    ticker = ticker + ".SR"

# Download data safely
try:
    data = yf.download(ticker, period="1y", progress=False)
except Exception:
    data = pd.DataFrame()

if data is None or data.empty or "Close" not in data.columns:
    st.warning("No data found for this ticker. Try another one.")
else:
    close_series = pd.to_numeric(data["Close"], errors="coerce").dropna()

    if close_series.empty:
        st.warning("Price data unavailable.")
    else:
        # Price chart
        st.subheader("Price Chart")
        st.line_chart(close_series)

        # Moving averages
        ma20 = close_series.rolling(20).mean()
        ma50 = close_series.rolling(50).mean()

        if len(close_series) > 50:
            if ma20.iloc[-1] > ma50.iloc[-1]:
                st.success("Prediction: Stock may go UP 📈")
            else:
                st.error("Prediction: Stock may go DOWN 📉")

        current_price = float(close_series.iloc[-1])
        st.metric("Current Price", round(current_price, 2))

st.divider()

# Watchlist
st.subheader("⭐ Watchlist")

watchlist_input = st.text_input(
    "Enter tickers separated by commas",
    "AAPL,TSLA,2222"
)

tickers = [t.strip().upper() for t in watchlist_input.split(",") if t.strip()]

for t in tickers:
    symbol = t
    if symbol.isdigit():
        symbol = symbol + ".SR"

    try:
        d = yf.download(symbol, period="5d", progress=False)
    except Exception:
        d = pd.DataFrame()

    if d is None or d.empty or "Close" not in d.columns:
        st.write(f"{symbol}: No data")
    else:
        price_series = pd.to_numeric(d["Close"], errors="coerce").dropna()
        if price_series.empty:
            st.write(f"{symbol}: No data")
        else:
            price = float(price_series.iloc[-1])
            st.write(f"{symbol}: {round(price, 2)}")
