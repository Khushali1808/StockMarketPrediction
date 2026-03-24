from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('stock_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Stock Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prev_close = data['prev_close']

    prediction = model.predict([[prev_close]])

    return jsonify({
        "predicted_price": float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)