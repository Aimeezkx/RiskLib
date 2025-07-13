import matplotlib.pyplot as plt
from core.simulator import generate_price_paths
from core.var_calculator import monte_carlo_var

# Simulation parameters
S0 = 100       # Initial asset price
mu = 0.05      # Expected return
sigma = 0.2    # Volatility
T = 1.0        # Time horizon (1 year)
steps = 252    # Number of steps (daily)
n_paths = 1000 # Number of simulated paths

# Run simulation
paths = generate_price_paths(S0, mu, sigma, T, steps, n_paths, seed=42)

# Plot simulated paths
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.plot(paths[i], lw=0.8)
plt.title('Simulated Asset Price Paths')
plt.xlabel('Time Step')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.show()

# Compute daily returns and VaR
final_prices = paths[:, -1]
returns = (final_prices - S0) / S0
var_95 = monte_carlo_var(returns, confidence_level=0.95)

print(f"Monte Carlo Estimated 1-Year VaR (95% confidence): {var_95:.2%}")
