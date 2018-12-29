""" Collections of Crossover algorithms"""


def average_crossover(couple: list) -> list:
    """ Creates a list of average values from two parent lists"""
    from numpy import mean

    average_weights = [mean([a, b]) for a, b in zip(*couple)]
    return average_weights
