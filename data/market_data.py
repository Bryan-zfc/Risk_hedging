import yfinance as yf
import pandas as pd
from datetime import datetime



def get_spot_price(ticker):
   
    # Get the most recent price of the underlying stock

    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1] #Fetch the most recent price
    return float(price)


def get_option_chain(ticker, expiry):
    
    # Get the calls and puts dataframes for a given expiry date

    stock = yf.Ticker(ticker)
    chain = stock.option_chain(expiry)
    return chain.calls, chain.puts


def get_expirations(ticker: str):
    
    # Get a list of the available expirations of options
    stock = yf.Ticker(ticker)
    return stock.options


def time_to_maturity(expiry):
   
    # Compute time to maturity

    expiry_date = pd.to_datetime(expiry)
    today = pd.Timestamp.today()
    T = (expiry_date - today).days / 365.0
    return T


def get_dividend_yield(ticker: str) -> float:
   
    # Gain the dividend yield
    
    stock = yf.Ticker(ticker)
    info = stock.info

    if "dividendYield" in info and info["dividendYield"] is not None:
        return float(info["dividendYield"])
    else:
        return 0.0

