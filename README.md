# 🚀 Forex AI Trading Signal Agent

## 📌 Project Overview

The **Forex AI Trading Signal Agent** is an AI-powered decision support system for Forex trading. It combines **Technical Analysis**, **Machine Learning**, **Reinforcement Learning**, **Risk Management**, **Monte Carlo Simulation**, and **Power BI** to analyze historical market data, generate trading signals, evaluate risk, and visualize insights through interactive dashboards.

This project was developed as part of the **Project 1C – Data Analyst Forex Trading Signal** assignment.

---

# 🎯 Objectives

- Generate BUY, SELL, and HOLD trading signals
- Apply technical indicators for market analysis
- Predict trading signals using Machine Learning
- Implement Reinforcement Learning using Q-Learning
- Analyze trading performance
- Perform portfolio risk management
- Forecast future market scenarios using Monte Carlo Simulation
- Visualize results using interactive Power BI dashboards

---

# ✨ Key Features

### 📈 Technical Analysis

Implemented indicators:

- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Bollinger Bands
- Average True Range (ATR)
- Ichimoku Cloud

---

### 🤖 Machine Learning

Model:

- Random Forest Classifier

Features Used:

- SMA
- EMA
- RSI
- MACD
- Bollinger Bands
- ATR
- Ichimoku Indicators

Output:

- BUY Signal
- SELL Signal
- Confidence Score

---

### 🧠 Reinforcement Learning

Implemented:

- Q-Learning Trading Agent

Actions:

- BUY
- SELL
- HOLD

State Representation:

- EMA Trend
- RSI
- MACD

Reward Function:

- Profit/Loss-based reward

---

### ⚠️ Risk Management

Implemented:

- Position Sizing
- Stop Loss
- Take Profit
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Risk-Reward Ratio

---

### 📊 Performance Analysis

Performance Metrics:

- Win Rate
- Sharpe Ratio
- Maximum Drawdown
- Portfolio Value
- Total Trades

---

### 🎲 Monte Carlo Simulation

Monte Carlo simulation is used to generate multiple future price paths based on historical market returns. This helps estimate uncertainty and evaluate potential future market outcomes.

---

# 📊 Power BI Dashboards

The project includes five interactive dashboards:

### 1. Trading Dashboard

Displays:

- Forex Price Trend
- RSI Indicator
- MACD Indicator
- Buy vs Sell Signals
- Current Market Price

---

### 2. Performance Dashboard

Displays:

- Win Rate
- Sharpe Ratio
- Maximum Drawdown
- Portfolio Value
- Total Trades

---

### 3. Risk Dashboard

Displays:

- Position Size
- Value at Risk (VaR)
- Conditional VaR
- Stop Loss
- Take Profit
- Risk-Reward Ratio

---

### 4. Monte Carlo Dashboard

Displays:

- Future Price Path Simulation
- Forecast Visualization

---

### 5. Advanced Analytics Dashboard

Displays:

- Total Trades
- Buy Percentage
- Sell Percentage
- Average Confidence
- Total Buy Signals
- Total Sell Signals
- Latest Trading Signal
- Latest Close Price

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Power BI Desktop

---

# 📁 Project Structure

```text
Project_1C_Forex_AI_Agent/

│── data/
│── models/
│── powerbi/
│── reports/
│── src/

│── README.md
│── requirements.txt
│── LICENSE
```

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone git clone https://github.com/Suvasini911/Forex_AI_Agent.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Python modules

Run the scripts in sequence:

- Technical Indicator Engine
- Machine Learning Engine
- Performance Engine
- Risk Engine
- Monte Carlo Simulation
- Reinforcement Learning Agent

### 4. Open Power BI

Open:

```
Forex_AI_Trading_Dashboard.pbix
```

Refresh the data to load the latest outputs.

---

# 📸 Dashboard Preview

Include screenshots in the `reports/` folder:

- Trading Dashboard
- Performance Dashboard
- Risk Dashboard
- Monte Carlo Dashboard
- Advanced Analytics Dashboard

---

# 🚀 Future Improvements

- PPO Reinforcement Learning
- Deep Q Network (DQN)
- A2C Reinforcement Learning
- Live Forex API Integration
- Real-time Dashboard Refresh
- Automated Trade Execution

---

# 👩‍💻 Author

**Suvasini**

Bachelor of Technology (Computer Science & Engineering)

CMR University, Bengaluru

---

# 📄 License

This project is developed for educational and academic purposes.
