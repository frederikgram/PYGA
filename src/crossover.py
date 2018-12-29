""" Collections of Crossover algorithms"""


def mean_crossover(couple: list) -> list:
    """ Creates a list of mean values from two parent lists"""
    from numpy import mean

    mean_weights = [mean([a, b]) for a, b in zip(*couple)]
    return mean_weights
