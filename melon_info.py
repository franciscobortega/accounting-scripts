"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, melon_flesh_color, melon_rind_color, melon_average_weight


def print_melon(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

    print(f'{name.upper()}\nprice: {price:.2f}\nseedless: {seedless}\nflesh_color: {flesh}\nrind_color: {rind}\naverage_weight: {weight}')


for i in melon_names:
    print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i], melon_flesh_color[i], melon_rind_color[i], melon_average_weight[i])
