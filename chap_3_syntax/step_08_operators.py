"""
This module demonstrates the use of operators in Python.
"""


def explore_operators():
    """This function demonstrates the use of operators in Python.
    - Operators are special symbols that represent computations.
    - The most common operators are arithmetic operators.
    """

    def common_operators():
        """
        This function demonstrates common operators in Python.

        - Operators are special symbols that represent
          computations.

        """

        print(-42)  # negative (unary)
        print(abs(-42))  # absolute value
        print(40 + 2)  # addition
        print(44 - 2)  # subtraction
        print(21 * 2)  # multiplication
        print(680 / 16)  # division
        print(680 // 16)  # floor division (no remainder)
        print(1234 % 149)  # modulus (remainder of division)
        print(7**2)  # exponentiation
        print((9 + 5) * 3)  # parentheses for grouping

    def augmented_assignment_operators():
        """
        This function demonstrates augmented assignment
        operators (compound operators).

        - These allow you to perform an operation with the
        current value of the variable as the left operand.
        """

        value = 10
        value += 10
        value -= 5
        value *= 16
        value //= 5
        value /= 4
        value **= 2
        value %= 51

    def explore_divmod():
        """
        This function demonstrates the divmod() function.
        - At the same time, you can divide two numbers and get both the quotient
        - The divmod() function takes two numbers and returns a tuple
        containing the quotient and the remainder.
        """

        a = 680
        b = 16

        quotient, remainder = divmod(a, b)
        print(f"divmod({a}, {b}) = (Quotient: {quotient}, " f"Remainder: {remainder})")

    # Call the sub-functions
    common_operators()
    augmented_assignment_operators()
    explore_divmod()


# Call the main function
explore_operators()
