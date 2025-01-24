"""
In this module, we explore variables and constants.
"""


def defining_variables():
    """
    Demonstrate defining variables in Python.

    - Python is a dynamically typed language, meaning you do
    not need to specify the type of a variable.
    """

    def demonstrate_variable_assignment():
        name = "Jason"
        points = 4571
        print(name)  # displays Jason
        print(points)  # displays 4571
        points = 42
        print(points)  # displays 42

    # Think Tank: On 'updating' varables by converting data types
    def demonstrate_type_change():
        """
        This function demonstrates updating variable data types.

        - There are two general rules for variables in Python:
          1. Define a variable before using it.
          2. Do not change the data type of a variable after defining it.

        - But you can update the value of a variable to a different data type.
        """

        value = 10  # value is an integer
        print(f"value is {value} and its type is {type(value)}")

        value = float(value)  # value is now a float
        print(f"value is {value} and its type is {type(value)}")

        value = str(value)  # value is now a string
        print(f"value is {value} and its type is {type(value)}")

    # Call the functions
    demonstrate_variable_assignment()
    demonstrate_type_change()


def constants_in_python():
    """
    Demonstrate constants in Python.

    - Constants are variables whose values should not be changed
    once they are set.
    - Python does not have built-in support for constants.
    - However, you can use all uppercase letters to indicate a variable is a constant.
    """
    PI = 3.14159  # pylint: disable=invalid-name
    print(PI)  # displays 3.14159
    # PI = 3.14 # This will throw an error

    constants_in_python()


# Call the main function
defining_variables()
