import pandas as pd
import numpy as np
import random
import os

print("Loading processed market data...")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/processed_market_data.csv")

required = ["Close", "EMA_20", "RSI_14", "MACD"]

missing = [c for c in required if c not in df.columns]

if missing:
    raise Exception(f"Missing columns: {missing}")

# -----------------------------
# Build Market State
# -----------------------------

def get_state(row):

    trend = 1 if row["Close"] > row["EMA_20"] else 0

    if row["RSI_14"] > 60:
        rsi = 2
    elif row["RSI_14"] < 40:
        rsi = 0
    else:
        rsi = 1

    macd = 1 if row["MACD"] > 0 else 0

    return trend * 6 + rsi * 2 + macd


df["State"] = df.apply(get_state, axis=1)

num_states = int(df["State"].max()) + 1
num_actions = 3

# Actions
# 0 HOLD
# 1 BUY
# 2 SELL

Q = np.zeros((num_states, num_actions))

alpha = 0.10
gamma = 0.95
epsilon = 0.15

episodes = 500

print("Training Q-Learning Agent...")

# -----------------------------
# Train
# -----------------------------

for ep in range(episodes):

    for i in range(len(df)-1):

        state = int(df.iloc[i]["State"])

        if random.random() < epsilon:
            action = random.randint(0,2)
        else:
            action = np.argmax(Q[state])

        current = df.iloc[i]["Close"]
        nxt = df.iloc[i+1]["Close"]

        price_change = nxt-current

        if action == 1:          # BUY

            reward = price_change * 10000

        elif action == 2:        # SELL

            reward = -price_change * 10000

        else:                    # HOLD

            reward = -0.02

        next_state = int(df.iloc[i+1]["State"])

        Q[state,action] += alpha * (
            reward
            + gamma*np.max(Q[next_state])
            - Q[state,action]
        )

print("Training Complete")

# -----------------------------
# Predict
# -----------------------------

signals=[]

for i in range(len(df)):

    state=int(df.iloc[i]["State"])

    q=Q[state]

    best=np.argmax(q)

    if best==1:
        signal="BUY"

    elif best==2:
        signal="SELL"

    else:
        signal="HOLD"

    # Technical confirmation

    if signal=="BUY":

        if df.iloc[i]["RSI_14"] < 45:
            signal="HOLD"

    elif signal=="SELL":

        if df.iloc[i]["RSI_14"] >55:
            signal="HOLD"

    signals.append(signal)

df["RL_Signal"]=signals

# -----------------------------
# Statistics
# -----------------------------

buy=(df["RL_Signal"]=="BUY").sum()
sell=(df["RL_Signal"]=="SELL").sum()
hold=(df["RL_Signal"]=="HOLD").sum()

print("\n========== RL SUMMARY ==========")
print(f"BUY  Signals : {buy}")
print(f"SELL Signals : {sell}")
print(f"HOLD Signals : {hold}")

# -----------------------------
# Save
# -----------------------------

os.makedirs("data",exist_ok=True)

df.to_csv(
    "data/rl_predictions.csv",
    index=False
)

print("\nSaved:")
print("data/rl_predictions.csv")