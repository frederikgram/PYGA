""" Collection of mutation algorithms for Genetic Algorithms """

from typing import List


def random_swap(weights: list) -> list:
    """ Randomly swaps two values in a list """
    import random

    index = range(len(weights))

    #  Randomly chose indexes to swap
    index_1, index_2 = random.sample(index, 2)

    #  Swap values
    weights[index_1], weights[index_2] = weights[index_2], weights[index_1]

    return weights

