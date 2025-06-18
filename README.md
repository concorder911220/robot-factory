# Robotic Package Sorting System

## Overview

This project implements a package sorting system for Thoughtful's robotic automation factory. The system classifies packages based on their dimensions and mass to dispatch them to the appropriate handling stacks.

## Problem Description

The robotic arm needs to sort packages into three different stacks based on whether they are bulky, heavy, or both:

- **STANDARD**: Packages that are neither bulky nor heavy
- **SPECIAL**: Packages that are either bulky OR heavy (but not both)
- **REJECTED**: Packages that are both bulky AND heavy

## Classification Rules

### Bulky Packages
A package is considered **bulky** if either:
- Its volume (Width × Height × Length) is ≥ 1,000,000 cm³
- Any of its dimensions (width, height, or length) is ≥ 150 cm

### Heavy Packages
A package is considered **heavy** if:
- Its mass is ≥ 20 kg

## Usage

### Function Signature
```python
sort(width, height, length, mass) -> str
```

### Parameters
- `width` (float): Width of the package in centimeters
- `height` (float): Height of the package in centimeters  
- `length` (float): Length of the package in centimeters
- `mass` (float): Mass of the package in kilograms

### Return Value
Returns a string indicating the destination stack:
- `"STANDARD"`: For packages that are neither bulky nor heavy
- `"SPECIAL"`: For packages that are either bulky or heavy (but not both)
- `"REJECTED"`: For packages that are both bulky and heavy

### Example Usage
```python
from package_sorter import sort

# Standard package (small and light)
result = sort(10, 10, 10, 5)  # Returns "STANDARD"

# Special package (bulky by dimension)
result = sort(150, 10, 10, 15)  # Returns "SPECIAL"

# Special package (heavy but not bulky)
result = sort(50, 50, 50, 25)  # Returns "SPECIAL"

# Rejected package (both bulky and heavy)
result = sort(150, 10, 10, 25)  # Returns "REJECTED"
```

## Running the Code

### Prerequisites
- Python 3.6 or higher

### Running the Main Function
```bash
python -c "from package_sorter import sort; print(sort(100, 100, 100, 20))"
```

### Running Tests
Execute the comprehensive test suite:
```bash
python test_package_sorter.py
```

Or using unittest module:
```bash
python -m unittest test_package_sorter.py
```

## Test Coverage

The test suite covers:
- **Standard packages**: Various combinations of non-bulky, non-heavy packages
- **Special packages**: 
  - Heavy but not bulky packages
  - Bulky but not heavy packages (both by volume and dimension)
- **Rejected packages**: Packages that are both heavy and bulky
- **Edge cases**: Exact threshold values, floating-point inputs
- **Boundary conditions**: Zero values and threshold boundaries

### Test Categories
1. `test_standard_packages()` - Normal handling packages
2. `test_special_packages_heavy_only()` - Heavy but not bulky
3. `test_special_packages_bulky_only()` - Bulky but not heavy
4. `test_rejected_packages()` - Both heavy and bulky
5. `test_edge_cases()` - Exact threshold values
6. `test_floating_point_dimensions()` - Decimal inputs
7. `test_zero_and_negative_values()` - Edge cases with zero values

## Implementation Details

The solution uses nested ternary operators as specified in the requirements:
```python
return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD")
```

This approach ensures:
- Correct precedence of rejection over special handling
- Efficient evaluation using short-circuit logic
- Clean, readable code structure

## Files Structure

```
robot-factory/
├── package_sorter.py      # Main sorting function
├── test_package_sorter.py # Comprehensive test suite
└── README.md             # This documentation
```

## Quality Assurance

The implementation emphasizes:
- **Correctness**: All sorting logic follows the specified rules exactly
- **Robustness**: Handles edge cases and floating-point inputs
- **Testability**: Comprehensive test coverage for all scenarios
- **Maintainability**: Clean, well-documented code with clear logic flow 