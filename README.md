# RiskLib: A Modular Monte Carlo VaR and Stress Testing Library

## Overview

**RiskLib** is a production-style Python library for **Monte Carlo simulation**, **Value-at-Risk (VaR)** computation, and **scenario-based stress testing**.

---

## Features

- Monte Carlo simulation engine for GBM-based asset price paths
- Historical, Parametric, and Monte Carlo-based VaR estimations
- Scenario stress testing with volatility and drift shock support
- Modular, testable architecture using clean Python packages
- CLI-based interface using YAML configs
- Includes unit tests for all core risk components

---

## Directory Structure

```
RiskLib/
├── config/
│   └── base_config.yaml         # YAML config for CLI
├── core/
│   ├── simulator.py             # Monte Carlo simulation engine
│   ├── var_calculator.py        # Historical / parametric / MC VaR
│   ├── stress.py                # Stress test logic
│   └── __init__.py
├── examples/
│   ├── run_simulation.py        # Standard simulation runner
│   └── run_simulation_stress.py # Extended stress scenario demo
├── tests/
│   └── test_stress.py           # pytest unit tests for stress module
├── cli.py                       # Command-line entry point
├── README.md                    # This file
└── requirements.txt             # Package requirements
```

---

## Quick Start

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Run simulation**

```bash
python -m examples.run_simulation
```

3. **Run stress scenario**

```bash
python -m examples.run_simulation_stress
```

4. **Run from CLI**

```bash
python cli.py --method montecarlo --config config/base_config.yaml
```

---

## Author

**Kaixin Zheng**  
Quantitative Risk Analyst | Python Risk Engineer  
[LinkedIn](https://www.linkedin.com/in/kaixin-zheng/)

---

## License

MIT License
