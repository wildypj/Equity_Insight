# EquityInsight

EquityInsight is a simple web application for predicting stock price movements using machine learning. This application allows users to input a stock ticker symbol and receive a prediction of whether the stock price is likely to go up or down.

## Features

- Input field to enter a stock ticker symbol.
- Prediction button to generate a prediction for the entered stock.
- Display of the prediction result (Up or Down) based on the machine learning model.
- Background image related to the stock market ambiance.
- Responsive design for usability across different devices.

## Files

1. **index.html**: HTML file containing the structure and front-end logic of the web application. It includes an input field for the stock ticker symbol, a prediction button, and a display area for the prediction result.

2. **styles.css**: CSS file defining the styles and layout of the web application. It provides styling for the input field, button, output area, and overall layout.

3. **app.py**: Python script using Flask to handle the backend of the web application. It includes routes for serving the main page and handling stock prediction requests. The machine learning model for stock prediction is imported and used for making predictions.

4. **ml_model.py**: Python script containing functions for training, evaluating, and using the machine learning model for stock prediction. It utilizes the RandomForestClassifier algorithm from the scikit-learn library.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Open your web browser and navigate to `http://localhost:5000` to access the EquityInsight web application.
5. Enter a stock ticker symbol (e.g., AAPL for Apple Inc.) in the input field.
6. Click the "Predict" button to generate a prediction for the entered stock.
7. View the prediction result displayed below the input field.

## Requirements

- Python 3.x
- Flask
- scikit-learn
- yfinance
- panda

