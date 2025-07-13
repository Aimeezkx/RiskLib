import argparse
import yaml
from core.simulator import generate_price_paths
from core.var_calculator import monte_carlo_var

def main():
    parser = argparse.ArgumentParser(description='Run Monte Carlo Simulation and VaR')
    parser.add_argument('--method', type=str, default='montecarlo', help='Method: montecarlo')
    parser.add_argument('--config', type=str, required=True, help='Path to YAML config file')
    args = parser.parse_args()

    # Load config
    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    S0 = config['S0']
    mu = config['mu']
    sigma = config['sigma']
    T = config['T']
    steps = config['steps']
    n_paths = config['n_paths']
    confidence = config.get('confidence_level', 0.95)

    print(f"Running Monte Carlo simulation with {n_paths} paths...")
    paths = generate_price_paths(S0, mu, sigma, T, steps, n_paths)

    final_prices = paths[:, -1]
    returns = (final_prices - S0) / S0
    var = monte_carlo_var(returns, confidence)

    print(f"Monte Carlo Estimated {int(confidence*100)}% VaR: {var:.2%}")

if __name__ == '__main__':
    main()
