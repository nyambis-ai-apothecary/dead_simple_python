"""
This module explores the use of strings in Python, including string literals,
string operations, and common string methods.
"""


def python_strings_main():
    """
    Main function to explore the use of strings in Python.
    """
    # Calls for various functions to demonstrate string operations below.

    def string_literals():
        """
        Demonstrates different ways of defining string literals in Python.
        Strings are sequences of characters enclosed in quotes.
        """
        danger = "Cuidado, llamas!"
        danger = "Cuidado, llamas!"
        danger = """Cuidado, llamas!"""
        danger = """Cuidado, llamas!"""
        print(danger)

    def escaping_quotes():
        """
        We explore how to handle quotes within strings.
        """
        # If your string contains a single quote, use double quotes to define it
        quote1 = "Shout 'Cuidado, llamas!'"
        print(quote1)

        # Vis versa, if double, use single quotes
        quote2 = 'Shout "Cuidado, llamas!"'
        print(quote2)

        # Using backslashes to escape quotes
        quote3 = 'Shout "Cuidado, llamas!"'
        print(quote3)

    def multiline_string_literals():
        """
        Demonstrates how to define multiline strings in Python.
        """
        # Using triple quotes to define multiline strings
        poem = """Roses are red,
        Violets are blue,
        Python is fun,
        And so are you!"""
        print(poem)

        # Using parentheses to define multiline strings
        poem = ("Roses are red,\n"
                "Violets are blue,\n"
                "Python is fun,\n"
                "And so are you!")
        print(poem)

    def raw_strings():
        """
        Raw string literals are used to avoid escaping backslashes.

        They are particulary useful when working with 
        regular expressions.

        The backslash is treated like a literal character,
        which means nothing is escaped.
        """
        print(r"I love backslashes: \ Aren't they cool?")

        # Compre the two lines below and their output

        print("A\nB") #ordinary string, \n is normal escape sequence
        print(r"A\nB") #raw string, \n a literal character

    def formatted_strings():
        """
        Formatted strings, or f-strings, allow you to insert the values of variables into a string in a very elegant way
        """
        # Without f-strings
        in_stock = 0
        print("This cheese shop has " + str(in_stock) + " types of cheese available.")

        # With f-strings
        in_stock = 0
        print(f"This cheese shop has {in_stock} types of cheese available.")

        # You can display both the expression and its result by appending a trailing equal sign (=)

        print(f"{5+5=}") # prints '5+5=10'

        # If you want to wrap an expression in literal curly braces, use two braces for every one you want to display.

        answer = 42
        print(f"{{{answer}}}")
        print(f"{{{{{answer}}}}}")
        print(f"{{{{{{answer}}}}}}")

    def format_specifications():
        """
        F-strings support format specifications, which allow you to control how the value is displayed.

        Immediately after the expression, you can add a colon (:) followed by a format specification.
        """
        def format_specs_alignment():
            """
            Alignment can be specified using the following format specifications:
            """
            text = "Hello"
            number = 42

            # Left alignment
            print(f"{text:<10}")  # 'Hello     '
            print(f"{number:<10}")  # '42        '

            # Right alignment
            print(f"{text:>10}")  # '     Hello'
            print(f"{number:>10}")  # '        42'

            # Center alignment
            print(f"{text:^10}")  # '  Hello   '
            print(f"{number:^10}")  # '    42    '

            # Using a fill character
            print(f"{text:*^10}")  # '**Hello***'
            print(f"{number:0>10}")  # '0000000042'
        def format_specs_sign_flags():
            """
            Sign flags control when the sign should be displayed on numbers.
            """

            positive_number = 42
            negative_number = -42

            # Plus (+) flag: displays the sign on both positive and negative numbers
            print(f"{positive_number:+}")  # '+42'
            print(f"{negative_number:+}")  # '-42'

            # Minus (-) flag: displays the sign only on negative numbers (default behavior)
            print(f"{positive_number:-}")  # '42'
            print(f"{negative_number:-}")  # '-42'

            # Space ( ) flag: shows a leading space on positive numbers and a sign on negative numbers
            print(f"{positive_number: }")  # ' 42'
            print(f"{negative_number: }")  # '-42'
        def format_specs_alternative_form():
            """
            The has (#) symbol turns on the alternative form for integers, floats, and complex numbers.

            Ex. Hexadecimal, octal, and binary numbers are prefixed with '0x', '0o', and '0b', respectively.
            """

            number = 42

            # Alternative form for hexadecimal
            print(f"{number:#x}")  # '0x2a'
            print(f"{number:#X}")  # '0X2A'

            # Alternative form for octal
            print(f"{number:#o}")  # '0o52'

            # Alternative form for binary
            print(f"{number:#b}")  # '0b101010'
        def format_specs_leading_zeros():
            """
            Leading zeros can be added to numbers for padding.
            """
            number = 42

            # Pad with zeros to a width of 5
            print(f"{number:05}")  # '00042'

            # Pad with zeros to a width of 10
            print(f"{number:010}")  # '0000000042'




        # Call sub-functions to demonstrate format specifications
        format_specs_alignment()
        format_specs_sign_flags()
        format_specs_alternative_form()
        format_specs_leading_zeros()

    # Call the functions to demonstrate string operations
    string_literals()
    escaping_quotes()
    multiline_string_literals()
    raw_strings()
    formatted_strings()
    format_specifications()

if __name__ == "__main__":
    python_strings_main()
