import yfinance as yf


def get_stock_prices():

    # tickers
    nvidia = yf.Ticker("NVDA")
    # iShares Core MSCI World UCITS ETF (Acc)
    world_etf = yf.Ticker("IWDA.AS")

    # latest prices
    nvda_price = nvidia.history(period="1d")["Close"].iloc[-1]
    etf_price = world_etf.history(period="1d")["Close"].iloc[-1]

    return f"""
Nvidia (NVDA): ${nvda_price:.2f}
iShares Core MSCI World ETF (IWDA): ${etf_price:.2f}
"""
