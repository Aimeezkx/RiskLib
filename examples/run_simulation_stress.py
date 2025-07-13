import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from core.simulator import generate_price_paths
from core.var_calculator import monte_carlo_var
from core.stress import apply_stress_scenario

# Base simulation parameters
S0 = 100
mu = 0.05
sigma = 0.2
T = 1.0
steps = 252
n_paths = 1000
confidence_level = 0.95

# Run baseline simulation
paths = generate_price_paths(S0, mu, sigma, T, steps, n_paths, seed=42)
final_prices = paths[:, -1]
returns = (final_prices - S0) / S0
baseline_var = monte_carlo_var(returns, confidence_level)

# Plot some sample paths
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.plot(paths[i], lw=0.8)
plt.title('Simulated Asset Price Paths (Baseline)')
plt.xlabel('Time Step')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Baseline Monte Carlo Estimated {int(confidence_level * 100)}% VaR: {baseline_var:.2%}")

# Run stress scenario: combined vol spike + price drop
stress_returns = apply_stress_scenario(
    S0=S0, mu=mu, sigma=sigma, T=T, steps=steps,
    n_paths=n_paths, shock_type='combined', shock_value=0.1
)
stress_var = monte_carlo_var(stress_returns, confidence_level)

# Plot histogram of stressed returns
plt.figure(figsize=(8, 4))
plt.hist(stress_returns, bins=50, alpha=0.7, color='orange')
plt.title('Distribution of Returns Under Combined Stress')
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Stressed Monte Carlo Estimated {int(confidence_level * 100)}% VaR: {stress_var:.2%}")
