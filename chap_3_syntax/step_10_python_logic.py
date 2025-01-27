"""
This module explores the use of logical operators.
"""


def python_logic():

    def conditional_statements():
        """
        Conditionals are compound statements composed of if, elif, and
        else clauses- each made up of a header and a suite.

        You can have as many elif conditionals as you want, sandwiched
        between if and else clauses.
        """

        command = "greet"

        if command == "greet":
            print("Hello!")
        elif command == "quit":
            print("Goodbye!")
        else:
            print("I don't understand")

    def comparison_operators():
        """
        Comparison operators are used to compare two values.
        They return a boolean value- True or False.

        == : Equal
        != : Not Equal
        <  : Less than
        >  : Greater than
        <= : Less than or equal to
        >= : Greater than or equal to
        """

        score = 98
        high_score = 100

        print(score == high_score)  # False
        print(score != high_score)  # True
        print(score < high_score)  # True
        print(score <= high_score)  # True
        print(score > high_score)  # False
        print(score >= high_score)  # False

    def boolean_none_identity_operators():
        """
        Demonstrates the use of boolean, None, and identity operators.
        Boolean operator returns True or False.

        None:
        - Represents the absence of a value

        Identity operators:
        - is: Returns True if both variables are the same object
        - is not: Returns True if both variables are not the same object
        """

        spam = True
        eggs = False
        potatoes = None

        if spam is True:  # evaluates to True
            print("We have spam!")

        if spam is not False:  # evaluates to True
            print("I don't like spam.")

        if spam:  # implictly evaluates to True (preferred)
            print("Spam, spam, spam, spam...")

        if eggs is False:  # evaluates to True
            print("We're all out of eggs!")

        if eggs is not True:  # evaluates to True
            print("No eggs, but we have spam.")

        if not eggs:  # implictly evaluates to True (preferred)
            print("Would you like spam instead.")

        if potatoes is not None:  # evaluates to False
            print("We have potatoes!")

        if potatoes is None:  # evaluates to True
            print("No potatoes, sorry.")

        if eggs is spam:  # evaluates to False
            print("This won't work.")

    def truthiness():
        """
        Most expressions in Python can be evaluated to True or False.

        You can typically do this using the value itself as an expression.
        """

        answer = 42

        if answer:
            print("The answer is", answer)
            print(bool(answer))

    def logical_operators():
        """
        Logical operators are used to combine conditional statements.

        'and': Returns True if both statements are True
        'or': Returns True if one of the statements is True
        'not': Reverse the result, returns False if the result is True
        """

        spam = True
        eggs = False

        if spam and eggs:  # and operator evaluates to False
            print("I do not like green eggs and spam.")
        if spam or eggs:  # or operator evaluates to True
            print("Here's your meal.")
        if (not eggs) and spam:  # not operator evaluates to True
            print("I DO NOT LIKE SPAM!")

            def logical_opps_not():
                """
                We can use the 'not' operator to invert any conditional statement.
                """

                score = 98
                high_score = 100
                print(score != high_score)  # True
                print(not score == high_score)  # True
                # pylint: disable=unnecessary-negation

                # both do the same thing, difference is readability.

            logical_opps_not()

    def walrus_operator():
        """
        The Walrus operator (:=) in Python 3.8 allows you to assign a value
        to a variable and use that variable in another expression at the same time.

        Essentially, the Walrus operator combines the assignment and the comparison
        within the if statement.
        """

        if (eggs := 7 + 5) == 12:
            print("We have one dozen eggs")
            print(eggs)

    # conditional_statements()
    # comparison_operators()
    # boolean_none_identity_operators()
    # truthiness()
    # logical_operators()
    walrus_operator()


python_logic()
