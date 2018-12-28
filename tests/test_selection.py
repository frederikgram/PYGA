""" Test if selection algorithms from selection.py function properly """

from src.selection import rank_selection, stochastic_sampling, roulette_selection


class TestObject:

    def __init__(self, id, score):
        self.id = id
        self.score = score


if __name__ == "__main__":
    """ Run Test"""

    #  Create testing pool
    test_objects = list()

    for i in range(100):
        test_objects.append(TestObject(i, i))

    # Roulette selection
    parents = roulette_selection(test_objects, "score")

    assert parents is not None
    assert len(parents) == 2
    assert isinstance(parents, tuple)
