import pandas as pd
import numpy as np

print("Loading ML Predictions...")

df = pd.read_csv("data/ml_predictions.csv")

# -------------------------------
# Hourly Returns
# -------------------------------

df["Return"] = df["Close"].pct_change().fillna(0)

# -------------------------------
# Value at Risk (95%)
# -------------------------------

var95 = np.percentile(df["Return"], 5)

# -------------------------------
# Conditional Value at Risk
# -------------------------------

cvar95 = df[df["Return"] <= var95]["Return"].mean()

# -------------------------------
# Position Size
# -------------------------------

account_balance = 100000
risk_percent = 0.02

position_size = account_balance * risk_percent

# -------------------------------
# Stop Loss & Take Profit
# -------------------------------

latest_price = df["Close"].iloc[-1]

stop_loss = latest_price * 0.98
take_profit = latest_price * 1.04

risk_reward = (
    take_profit - latest_price
) / (
    latest_price - stop_loss
)

# -------------------------------
# Summary Table
# -------------------------------

summary = pd.DataFrame({

    "Metric":[
        "Account Balance",
        "Risk Per Trade",
        "Position Size",
        "Value at Risk (95%)",
        "Conditional VaR",
        "Stop Loss",
        "Take Profit",
        "Risk Reward Ratio"
    ],

    "Value":[
        account_balance,
        risk_percent,
        round(position_size,2),
        round(var95,6),
        round(cvar95,6),
        round(stop_loss,5),
        round(take_profit,5),
        round(risk_reward,2)
    ]

})

summary.to_csv(
    "data/risk_summary.csv",
    index=False
)

print(summary)

print("\nRisk Summary Saved")