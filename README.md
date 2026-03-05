# India Stock Vision 2026 🇮🇳
An open-source Large Scale Stock Prediction Model focusing on the **NSE (Nifty 50)** and **BSE (Sensex)**.

### 🏗 Architecture
- **Data Ingestion:** Automated fetching via `yfinance`.
- **Feature Engineering:** Technical indicators (RSI, SMA, Volatility).
- **Model:** Stacked LSTM (Long Short-Term Memory) with Dropout for volatility handling.
- **Environment:** Developed on Google Colab, deployed via GitHub.

### 📁 Structure
- `/src`: Modular Python scripts for the ML pipeline.
- `/data`: Raw and processed market data.
- `/notebooks`: Interactive Colab files for visualization.
