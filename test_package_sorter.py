import unittest
from package_sorter import sort


class TestPackageSorter(unittest.TestCase):
    """Test cases for the package sorting function."""
    
    def test_standard_packages(self):
        """Test packages that should go to STANDARD stack."""
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
        
        # Medium package, not bulky, not heavy
        self.assertEqual(sort(50, 50, 50, 15), "STANDARD")
        
        # Just under the bulky thresholds
        self.assertEqual(sort(149, 149, 45, 19), "STANDARD")  # Max dimension < 150
        self.assertEqual(sort(99, 99, 101, 19), "STANDARD")   # Volume < 1,000,000
    
    def test_special_packages_heavy_only(self):
        """Test packages that are heavy but not bulky."""
        # Heavy but small
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")
        
        # Heavy but medium size
        self.assertEqual(sort(50, 50, 50, 30), "SPECIAL")
    
    def test_special_packages_bulky_only(self):
        """Test packages that are bulky but not heavy."""
        # Bulky by dimension, not heavy
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")
        self.assertEqual(sort(10, 150, 10, 15), "SPECIAL")
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")
        self.assertEqual(sort(200, 50, 30, 19), "SPECIAL")
        
        # Bulky by volume, not heavy
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")  # Volume = 1,000,000
        self.assertEqual(sort(110, 95, 96, 15), "SPECIAL")    # Volume > 1,000,000
    
    def test_rejected_packages(self):
        """Test packages that should be REJECTED (both heavy and bulky)."""
        # Heavy and bulky by dimension
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 150, 10, 25), "REJECTED")
        self.assertEqual(sort(10, 10, 150, 30), "REJECTED")
        self.assertEqual(sort(200, 50, 30, 40), "REJECTED")
        
        # Heavy and bulky by volume
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # Volume = 1,000,000, mass = 20
        self.assertEqual(sort(110, 95, 96, 25), "REJECTED")    # Volume > 1,000,000, mass > 20
        
        # Heavy and bulky by both criteria
        self.assertEqual(sort(150, 100, 100, 50), "REJECTED")
    
    def test_edge_cases(self):
        """Test edge cases at the exact thresholds."""
        # Exact mass threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")     # Exactly 20kg
        self.assertEqual(sort(10, 10, 10, 19.999), "STANDARD") # Just under 20kg
        
        # Exact dimension threshold
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")    # Exactly 150cm
        self.assertEqual(sort(149.999, 10, 10, 10), "STANDARD") # Just under 150cm
        
        # Exact volume threshold
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # Exactly 1,000,000 cm³
        self.assertEqual(sort(99.999, 100, 100, 10), "STANDARD") # Just under 1,000,000 cm³
        
        # Both thresholds exactly
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")   # Exactly bulky and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED") # Exactly bulky by volume and heavy
    
    def test_floating_point_dimensions(self):
        """Test with floating point dimensions."""
        self.assertEqual(sort(10.5, 10.5, 10.5, 5.5), "STANDARD")
        self.assertEqual(sort(150.1, 10.5, 10.5, 19.9), "SPECIAL")
        self.assertEqual(sort(150.1, 10.5, 10.5, 20.1), "REJECTED")
    
    def test_zero_and_negative_values(self):
        """Test edge cases with zero and negative values (if applicable)."""
        # Zero dimensions should be STANDARD (not bulky)
        self.assertEqual(sort(0, 0, 0, 5), "STANDARD")
        
        # Zero mass should be STANDARD (not heavy)
        self.assertEqual(sort(10, 10, 10, 0), "STANDARD")
        
        # Large dimension with zero mass
        self.assertEqual(sort(150, 10, 10, 0), "SPECIAL")
        
        # Small dimension with large mass
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")


if __name__ == "__main__":
    unittest.main() 