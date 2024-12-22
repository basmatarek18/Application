# 1. Module Docstring

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


# 2. Class-Level Docstring

class Calculator:
    """
    A simple calculator class for basic arithmetic operations.

    Methods:
        add(a, b): Returns the sum of two numbers.
        subtract(a, b): Returns the difference between two numbers.
    """
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers and return the result."""
        return a - b
    
    
# 3. Function or Method-Level Docstring

def divide(a, b):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b


