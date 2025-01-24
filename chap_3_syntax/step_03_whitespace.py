"""
In this module, we explore the importance of whitespace in Python.
"""


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


# Call the function
importance_whitespace()
