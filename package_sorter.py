def sort(width, height, length, mass):
    """
    Sort packages based on their dimensions and mass.
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
    
    Returns:
        str: The stack where the package should go ('STANDARD', 'SPECIAL', or 'REJECTED')
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if package is bulky
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    
    # Check if package is heavy
    is_heavy = mass >= 20
    
    # Use ternary operator to determine the result as required
    return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD") 