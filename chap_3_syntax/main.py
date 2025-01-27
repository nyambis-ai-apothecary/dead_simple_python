"""
This is the main entry point for the program. 

It imports and calls functions from various modules
to demonstrate different Python concepts.
"""

from step_01_hello import print_hello_world, get_input
from step_02_statements_expressions import statements_expressions
from step_03_whitespace import importance_whitespace
from step_04_pass_placeholder import pass_placeholder
from step_05_comments_docstrings import comments_docstrings
from step_06_variables_constants import defining_variables, constants_in_python
from step_07_number_types import explore_integers, explore_floats
from step_08_operators import explore_operators
from step_09_math_module import the_math_module
from step_10_logic import conditional_statements, comparison_operators


def main():
    """Main function to call all the demonstration functions."""
    print_hello_world()
    get_input()
    statements_expressions()
    importance_whitespace()
    defining_variables()
    constants_in_python()
    explore_integers()
    explore_floats()
    explore_operators()
    the_math_module()
    pass_placeholder()
    comments_docstrings()
    conditional_statements()
    comparison_operators()


if __name__ == "__main__":
    main()
