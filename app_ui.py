import streamlit as st
import yfinance as yf
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("stock_model.pkl", "rb"))

st.set_page_config(page_title="Stock Predictor", layout="wide")

st.title("📈 Stock Market Prediction App")

# Sidebar
st.sidebar.header("Settings")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL")

# Fetch data
data = yf.download(stock_symbol, start="2022-01-01", end="2024-01-01")

if not data.empty:
    st.subheader(f"{stock_symbol} Closing Price Chart")

    fig, ax = plt.subplots()
    ax.plot(data['Close'])
    ax.set_title("Stock Closing Prices")
    st.pyplot(fig)

    # Latest price
    latest_price = float(data['Close'].iloc[-1])

    st.write(f"Latest Closing Price: {latest_price:.2f}")

    if st.button("Predict Next Price"):
        prediction = model.predict([[latest_price]])
        predicted_price = float(np.array(prediction).item())

        st.success(f"Predicted Next Price: {predicted_price:.2f}")

else:
    st.error("Invalid stock symbol or no data available.")