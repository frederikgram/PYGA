""" Collection of parent selection algorithms for Genetic Algorithms"""

from typing import Tuple


def rank_selection(objects: object, fitness_attribute: str) -> Tuple[object]:
    """ Parent Rank Selection Algorithm """

    for obj in objects:
        try:
            score = getattr(obj, fitness_attribute)
        except AttributeError:
            print("Invalid fitness attribute")
            raise

    return tuple()


def roulette_selection(objects: object, fitness_attribute: str) -> Tuple[object]:
    """ Roulette Wheel Parent Selection Algorithm """

    import operator
    import random

    #  Calculate total sum of fitness values
    fitness_sum = sum([getattr(obj, fitness_attribute) for obj in objects])

    #  Find two parents
    parents = tuple()
    for _ in range(2):

        #  Find random point
        point = random.uniform(0, fitness_sum)

        # Find the object which fitness attribute exceeds the variable point
        for obj in sorted(objects.items(), key=getattr(operator.itemgetter(1), fitness_attribute)):
            if point > obj and obj not in parents:
                parents.append(obj)
                break

    return parents


def stochastic_sampling(objects: object, fitness_attribute: str) -> Tuple[object]:
    """ Stochastic Universal Sampling Parent Selection Algorithm """
    pass
