import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Download stock data (example: Apple)
df = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# Use closing price
df = df[['Close']].dropna()

# Create features (previous day's price)
df['Prev_Close'] = df['Close'].shift(1)
df = df.dropna()

X = df[['Prev_Close']]
y = df['Close']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("stock_model.pkl", "wb"))

print("Stock model trained and saved!")