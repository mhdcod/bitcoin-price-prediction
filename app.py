#import matplotlib
#matplotlib.use('Agg')  # Non-interactive backend for Matplotlib
import plotly.graph_objects as go
from flask import Flask, render_template, request, redirect, url_for
#import pandas as pd
import numpy as np
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
#import io
#import base64
from datetime import datetime
import requests

# Initialize Flask app
app = Flask(__name__)

# Load Pre-trained Model
model = load_model("model5.keras")

# Helper Function to Convert Plotly Plots to HTML
def plot_to_html(fig):
    fig_html = fig.to_html(full_html=False)
    return fig_html

# Function to fetch live BTC price
def fetch_live_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stock = request.form.get("stock")
        no_of_days = int(request.form.get("no_of_days"))
        return redirect(url_for("predict", stock=stock, no_of_days=no_of_days))
    return render_template("index.html")

@app.route("/predict")
def predict():
    stock = request.args.get("stock", "BTC-USD")
    no_of_days = int(request.args.get("no_of_days", 10))

    # Fetch Stock Data
    end = datetime.now()
    start = datetime(end.year - 10, end.month, end.day)
    btc_data = yf.download(stock, start, end)
    
    if btc_data.empty:
        return render_template("result.html", error="Invalid stock ticker or no data available.")

    # Data Preparation
    splitting_len = int(len(btc_data) * 0.9)
    x_test = btc_data[['Close']][splitting_len:]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(x_test)

    x_data = []
    y_data = []
    for i in range(100, len(scaled_data)):
        x_data.append(scaled_data[i - 100:i])
        y_data.append(scaled_data[i])

    x_data = np.array(x_data)
    y_data = np.array(y_data)

    # Predictions
    predictions = model.predict(x_data)
    inv_predictions = scaler.inverse_transform(predictions)
    inv_y_test = scaler.inverse_transform(y_data)

    # Prepare Data for Plotting
    #plotting_data = pd.DataFrame({
    #    'Original Test Data': inv_y_test.flatten(),
    #    'Predicted Test Data': inv_predictions.flatten()
    #}, index=x_test.index[100:])

    # Plot 3: Future Predictions using Plotly
    last_100 = btc_data[['Close']].tail(100)
    last_100_scaled = scaler.transform(last_100)

    future_predictions = []
    last_100_scaled = last_100_scaled.reshape(1, -1, 1)
    for _ in range(no_of_days):
        next_day = model.predict(last_100_scaled)
        future_predictions.append(scaler.inverse_transform(next_day))
        last_100_scaled = np.append(last_100_scaled[:, 1:, :], next_day.reshape(1, 1, -1), axis=1)

    future_predictions = np.array(future_predictions).flatten()

    # Create Plotly Graph
    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(
        x=list(range(1, no_of_days + 1)),
        y=future_predictions,
        mode='lines+markers',
        marker=dict(color='purple', size=8),
        name="Predicted Future Prices",
        text=future_predictions,  # Add hover text
        hovertemplate='Predicted Price: %{text}<extra></extra>'
    ))

    fig3.update_layout(
        title="Future Close Price Predictions",
        xaxis_title="Days Ahead",
        yaxis_title="Predicted Close Price",
        template="plotly_dark"
    )

    # Convert plot to HTML
    future_plot = plot_to_html(fig3)

    # Fetch live BTC price
    btc_price = fetch_live_btc_price()

    return render_template(
        "result.html",
        stock=stock,
        future_plot=future_plot,
        future_predictions=future_predictions,
        btc_price=btc_price
    )

if __name__ == "__main__":
    app.run(debug=True)
