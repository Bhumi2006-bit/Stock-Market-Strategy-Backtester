import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from backtester import backtest_strategy
from data_loader import download_stock_data
from indicators import calculate_indicators
from strategy import generate_signals
from datetime import date, timedelta


st.set_page_config(
    page_title="Stock Market Strategy Backtester",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Market Strategy Backtester")

st.markdown(
    "Evaluate a **Moving Average Crossover** trading strategy using historical stock data "
    "from Yahoo Finance and compare its performance against a **Buy & Hold** strategy."
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Strategy Inputs")

ticker = st.sidebar.text_input("Ticker", value="TCS.NS")

start_date = st.sidebar.date_input(
    "Start Date",
    value=pd.to_datetime("2020-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    value=date.today() - timedelta(days=1)
)

capital = st.sidebar.number_input(
    "Initial Capital",
    value=100000,
    step=10000
)

run = st.sidebar.button("🚀 Run Backtest", use_container_width=True)

st.sidebar.info("Examples:\n\n• TCS.NS\n\n• RELIANCE.NS\n\n• INFY.NS\n\n• AAPL\n\n• MSFT")

# -----------------------------
# Session State
# -----------------------------

if "df" not in st.session_state:
    st.session_state.df = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "error" not in st.session_state:
    st.session_state.error = None

# -----------------------------
# Run Backtest
# -----------------------------

if run:
    # Reset previous state
    st.session_state.df = None
    st.session_state.summary = None
    st.session_state.error = None

    error_msg = None

    with st.spinner("Downloading data and running backtest..."):

        df = download_stock_data(ticker, str(start_date), str(end_date))

        if df is None:
            error_msg = "❌ Invalid ticker or no data found. Please enter a valid Yahoo Finance ticker."
        else:
            try:
                df = calculate_indicators(df)
                df = generate_signals(df)
                df = backtest_strategy(df, capital)

                strategy_return = (
                    (df["Portfolio Value"].iloc[-1] - capital) / capital
                ) * 100

                buy_hold_return = (
                    (df["Buy Hold Value"].iloc[-1] - capital) / capital
                ) * 100

                outperformance = strategy_return - buy_hold_return
                total_signals = df["Signal"].diff().fillna(0).ne(0).sum()

                summary = {
                    "strategy_return": strategy_return,
                    "buy_hold_return": buy_hold_return,
                    "outperformance": outperformance,
                    "signals": total_signals,
                    "final_portfolio": df["Portfolio Value"].dropna().iloc[-1],
                    "latest_price": df["Close"].dropna().iloc[-1],
                    "highest": df["High"].max(),
                    "lowest": df["Low"].min(),
                }

                st.session_state.df = df
                st.session_state.summary = summary

            except ValueError as e:
                error_msg = f"❌ {e}"

            except Exception:
                error_msg = "❌ Something went wrong while processing the stock data."

    # Show error or success AFTER spinner closes
    if error_msg:
        st.session_state.error = error_msg
    else:
        st.success("✅ Backtest completed successfully!")

# Show persistent error if any
if st.session_state.error:
    st.error(st.session_state.error)
    st.stop()

# -----------------------------
# Nothing executed yet
# -----------------------------

if st.session_state.df is None:
    st.info("Configure inputs in the sidebar and click **Run Backtest** to get started.")
    st.stop()

df = st.session_state.df
summary = st.session_state.summary

# -----------------------------
# Top Metrics
# -----------------------------

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("📈 Strategy Return", f"{summary['strategy_return']:.2f}%")
m2.metric("📊 Buy & Hold", f"{summary['buy_hold_return']:.2f}%")
m3.metric("⚖️ Outperformance", f"{summary['outperformance']:.2f}%")
m4.metric("🔄 Signals", int(summary["signals"]))
m5.metric("📅 Trading Days", len(df))

st.divider()

m6, m7, m8, m9, m10 = st.columns(5)
m6.metric("💵 Initial Capital", f"₹{capital:,.0f}")
m7.metric("📈 Latest Price", f"₹{summary['latest_price']:.2f}")
m8.metric("💼 Portfolio Value", f"₹{summary['final_portfolio']:,.0f}")
m9.metric("📈 Highest Price", f"₹{summary['highest']:.2f}")
m10.metric("📉 Lowest Price", f"₹{summary['lowest']:.2f}")

st.divider()

overview_tab, charts_tab, data_tab, download_tab, about_tab = st.tabs(
    ["📊 Overview", "📈 Charts", "📄 Dataset", "⬇ Downloads", "ℹ About"]
)

# ======================================================
# ABOUT TAB
# ======================================================

with about_tab:

    st.subheader("About the Project")

    st.markdown("""
### How to Use

1. Enter a valid Yahoo Finance ticker (e.g. TCS.NS, RELIANCE.NS, AAPL).
2. Select a date range.
3. Choose the initial investment amount.
4. Click **Run Backtest**.
5. View the strategy performance, charts, and download the results.

---

### Overview

This app evaluates a **Moving Average Crossover** trading strategy using historical stock data
from Yahoo Finance, backtested over a user-defined period and compared against Buy & Hold.

### Trading Strategy

- **Buy** when the 20-Day MA crosses above the 50-Day MA.
- **Sell** when the 20-Day MA crosses below the 50-Day MA.

### Technologies

Python · Pandas · NumPy · Matplotlib · Streamlit · yfinance

### Key Features

- Download historical stock data
- Calculate moving averages and generate signals
- Backtest trading strategy vs Buy & Hold
- Interactive charts and exportable results
""")

# ======================================================
# OVERVIEW TAB
# ======================================================

with overview_tab:

    st.subheader("Performance Summary")

    summary_df = pd.DataFrame({
        "Metric": [
            "Initial Capital",
            "Final Portfolio Value",
            "Strategy Return",
            "Buy & Hold Return",
            "Outperformance",
            "Trading Signals",
            "Trading Days"
        ],
        "Value": [
            f"₹{capital:,.2f}",
            f"₹{summary['final_portfolio']:,.2f}",
            f"{summary['strategy_return']:.2f}%",
            f"{summary['buy_hold_return']:.2f}%",
            f"{summary['outperformance']:.2f}%",
            int(summary["signals"]),
            len(df)
        ]
    })

    st.dataframe(summary_df, hide_index=True, use_container_width=True)

# ======================================================
# CHARTS TAB
# ======================================================

with charts_tab:

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.subheader("📈 Stock Price")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["Date"], df["Close"], linewidth=2)
        ax.set_title("Closing Price")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

    with row1_col2:
        st.subheader("📊 Moving Average")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["Date"], df["Close"], label="Close")
        ax.plot(df["Date"], df["MA20"], label="20 MA")
        ax.plot(df["Date"], df["MA50"], label="50 MA")
        ax.set_title("Moving Average Crossover")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.subheader("🟢 Buy / Sell Signals")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["Date"], df["Close"], label="Close")
        buy = df[df["Signal"] == 1]
        sell = df[df["Signal"] == -1]
        ax.scatter(buy["Date"], buy["Close"], marker="^", color="green", s=80, label="BUY")
        ax.scatter(sell["Date"], sell["Close"], marker="v", color="red", s=80, label="SELL")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

    with row2_col2:
        st.subheader("💰 Portfolio Comparison")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df["Date"], df["Portfolio Value"], label="Strategy")
        ax.plot(df["Date"], df["Buy Hold Value"], label="Buy & Hold")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
        plt.close(fig)

# ======================================================
# DATA TAB
# ======================================================

with data_tab:
    st.subheader("Historical Dataset")
    st.write(f"Rows : {len(df)} | Columns : {len(df.columns)}")
    st.dataframe(df, use_container_width=True)

# ======================================================
# DOWNLOAD TAB
# ======================================================

with download_tab:
    st.subheader("Download Results")
    st.write("Download the processed dataset and performance report.")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Historical Data",
        csv,
        file_name="historical_stock_data.csv",
        mime="text/csv"
    )

    report = f"""
====================================
Performance Summary
====================================

Ticker             : {ticker}
Initial Capital    : ₹{capital:,.2f}
Final Portfolio    : ₹{summary['final_portfolio']:,.2f}
Strategy Return    : {summary['strategy_return']:.2f} %
Buy & Hold Return  : {summary['buy_hold_return']:.2f} %
Outperformance     : {summary['outperformance']:.2f} %
Signals Generated  : {int(summary['signals'])}
Trading Days       : {len(df)}
"""

    st.download_button(
        "📄 Download Performance Summary",
        report,
        file_name="performance_summary.txt",
        mime="text/plain"
    )