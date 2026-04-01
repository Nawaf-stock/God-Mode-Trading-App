import streamlit as st
import yfinance as yf
import pandas as pd

st.title("God Mode Trading Dashboard 📈")
st.write("US 🇺🇸 + Saudi 🇸🇦 stocks supported")

ticker_input = st.text_input("Enter stock ticker", "AAPL")
ticker = ticker_input.strip().upper()

# Convert Saudi tickers automatically
if ticker.isdigit():
    ticker = ticker + ".SR"

try:
    data = yf.download(ticker, period="1y", progress=False)
except:
    data = None

if data is None or len(data) == 0:
    st.warning("No data found for this ticker.")
else:

    close_series = data["Close"]

    if isinstance(close_series, pd.DataFrame):
        close_series = close_series.iloc[:, 0]

    close_series = close_series.dropna()

    if len(close_series) == 0:
        st.warning("Price data unavailable.")
    else:
        st.subheader("Price Chart")
        st.line_chart(close_series)

        current_price = close_series.iloc[-1]
        st.metric("Current Price", round(float(current_price), 2))

        ma20 = close_series.rolling(20).mean()
        ma50 = close_series.rolling(50).mean()

        if len(close_series) > 50:
            if ma20.iloc[-1] > ma50.iloc[-1]:
                st.success("Prediction: Stock may go UP 📈")
            else:
                st.error("Prediction: Stock may go DOWN 📉")

st.divider()

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
    except:
        d = None

    if d is None or len(d) == 0:
        st.write(f"{symbol}: No data")
    else:

        price_series = d["Close"]

        if isinstance(price_series, pd.DataFrame):
            price_series = price_series.iloc[:, 0]

        price_series = price_series.dropna()

        if len(price_series) == 0:
            st.write(f"{symbol}: No data")
        else:
            price = price_series.iloc[-1]
            st.write(f"{symbol}: {round(float(price), 2)}")
