import pandas as pd
import numpy as np

def add_technical_indicators(df):
    # To ensure data is sorted by date
    df = df.sort_index()
    
    # 1. Moving Averages (50-day and 200-day)
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # 2. RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # 3. Daily Returns
    df['Daily_Return'] = df['Close'].pct_change()
    
    return df.dropna()

if __name__ == "__main__":
    import os
    # Load raw data
    raw_path = 'data/raw/NSEI.csv'
    if os.path.exists(raw_path):
        df = pd.read_csv(raw_path, index_col='Date', parse_dates=True)
        processed_df = add_technical_indicators(df)
        
        # Save to processed folder
        processed_df.to_csv('data/processed/NSEI_features.csv')
        print("Feature engineering complete. Saved to data/processed/NSEI_features.csv")
