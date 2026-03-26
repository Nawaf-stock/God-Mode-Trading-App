
stock-app
touch app.p open -e app.py 
nawafadel@Nawafs-MacBook-Air stock-app % >....                                  

    # --- PAPER TRADING ---
    st.subheader("💸 Paper Trading")

    st.write(f"Balance: ${round(st.session_state.money,2)}")

    qty = st.number_input("Shares", 1, 100, 1)

    if st.button("Buy"):
        cost = price * qty
        if st.session_state.money >= cost:
            st.session_state.money -= cost
            st.session_state.portfolio[ticker] = st.session_state.portfolio.get(ticker, 0) + qty

    if st.button("Sell"):
        if ticker in st.session_state.portfolio and st.session_state.portfolio[ticker] >= qty:
            st.session_state.money += price * qty
            st.session_state.portfolio[ticker] -= qty

    st.write("📦 Portfolio:")
    st.write(st.session_state.portfolio)
