📈 Stock Market Predictor

A machine learning project that predicts stock prices based on historical data using a regression model (e.g., Linear Regression / Random Forest).

📁 Project Structure
stock_market_predictor/

├── train_model.py        # Fetch data & train model
├── app.py                # Flask REST API
├── app_ui.py             # Streamlit frontend
├── requirements.txt      # Python dependencies
├── stock_data.csv        # Historical stock dataset (optional saved)
├── stock_model.pkl       # Trained ML model
├── feature_columns.pkl   # Feature order (if multiple features used)
└── README.md             # Project documentation
🚀 Getting Started
1. Install dependencies
pip install -r requirements.txt
2. Train the model
python train_model.py
Downloads historical stock data (e.g., AAPL)
Prepares features
Trains and saves the model
3. Run the Flask API
python app.py

API will run at:

http://127.0.0.1:5000
4. Run the Streamlit UI
python -m streamlit run app_ui.py
🌐 API Reference
POST /predict
Request:
{
    "prev_close": 150.25
}
Response:
{
    "predicted_price": 152.80,
    "stock": "AAPL",
    "note": "Predicted next closing price"
}
📊 Features Used
Feature	Type	Description
prev_close	Numeric	Previous closing price
moving_avg_5	Numeric	5-day moving average (optional)
moving_avg_10	Numeric	10-day moving average (optional)
volume	Numeric	Trading volume (optional)
🤖 Model Details
Algorithm: Linear Regression / Random Forest
Input: Historical stock features
Output: Next day closing price
Typical Use Cases:
Short-term price trend estimation
Educational ML project
API + UI integration demo
📈 Supported Stocks (Examples)

You can use any stock symbol supported by Yahoo Finance, such as:

AAPL (Apple)
MSFT (Microsoft)
TSLA (Tesla)
GOOGL (Google)
AMZN (Amazon)
⚠️ Disclaimer

This project is for educational purposes only. Stock price prediction is uncertain and should not be used for financial decision-making.
