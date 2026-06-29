# 📈 Stock Market Strategy Backtester

An interactive web application that evaluates a **Moving Average Crossover Trading Strategy** using historical stock market data from **Yahoo Finance**. The application compares the strategy's performance against a traditional **Buy & Hold** investment approach and provides detailed visualizations, performance metrics, and downloadable reports.

---

## 🚀 Live Demo

**Streamlit App:** *http://stock-market-strategy-backtester.streamlit.app/*

---

## 📷 Screenshots

### Dashboard

<img width="1919" height="969" alt="home" src="https://github.com/user-attachments/assets/76ce9c2e-742f-4492-b9d0-a552ed780181" />


### Charts

<img width="1408" height="835" alt="charts" src="https://github.com/user-attachments/assets/a988fcdd-93ea-494e-97c6-86db4d23b09c" />


### Performance Overview

<img width="1427" height="576" alt="overview" src="https://github.com/user-attachments/assets/58afa846-104c-4287-8573-9f481dfa4ab2" />


---

# ✨ Features

* Download historical stock data from Yahoo Finance
* Support for Indian and US stocks
* Calculate 20-Day and 50-Day Moving Averages
* Generate Buy/Sell trading signals
* Backtest Moving Average Crossover Strategy
* Compare Strategy vs Buy & Hold performance
* Interactive Streamlit dashboard
* Portfolio value simulation
* Performance summary
* Download historical dataset as CSV
* Download performance report as TXT

---

# 📊 Trading Strategy

The application implements a **Moving Average Crossover Strategy**.

### Buy Signal

A BUY signal is generated when:

* 20-Day Moving Average crosses **above** the 50-Day Moving Average.

### Sell Signal

A SELL signal is generated when:

* 20-Day Moving Average crosses **below** the 50-Day Moving Average.

---

# 📈 Performance Metrics

The dashboard displays:

* Strategy Return (%)
* Buy & Hold Return (%)
* Outperformance (%)
* Total Trading Signals
* Trading Days
* Initial Capital
* Latest Stock Price
* Portfolio Value
* Highest Price
* Lowest Price

---

# 📉 Charts

The application provides four interactive charts:

* Stock Closing Price
* Moving Average Crossover
* Buy/Sell Signal Visualization
* Strategy Portfolio vs Buy & Hold Portfolio

---

# 🛠 Tech Stack

### Backend

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Streamlit
* yfinance

### Data Source

* Yahoo Finance

---

# 📁 Project Structure

```
Stock-Market-Strategy-Backtester/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── src/
│   ├── data_loader.py
│   ├── indicators.py
│   ├── strategy.py
│   ├── backtester.py
│   ├── visualization.py
│
├── data/
└── screenshots/
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Bhumi2006-bit/Stock-Market-Strategy-Backtester.git
```

Move into the project directory

```bash
cd Stock-Market-Strategy-Backtester
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Start the Streamlit app

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📄 Example Inputs

Ticker

```
TCS.NS
```

or

```
RELIANCE.NS
```

or

```
INFY.NS
```

or

```
AAPL
```

Start Date

```
2020-01-01
```

End Date

```
2025-12-31
```

Initial Capital

```
100000
```

---

# 📥 Output

The application generates:

* Historical Stock Dataset (CSV)
* Performance Summary (TXT)
* Interactive Dashboard
* Strategy Charts

---

# 🔮 Future Improvements

* Additional technical indicators (RSI, MACD, Bollinger Bands)
* Multiple trading strategies
* Candlestick charts
* Portfolio optimization
* Risk metrics (Sharpe Ratio, Maximum Drawdown)
* Transaction cost simulation
* Multi-stock comparison
* Strategy parameter optimization

---

# 👩‍💻 Author

**Bhumi Asati**

GitHub: https://github.com/Bhumi2006-bit

LinkedIn: https://www.linkedin.com/in/bhumi-asati-31b509280

---

# 📜 License

This project is licensed under the MIT License.
