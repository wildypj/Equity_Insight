from flask import Flask, render_template, request, jsonify
from ml_model import train_model, evaluate_model, predict_stock_close, backtest_model
import yfinance as yf 


app = Flask(__name__)

model, predictors, _ = train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')

    # Fetch data for the given stock ticker
    stock_data = yf.Ticker(ticker)
    stock_data = stock_data.history(period="1d")

    # Make prediction using the model
    prediction = predict_stock_close(stock_data, model, predictors)
    prediction = "Up" if prediction == 1 else "Down"

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
