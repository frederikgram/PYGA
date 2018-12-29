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


def roulette_selection(objects: list, fitness_attribute: str) -> list:
    """ Roulette Wheel Parent Selection Algorithm """

    import random

    #  Calculate total sum of fitness values
    fitness_sum = sum([getattr(obj, fitness_attribute) for obj in objects])
    objects = sorted(objects, key=lambda obj: getattr(obj, fitness_attribute), reverse=True)

    #  Find two parents
    parents = list()
    while len(parents) < 2:

        #  Find random point
        point = random.uniform(0, fitness_sum)

        # Find the object which fitness attribute exceeds the variable point
        for obj in objects:
            if point < getattr(obj, fitness_attribute) and obj not in parents:
                parents.append(obj)
                break

    return parents


def stochastic_sampling(objects: object, fitness_attribute: str) -> Tuple[object]:
    """ Stochastic Universal Sampling Parent Selection Algorithm """
    pass
