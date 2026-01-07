"""
Calculator Module
A modular calculator that supports various operations.
Each operation can be implemented by different team members.
"""


def multiply(a, b):
    """
    Performs multiplication of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def calculate(operation, a, b):
    """
    Main calculator function that performs operations.
    
    Args:
        operation: String indicating the operation ('multiply', 'add', 'subtract', 'divide')
        a: First number
        b: Second number
    
    Returns:
        Result of the operation
    """
    operations = {
        'multiply': multiply,
        # Other operations to be added by team members
        # 'add': add,
        # 'subtract': subtract,
        # 'divide': divide,
    }
    
    if operation not in operations:
        raise ValueError(f"Operation '{operation}' not supported yet. Available: {list(operations.keys())}")
    
    return operations[operation](a, b)


if __name__ == "__main__":
    # Test multiplication
    print("Calculator - Multiplication Test")
    print(f"5 × 3 = {multiply(5, 3)}")
    print(f"10 × 7 = {multiply(10, 7)}")
    print(f"2.5 × 4 = {multiply(2.5, 4)}")
    
    # Using main calculator function
    print("\nUsing calculate function:")
    print(f"multiply(12, 8) = {calculate('multiply', 12, 8)}")
