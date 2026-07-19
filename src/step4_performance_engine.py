import pandas as pd
import numpy as np

print("Loading ML prediction data...")

df = pd.read_csv("data/ml_predictions.csv")

# -----------------------------
# Returns
# -----------------------------

df["Return"] = df["Close"].pct_change().fillna(0)

# BUY = +Return
# SELL = -Return

df["Strategy_Return"] = np.where(
    df["Signal"] == "BUY",
    df["Return"],
    -df["Return"]
)

# -----------------------------
# Cumulative Return
# -----------------------------

df["Cumulative_Return"] = (
    1 + df["Strategy_Return"]
).cumprod()

# -----------------------------
# Win Rate
# -----------------------------

wins = (df["Strategy_Return"] > 0).sum()

total = len(df)

win_rate = wins / total * 100

# -----------------------------
# Sharpe Ratio
# -----------------------------

sharpe = (
    df["Strategy_Return"].mean()
    /
    df["Strategy_Return"].std()
)

# -----------------------------
# Maximum Drawdown
# -----------------------------

rolling_max = df["Cumulative_Return"].cummax()

drawdown = (
    df["Cumulative_Return"] - rolling_max
) / rolling_max

max_drawdown = drawdown.min()

# -----------------------------
# Performance Summary
# -----------------------------

summary = pd.DataFrame({

    "Metric":[
        "Total Trades",
        "Win Rate",
        "Sharpe Ratio",
        "Maximum Drawdown",
        "Final Portfolio Value"
    ],

    "Value":[
        total,
        round(win_rate,2),
        round(sharpe,4),
        round(max_drawdown,4),
        round(df["Cumulative_Return"].iloc[-1],4)
    ]

})

summary.to_csv(
    "data/performance_summary.csv",
    index=False
)

print("\nPerformance Summary\n")

print(summary)

print("\nSaved:")
print("data/performance_summary.csv")