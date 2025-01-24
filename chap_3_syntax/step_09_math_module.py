"""
This module demonstrates the use of the math module.
"""

import math


def the_math_module():
    """
    Demonstrate the use of the math module.

    - The math module provides mathematical functions and constants.
    """

    def math_mod_math_pi():
        """
        Use math.pi to calculate the area of a circle.
        """
        radius = 5
        area = math.pi * radius**2
        print(f"The area of the circle is {area:.2f}")

    def math_mod_eulers_number():
        """
        Demonstrate the use of Euler's number (math.e).

        - Euler's number is used for advanced math like exponential growth and decay.
        - We can use math.e to solve a simple compound interest problem.
        """
        principal = 1000
        rate = 0.05
        time = 10
        amount = principal * math.e ** (rate * time)
        print(f"The amount after {time} years is {amount:.2f}")

    def math_mod_infinity():
        """
        Demonstrate the use of infinity (math.inf).

        - Use math.inf to handle extreme values.
        - Find the smallest number in a list by starting with infinity.
        """
        numbers = [10, 5, 20, 15]
        smallest = math.inf  # Start with infinity

        for number in numbers:
            smallest = min(smallest, number)
        print(f"The smallest number is {smallest}")

    def math_mod_nan():
        """
        Demonstrate the use of NaN (math.nan).

        - math.nan represents an undefined or unrepresentable value.
        - Use it for error handling in calculations.
        """

        def divide(x, y):
            if y == 0:
                return math.nan  # Return NaN if division by zero
            return x / y

        result = divide(10, 0)
        if math.isnan(result):
            print("Error: Cannot divide by zero")
        else:
            print(f"The result is: {result}")

    def math_mod_tau():
        """
        Demonstrate the use of tau (math.tau).

        - math.tau is a mathematical constant equal to 2 * pi.
        - It represents the ratio of a circle's circumference to its radius.
        """
        radius = 5
        area = math.pi * radius**2
        circumference = math.tau * radius

        print(f"Area: {area:.2f}")
        print(f"Circumference: {circumference:.2f}")

    # Call the sub-functions
    math_mod_math_pi()
    math_mod_eulers_number()
    math_mod_infinity()
    math_mod_nan()
    math_mod_tau()


# Call the main functin
the_math_module()
