import pandas as pd
import numpy as np

def apply_features(df):
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # RSI Calculation
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # Volatility
    df['Daily_Volatility'] = df['High'] - df['Low']
    return df.dropna()

if __name__ == "__main__":
    df = pd.read_csv('data/raw/NSEI.csv', index_col=0, parse_dates=True)
    processed = apply_features(df)
    processed.to_csv('data/processed/NSEI_features.csv')
    print("Feature Engineering Complete.")
