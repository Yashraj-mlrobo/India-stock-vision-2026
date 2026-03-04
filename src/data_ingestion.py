
import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(tickers, start_date, end_date, save_path='data/raw/'):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = yf.download(ticker, start=start_date, end=end_date)
        file_name = f"{ticker.replace('^', '')}.csv"
        df.to_csv(os.path.join(save_path, file_name))
        print(f"Saved {ticker} to {save_path}{file_name}")

if __name__ == "__main__":
    # Indian Indices
    indian_indices = ["^NSEI", "^BSESN"]
    fetch_stock_data(indian_indices, "2020-01-01", "2026-03-04")
