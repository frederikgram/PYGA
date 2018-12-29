""" Collection of mutation algorithms for Genetic Algorithms """


def random_swap(weights: list) -> list:
    """ Randomly swaps two values in a list """
    import random

    index = range(len(weights))

    #  Randomly chose indexes to swap
    index_1, index_2 = random.sample(index, 2)

    #  Swap values
    weights[index_1], weights[index_2] = weights[index_2], weights[index_1]

    return weights


def uniform(weights: list) -> list:
    """ Sets an entry of a given list to a random float in between 0 and 1 """
    import random

    index = random.randint(0, len(weights) - 1)
    weights[index] = random.uniform(0, 1)

    return weights
