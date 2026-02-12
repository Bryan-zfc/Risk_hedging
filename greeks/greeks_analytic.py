import numpy as np
from scipy.stats import norm

# S0 = current stock prize
# K = Strike prize
# T = Expiration time
# r = interest
# sigma = volatility
# q = dividend

# Computing the Greeks using the BS model. 

def black_scholes_dplus(S0, K, T, r, sigma, q=0.0):
    # Compute the d+ term in BS
    return (np.log(S0 / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def analytic_delta_call(S0, K, T, r, sigma, q=0.0):
    dplus = black_scholes_dplus(S0, K, T, r, sigma, q)
    return np.exp(-q * T) * norm.cdf(dplus)


def analytic_delta_put(S0, K, T, r, sigma, q=0.0):
    dplus = black_scholes_dplus(S0, K, T, r, sigma, q)
    return np.exp(-q * T) * (norm.cdf(dplus) - 1)

def analytic_delta(S0, K, T, r, sigma, q=0.0, option_type = "call"):
    dplus = black_scholes_dplus(S0, K, T, r, sigma, q)
    if option_type == "call":
        return np.exp(-q * T) * norm.cdf(dplus)
    elif option_type == "put":
        return np.exp(-q * T) * (norm.cdf(dplus) - 1)

def analytic_gamma(S0, K, T, r, sigma, q=0.0, option_type = "call"):
     dplus = black_scholes_dplus(S0, K, T, r, sigma, q)
     return  norm.pdf(dplus) / (S0 * sigma * np.sqrt(T))

def analytic_vega(S0, K, T, r, sigma, q=0.0, option_type = "call"):
     dplus = black_scholes_dplus(S0, K, T, r, sigma, q)
     return norm.pdf(dplus) * S0 * np.sqrt(T)


