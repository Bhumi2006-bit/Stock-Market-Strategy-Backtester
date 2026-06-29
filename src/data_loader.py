import os
import pandas as pd
import yfinance as yf


def download_stock_data(ticker: str, start_date: str, end_date: str):
    """
    Downloads historical stock data from Yahoo Finance.
    Returns None if ticker is invalid or data is unavailable.
    """

    print("\nDownloading historical stock data...\n")

    try:
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False
        )
    except Exception:
        return None

    if df is None or df.empty:
        return None

    # Fix MultiIndex columns returned by latest yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    numeric_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

    try:
        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column])
    except Exception:
        return None

    os.makedirs("../data", exist_ok=True)
    df.to_csv("../data/historical_stock_data.csv", index=False)

    print(f"Downloaded {len(df)} rows successfully.")

    return df