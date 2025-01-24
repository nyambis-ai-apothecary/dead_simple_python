"""
Explore different number types in Python.
"""


def explore_integers():
    """
    Demonstrate the use of integers in Python.

    - Integers are whole numbers (no decimals) and can be positive
    or negative.

    - They can be very large without any size limits.

    - Representations: Decimal (base-10), Binary (base-2),
    Octal (base-8), Hexadecimal (base-16).

    """
    decimal_number = 10
    binary_number = 0b1010
    octal_number = 0o12
    hexadecimal_number = 0xA

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_number}")
    print(f"Octal: {octal_number}")
    print(f"Hexadecimal: {hexadecimal_number}")


def explore_floats():
    """
    Demonstrate the use of floating-point numbers (floats).

    - Floats store numbers with a decimal part.
    - Scientific notation is also supported.
    - Values are stored as double-precision, IEEE 754 floating-point numbers.
    """
    pi = 3.141592
    radius = 5.0

    # Calculate the area of a circle
    area = pi * radius**2

    # Print the result with 2 decimal places
    print(f"The area of the circle is {area:.2f}")


# Call the functions
explore_integers()
explore_floats()
