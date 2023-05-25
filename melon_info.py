"""Print out all the melons in our inventory."""


from melons import melons
import textwrap


def print_melon(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

    # formatted information is assigned to variable
    attribute_information = f"""
    {name.upper()}
    price: {price:.2f}
    seedless: {seedless}
    flesh_color: {flesh}
    rind_color: {rind}
    average_weight: {weight}"""

    # formatted information is printed and indentation from triple string is removed
    print(textwrap.dedent(attribute_information))


for melon in melons:
    # destructuring value for each melon dictionary in melons list
    name, price, seedlessness, flesh_color, rind_color, average_weight = melon.values()

    # passing in values to print_melon function
    print_melon(name, price, seedlessness, flesh_color, rind_color, average_weight)
