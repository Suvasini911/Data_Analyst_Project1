import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading Market Data...")

df = pd.read_csv("data/processed_market_data.csv")

prices = df["Close"]

last_price = prices.iloc[-1]

returns = prices.pct_change().dropna()

mean_return = returns.mean()

volatility = returns.std()

# -------------------------------
# Monte Carlo Parameters
# -------------------------------

num_simulations = 1000

forecast_days = 30

simulations = np.zeros((forecast_days, num_simulations))

# -------------------------------
# Run Simulation
# -------------------------------

for i in range(num_simulations):

    simulated_price = last_price

    for j in range(forecast_days):

        simulated_return = np.random.normal(
            mean_return,
            volatility
        )

        simulated_price *= (1 + simulated_return)

        simulations[j, i] = simulated_price

# -------------------------------
# Save Simulation Data
# -------------------------------

mc = pd.DataFrame(simulations)

mc.to_csv(
    "data/mc_scenarios.csv",
    index=False
)

print("Monte Carlo scenarios saved.")

# -------------------------------
# Plot
# -------------------------------

plt.figure(figsize=(12,6))

plt.plot(simulations)

plt.title("Monte Carlo Price Simulation")

plt.xlabel("Days")

plt.ylabel("Price")

plt.grid(True)

plt.savefig("data/monte_carlo_simulation.png")

plt.show()