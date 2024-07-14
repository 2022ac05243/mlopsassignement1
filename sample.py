# sample.py

# Module docstring explaining the purpose of the module
"""
This module contains functions related to number operations.
"""

# Global variable example
numbers = [1, 2, 3]

def calculate_sum():
    """
    Calculate the sum of numbers.
    """
    # Redefining 'numbers' from the outer scope
    numbers = [4, 5, 6]  # avoid redefining variables if not necessary
    return sum(numbers)

def calculate_product():
    """
    Calculate the product of numbers.
    """
    return numbers[0] * numbers[1] * numbers[2]
