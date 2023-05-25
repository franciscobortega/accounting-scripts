"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

    print(f'{name.upper()}\nprice: {price:.2f}\nseedless: {seedless}\nflesh_color: {flesh}\nrind_color: {rind}\naverage_weight: {weight}')


for melon in melons:
    # destructuring value for each melon dictionary in melons list
    name, price, seedlessness, flesh_color, rind_color, average_weight = melon.values()

    # passing in values to print_melon function
    print_melon(name, price, seedlessness, flesh_color, rind_color, average_weight)
