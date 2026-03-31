# Watchlist Section
st.subheader("⭐ Watchlist")
watchlist_input = st.text_input("Enter tickers separated by commas", "AAPL, TSLA, 2222")

if watchlist_input:
    tickers = [t.strip() for t in watchlist_input.split(",")]
    cols = st.columns(len(tickers))
    
    for i, t in enumerate(tickers):
        # Determine if it's a Saudi or US stock
        symbol = t + ".SR" if t.isdigit() else t
        w_data = yf.download(symbol, period="1d")
        
        if not w_data.empty:
            price = round(float(w_data["Close"].iloc[-1]), 2)
            cols[i].metric(symbol, price)
        else:
            # This was the line causing your error
            cols[i].write(f"{symbol} ❌")    st.warning("Stock ticker not found. Try another one.")

st.divider()

# Watchlist Section
st.subheader("⭐ Watchlist")
watchlist_input = st.text_input("Enter tickers separated by commas", "AAPL, TSLA, 2222")

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
else:
    st.warning("Stock ticker not found. Try another one.")

st.divider()

# Watchlist
st.subheader("⭐ Watchlist")
watchlist_input = st.text_input("Enter tickers separated by commas", "AAPL, TSLA, 2222")

if watchlist_input:
    tickers = [t.strip() for t in watchlist_input.split(",")]
    
    # Create columns for the watchlist display
    cols = st.columns(len(tickers))
    
    for i, t in enumerate(tickers):
        symbol = t + ".SR" if t.isdigit() else t
        w_data = yf.download(symbol, period="1d")
        
        if not w_data.empty:
            price = round(float(w_data["Close"].iloc[-1]), 2)
            cols[i].metric(symbol, price)
        else:
            cols[i].write(f"{symbol} ❌")else:
    st.warning("Stock ticker not found. Try another one.")

st.divider()

# Watchlist
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
