import numpy as np
from scipy.stats import norm

# Computing the numerical delta of a price function by computing the slope over a very small increment (f'(x) = f(x-e)+f(x+e)/ 2e when e --> 0 )
def numerical_delta(price_func, S0, eps=1e-4):

    return (price_func(S0 + eps) - price_func(S0 - eps)) / (2 * eps)
