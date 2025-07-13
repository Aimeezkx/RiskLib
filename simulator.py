import numpy as np

def generate_price_paths(S0, mu, sigma, T, steps, n_paths, seed=None):
    if seed:
        np.random.seed(seed)
    dt = T / steps
    paths = np.zeros((n_paths, steps + 1))
    paths[:, 0] = S0
    for t in range(1, steps + 1):
        z = np.random.standard_normal(n_paths)
        paths[:, t] = paths[:, t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
    return paths
