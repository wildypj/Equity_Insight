import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import pandas as pd

def train_model():
    sp500 = yf.Ticker("^GSPC")
    sp500 = sp500.history(period="max")
    del sp500["Dividends"]
    del sp500["Stock Splits"]
    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)
    sp500 = sp500.loc["1990-01-01":].copy()

    model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)
    predictors = ["Close", "Open", "High", "Low", "Volume"]
    model.fit(sp500[predictors], sp500["Target"])

    return model, predictors, sp500

def evaluate_model(model, predictors, test_size=100):
    _, _, sp500 = train_model()  # Load sp500 data
    test = sp500.iloc[-test_size:]
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index=test.index)
    precision = precision_score(test["Target"], preds)
    return precision

def predict_stock_close(stock_data, model, predictors):
    prediction = model.predict(stock_data[predictors].values.reshape(1, -1))
    return prediction[0]

def backtest_model(model, predictors, sp500, start=2500, step=250):
    all_predictions = []

    for i in range(start, sp500.shape[0], step):
        train = sp500.iloc[0:i].copy()
        test = sp500.iloc[i:(i+step)].copy()
        predictions = predict_stock_close(train, model, predictors)  # Fix the reference here
        all_predictions.append(predictions)
    
    return pd.concat(all_predictions)
