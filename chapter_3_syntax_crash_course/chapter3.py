"""
This module serves as a reference and
playground for exploring and practicing
different Python syntax features.
"""


def print_hello_world():
    """Print the classic 'Hello, world!' message."""
    print("Hello, world!")


def get_input():
    """Get input from the console and greet the user."""
    name = input("What is your name? ")
    print("Hello, " + name)


def statements_and_expressions():
    """
    Demonstrate statements and expressions in Python.

    - Each line of code in Python that ends with a line break is a statement.
    - An expression is a section of code that evaluates to a single value.
    - Assign the expression "Hello, world!" to message and then pass
    the expression message to print().
    """
    message = "Hello, world"
    print(message)


def importance_whitespace():
    """
    Demonstrate the importance of whitespace in Python.

    A compound statement is made up of two or more clauses, each of which:
    - starts with a header
    - and a block of code called a suite.

    The program below prints different messages, depending on whether a name is provided.
    """
    name = "Jason"
    if name != "":  # if header
        message = "Hello, " + name + "!"  # suite line 1
        print(message)  # suite line 2
    print("I am a computer")


def pass_placeholder():
    """
    The pass statement is a null operation that does nothing.
    "Doing Nothing": It is used as a placeholder when a statement is required syntactically
    but you do not want to execute any code.
    """

    nyambi = True
    if nyambi:
        pass


def comments_and_docstrings():
    """
    Demonstrate comments and docstrings in Python.

    - To write comments in Python, use the hash symbol (#).
    - Docstrings are used to document modules, classes, functions,
    and methods. You would typically place docstrings at the top, inside whatever they are defining.
    """
    # This is a comment
    print("Hello, world!")
    print("How are you?")  # This is an inline comment

    def make_tea():
        """Will produce a concoction almost, but not entirely unlike tea."""
        # ...function logic...

    make_tea()


def defining_variables():
    """
    Demonstrate defining variables in Python.

    - Python is a dynamically typed language, meaning you do 
    not need to specify the type of a variable.
    """
    name = "Jason"
    points = 4571
    print(name) # displays Jason
    print(points) # displays 4571
    points = 42
    print(points) # displays 42

def constants_in_python():
    """
    Demonstrate constants in Python.

    - Constants are variables whose values should not be changed 
    once they are set.
    - Python does not have built-in support for constants.
    - However, you can use all uppercase letters to indicate a variable is a constant.
    """
    PI = 3.14159 #pylint: disable=invalid-name
    print(PI) # displays 3.14159
    # PI = 3.14 # This will throw an error

def explore_integers():
    """
    This function demonstrates the use of integers
    in Python.

    Integers are whole numbers (no decimals) and can be positive or negative. 
    They can be very large without any size limits.

    We'll explore different ways to represent integers:
    - Decimal (base-10): The usual way we write numbers
    (e.g., 10, -5)

    - Binary (base-2):  Using '0b' followed by 0s and
    1s (e.g., 0b1010).

    - Octal (base-8): Using '0o' followed by digits
    0-7 (e.g., 0o12).

    - Hexadecimal (base-16): Using '0x' followed by
    digits 0-9 and A-F (e.g., 0xA)
  """

    number = 42
    print(f"Integer: {number}") # displays 42

def explore_floats():
    """
    This function demonstrates the use of floating-point numbers (floats).

    - Floats store numbers with a decimal part (3.141592).
    - You can also use scientific notation (2.49e4).
    - Internally, values are stored as double-precision, IEEE 754 
    floating-point numbers, which are subject to the limits inherent
    in that format.
    """

    # Examples of floating-point numbers
    pi = 3.141592
    radius = 5.0

    # Calculating the area of a circle using floating-point numbers
    area = pi * radius ** 2

    # Printing the result with 2 decimal places
    print(f"The area of the circle is {area:.2f}")


if __name__ == "__main__":
    # print_hello_world()
    # get_input()
    # statements_and_expressions()
    # importance_whitespace()
    # pass_placeholder()
    # comments_and_docstrings()
    # defining_variables()
    # constants_in_python()
    # explore_integers()
    explore_floats()
