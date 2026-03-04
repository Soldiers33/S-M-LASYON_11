# AI Coding Agent Instructions for S-M-LASYON_11

## Project Overview
This is a scientific simulation proving the universe operates on an 11-based (undecimal) organic kernel rather than decimal (base-10). The project validates this theory using NASA datasets, Monte Carlo simulations, and Bayesian inference (p < 0.0001 statistical significance).

## Core Architecture

### Main Components
- **`simulasyon_11.py`** (1596 lines): Core simulation engine with mathematical models
- **`levhi_mahfuz.py`** (411 lines): Central constants repository ("Sacred Tablet")
- **`event_window_monitoring_system.py`** (582 lines): 2033-2035 event monitoring system
- **`antigravity_bridge.py`** (257 lines): Real-time data processor from external sources
- **`dashboard_11.py`** (501 lines): Flask web dashboard for visualization

### Data Flow
1. External data → `antigravity_bridge.py` → validation against `levhi_mahfuz.py` constants
2. Validated data → `simulasyon_11.py` → mathematical modeling
3. Results → `event_window_monitoring_system.py` → anomaly detection
4. Output → `dashboard_11.py` → web interface

## Critical Workflows

### Running Simulations
```bash
python3 simulasyon_11.py  # Main simulation (outputs to results.txt)
```

### Validation & Testing
```bash
python3 test_11_dimensional_constants.py  # Unit tests for constants
python3 verify_constants.py              # Cross-reference with NASA data
python3 process_discoveries.py           # Process new discoveries
```

### Analysis & Deployment
```bash
python3 dashboard_11.py  # Start Flask dashboard (localhost:5000)
# Or use COLAB_MEGA_ANALYSIS.ipynb for comprehensive analysis
```

## Project-Specific Patterns

### Constants Organization
- Use `LevhiMahfuzConstants` class in `levhi_mahfuz.py` for all universal constants
- Constants validated against authoritative sources (NASA, Wikipedia, IAU)
- 11-based mathematics: prefer calculations involving 11, 111, 11111111111

### Code Structure
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MODULE DESCRIPTION
Date: YYYY-MM-DD
Purpose: Brief purpose statement
"""

# Imports in order: standard library, third-party, local
import math
import json
from datetime import datetime
from levhi_mahfuz import LevhiMahfuzConstants

class ModuleConstants:
    """All constants for this module"""
    VALUE = 123.456

def main_function():
    """Main processing logic"""
    # Use constants from LevhiMahfuzConstants
    base = LevhiMahfuzConstants.BASE_SYSTEM  # = 11
    # ... implementation
```

### Validation Pattern
```python
def validate_against_real_data(calculated_value, real_source, tolerance=0.01):
    """Always validate calculations against real measurements"""
    deviation = abs(calculated_value - real_source) / real_source * 100
    if deviation > tolerance:
        print(f"⚠️  Deviation: {deviation:.2f}% from {real_source}")
    return deviation < tolerance
```

### Output Formatting
- Use ANSI color codes from `Colors` class for terminal output
- Include timestamps in ISO format: `datetime.now().isoformat()`
- Save results to `results.txt` for persistence
- Use JSON for structured data exchange

### Error Handling
```python
try:
    # Risky operation
    result = complex_calculation()
except Exception as e:
    print(f"{Colors.FAIL}ERROR: {str(e)}{Colors.ENDC}")
    return None
```

## Integration Points

### External Data Sources
- NASA astronomical data (distances, periods, constants)
- Wikipedia measurements (latitudes, historical data)
- "Antigravity system" real-time data feeds
- Geological records and archaeological measurements

### Cross-Component Communication
- `antigravity_data.json`: Real-time data exchange format
- `event_window_monitoring.json`: Monitoring system state
- `verification_data.json`: Validation results
- All components share `LevhiMahfuzConstants` for consistency

## Key Files to Reference

### Core Logic
- `levhi_mahfuz.py`: All universal constants and formulas
- `simulasyon_11.py`: Main simulation algorithms
- `COLAB_MEGA_ANALYSIS.ipynb`: Comprehensive analysis workflow

### Validation
- `verify_constants.py`: Scientific cross-referencing
- `test_11_dimensional_constants.py`: Unit test patterns
- `ANTIGRAVITY_VALIDATION_REPORT.txt`: Validation results

### Data Processing
- `process_discoveries.py`: Real-time data processing patterns
- `antigravity_bridge.py`: External data integration
- `merge_analysis_report.json`: Analysis results format

## Common Pitfalls to Avoid

- **Don't use decimal approximations**: Prefer exact 11-based calculations
- **Always validate**: Cross-reference all constants with authoritative sources
- **Preserve precision**: Use appropriate significant figures for astronomical data
- **Include timestamps**: All operations should be timestamped for reproducibility
- **Use Turkish comments**: Maintain consistency with existing codebase documentation

## Development Environment

- **Python 3.12+** required
- **Dependencies**: pandas, numpy, scipy, flask
- **Testing**: Run all validation scripts before commits
- **Documentation**: Update README.md and analysis reports for significant changes