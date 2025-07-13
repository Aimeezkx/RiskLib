from core.simulator import generate_price_paths

def apply_stress_scenario(S0, mu, sigma, T, steps, n_paths, shock_type='vol_spike', shock_value=0.1):
    '''
    Applies a stress scenario and returns the final returns distribution.

    Parameters:
        S0: float - initial price
        mu: float - expected return
        sigma: float - volatility
        T: float - time horizon
        steps: int - number of time steps
        n_paths: int - number of simulation paths
        shock_type: str - type of stress ('vol_spike', 'price_drop', 'combined')
        shock_value: float - magnitude of stress

    Returns:
        np.ndarray: final returns under stress
    '''
    if shock_type == 'vol_spike':
        stressed_sigma = sigma + shock_value
        stressed_mu = mu
    elif shock_type == 'price_drop':
        stressed_mu = mu - shock_value
        stressed_sigma = sigma
    elif shock_type == 'combined':
        stressed_mu = mu - shock_value
        stressed_sigma = sigma + shock_value
    else:
        raise ValueError("Unsupported shock_type. Use 'vol_spike', 'price_drop', or 'combined'.")

    paths = generate_price_paths(S0, stressed_mu, stressed_sigma, T, steps, n_paths)
    final_prices = paths[:, -1]
    returns = (final_prices - S0) / S0
    return returns
