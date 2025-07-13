import numpy as np
from scipy.stats import norm

def historical_var(returns, confidence_level=0.95):
    sorted_returns = np.sort(returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    return -sorted_returns[index]

def parametric_var(mu, sigma, confidence_level=0.95):
    return - (mu + sigma * norm.ppf(1 - confidence_level))

def monte_carlo_var(simulated_returns, confidence_level=0.95):
    sorted_returns = np.sort(simulated_returns)
    index = int((1 - confidence_level) * len(sorted_returns))
    return -sorted_returns[index] 