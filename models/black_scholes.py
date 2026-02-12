import numpy as np
from scipy.stats import norm


#Computing the analytic option prices using Black Scholes for European options. Will try to add models for American options later.

def dplus(S0, K, T, r, sigma, q=0.0):
    # Compute the d+ term in BS
    return (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def dminus(S0, K, T, r, sigma, q=0.0):
    # Compute the d- term
    return dplus(S0, K, T, r, sigma, q) - sigma * np.sqrt(T)


def bs_call_price(S0, K, T, r, sigma, q=0.0):
    # The analytic price of a (European) call option using BS
    d_1 = dplus(S0, K, T, r, sigma, q)
    d_2 = dminus(S0, K, T, r, sigma, q)
  
    return (
        S0 * np.exp(-q * T) * norm.cdf(d_1)
        - K * np.exp(-r * T) * norm.cdf(d_2)
    )

def bs_put_price(S0, K, T, r, sigma, q=0.0):
    # The analytic price of a (European) put option using BS
    
    d_1 = dplus(S0, K, T, r, sigma, q)
    d_2 = dminus(S0, K, T, r, sigma, q)

    return (
        K * np.exp(-r * T) * norm.cdf(-d_2)
        - S0 * np.exp(-q * T) * norm.cdf(-d_1)
    )

