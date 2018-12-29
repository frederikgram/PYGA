""" Complete test for the PYGA framework"""

from src.ga import GA
import numpy as np

TEST_CONFIGURATION = {"generation_size": 100,
                      "selection_function": "roulette",
                      "mutation_function": "uniform",
                      "iterate_evolution": False,
                      "max_score": 10,
                      }


def give_score(weights) -> float:
    """ Higher weights give higher scores """
    return np.mean(weights)


LOCAL_NEAT = GA(_num_features=5, score_function=give_score)
LOCAL_NEAT.configure(TEST_CONFIGURATION)


for new_weight in LOCAL_NEAT.evolve():
        print(new_weight)
