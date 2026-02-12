import numpy as np
from scipy.optimize import brentq
from models.black_scholes import bs_call_price, bs_put_price

#Using brentq (i.e. Brent's root finding method) to find the volatilty used to get the market option prize under the BS model. 

def implied_vol_call(market_price, S0, K, T, r, q=0.0):
    def objective(sigma):
        return bs_call_price(S0, K, T, r, sigma, q) - market_price
    return brentq(objective, 1e-6, 5.0)


def implied_vol_put(market_price, S0, K, T, r, q=0.0):
    def objective(sigma):
        return bs_put_price(S0, K, T, r, sigma, q) - market_price
    return brentq(objective, 1e-6, 5.0)
