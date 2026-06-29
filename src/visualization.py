import os
import matplotlib.pyplot as plt


plt.style.use("ggplot")


def create_plots(df, ticker):

    os.makedirs("../plots", exist_ok=True)

    # ============================
    # 1. Stock Price
    # ============================

    plt.figure(figsize=(12,6))

    plt.plot(
        df["Date"],
        df["Close"],
        linewidth=2,
        label="Close Price"
    )

    plt.title(
        f"{ticker} Closing Price",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "../plots/stock_price.png",
        dpi=300
    )

    plt.close()

    # ============================
    # 2. Moving Average
    # ============================

    plt.figure(figsize=(12,6))

    plt.plot(
        df["Date"],
        df["Close"],
        linewidth=2,
        label="Close"
    )

    plt.plot(
        df["Date"],
        df["MA20"],
        linewidth=2,
        label="20 Day MA"
    )

    plt.plot(
        df["Date"],
        df["MA50"],
        linewidth=2,
        label="50 Day MA"
    )

    plt.title(
        "Moving Average Strategy",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "../plots/moving_average.png",
        dpi=300
    )

    plt.close()

    # ============================
    # 3. Buy Sell Signals
    # ============================

    plt.figure(figsize=(14,6))

    plt.plot(
        df["Date"],
        df["Close"],
        linewidth=2,
        label="Close Price"
    )

    buy = df[df["Signal"] == 1]

    sell = df[df["Signal"] == -1]

    plt.scatter(
        buy["Date"],
        buy["Close"],
        marker="^",
        s=120,
        label="BUY"
    )

    plt.scatter(
        sell["Date"],
        sell["Close"],
        marker="v",
        s=120,
        label="SELL"
    )

    plt.title(
        "Trading Signals",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "../plots/buy_sell_signals.png",
        dpi=300
    )

    plt.close()

    # ============================
    # 4. Portfolio Comparison
    # ============================

    plt.figure(figsize=(12,6))

    plt.plot(
        df["Date"],
        df["Portfolio Value"],
        linewidth=2,
        label="Strategy"
    )

    plt.plot(
        df["Date"],
        df["Buy Hold Value"],
        linewidth=2,
        label="Buy & Hold"
    )

    plt.title(
        "Strategy vs Buy & Hold",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date")

    plt.ylabel("Portfolio Value")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "../plots/cumulative_returns.png",
        dpi=300
    )

    plt.close()

    print("\nGraphs generated successfully!")