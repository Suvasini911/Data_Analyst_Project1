import pandas as pd
import numpy as np

def compute_indicators(df):
    """
    Computes professional-grade technical analysis indicators on Forex data.
    """
    # 1. Simple Moving Averages (SMA)
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # Exponential Moving Averages (EMA)
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    # 2. Relative Strength Index (RSI - 14 Period)
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta.where(delta < 0, 0.0))
    
    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()
    
    rs = avg_gain / (avg_loss + 1e-9)
    df['RSI_14'] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema26 = df['Close'].ewm(span=26, adjust=False).mean()
    
    df['MACD'] = ema12 - ema26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Histogram'] = df['MACD'] - df['MACD_Signal']

          # Bollinger Bands
    rolling_mean = df['Close'].rolling(window=20).mean()
    rolling_std = df['Close'].rolling(window=20).std()

    df['BB_Middle'] = rolling_mean
    df['BB_Upper'] = rolling_mean + (2 * rolling_std)
    df['BB_Lower'] = rolling_mean - (2 * rolling_std)

    # Average True Range (ATR)
    high_low = df['High'] - df['Low']
    high_close = abs(df['High'] - df['Close'].shift())
    low_close = abs(df['Low'] - df['Close'].shift())
    
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)

    df['ATR_14'] = true_range.rolling(window=14).mean()

    # Ichimoku Cloud
    nine_high = df['High'].rolling(window=9).max()
    nine_low = df['Low'].rolling(window=9).min()

    df['Tenkan'] = (nine_high + nine_low) / 2

    twentysix_high = df['High'].rolling(window=26).max()
    twentysix_low = df['Low'].rolling(window=26).min()

    df['Kijun'] = (twentysix_high + twentysix_low) / 2

    df['Senkou_A'] = ((df['Tenkan'] + df['Kijun']) / 2).shift(26)

    fiftytwo_high = df['High'].rolling(window=52).max()
    fiftytwo_low = df['Low'].rolling(window=52).min()

    df['Senkou_B'] = ((fiftytwo_high + fiftytwo_low) / 2).shift(26)

    df['Chikou'] = df['Close'].shift(-26)
    
    # 3. Trend Cross Signal Generation Logic
    # 3. Trend Cross Signal Generation Logic
    # 3. Composite Trading Signal Logic

    df['Signal'] = 'HOLD'

    buy_condition = (
    (df['SMA_10'] > df['SMA_50']) &
    (df['RSI_14'] < 70) &
    (df['MACD'] > df['MACD_Signal'])
)

    sell_condition = (
    (df['SMA_10'] < df['SMA_50']) &
    (df['RSI_14'] > 30) &
    (df['MACD'] < df['MACD_Signal'])
)

    df.loc[buy_condition, 'Signal'] = 'BUY'
    df.loc[sell_condition, 'Signal'] = 'SELL'
    
    return df

# Load the project dataset from the 'data' subfolder
try:
    print("Loading forex_price_data.csv from the data folder...")
    market_data = pd.read_csv('data/forex_price_data.csv')
    
    # Process indicators
    processed_data = compute_indicators(market_data)
    
    # Save the output inside the data folder
    processed_data.to_csv('data/processed_market_data.csv', index=False)
    print("--- SUCCESS: INDICATORS COMPUTED ---")
    print("New file created: 'data/processed_market_data.csv'")
    
    # Display the latest calculation records
    print("\nDisplaying latest processed records:")
    print(
    processed_data[
        [
            'DateTime',
            'Close',
            'SMA_10',
            'EMA_10',
            'RSI_14',
            'MACD',
            'ATR_14',
            'Signal'
        ]
    ].tail(5)
)    
except Exception as e:
    print(f"An error occurred: {e}")