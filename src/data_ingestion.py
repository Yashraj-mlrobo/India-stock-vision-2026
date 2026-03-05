import yfinance as yf
import pandas as pd
import os

def fetch_and_clean_data(ticker="^NSEI", start="2020-01-01"):
    df = yf.download(ticker, start=start)
    # Flattening yfinance multi-index
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv(f'data/raw/{ticker.replace("^", "")}.csv')
    return df

if __name__ == "__main__":
    fetch_and_clean_data("^NSEI")
    fetch_and_clean_data("^BSESN")
    print("Data Ingestion Complete.")
