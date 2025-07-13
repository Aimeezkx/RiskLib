import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from core.stress import apply_stress_scenario

def test_apply_stress_scenario_returns_shape():
    returns = apply_stress_scenario(
        S0=100, mu=0.05, sigma=0.2, T=1.0, steps=252, n_paths=1000,
        shock_type='vol_spike', shock_value=0.1
    )
    assert isinstance(returns, np.ndarray)
    assert returns.shape == (1000,)

def test_invalid_shock_type():
    try:
        apply_stress_scenario(
            S0=100, mu=0.05, sigma=0.2, T=1.0, steps=252, n_paths=1000,
            shock_type='invalid', shock_value=0.1
        )
        assert False, "Expected ValueError for invalid shock_type"
    except ValueError as e:
        assert "Unsupported shock_type" in str(e)
