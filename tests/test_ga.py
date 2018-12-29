""" Overall test for the PYGA framework"""

from src.ga import GA
import numpy as np

TEST_CONFIGURATION = {
    "generation_size": 100,
    "iterate_evolution": True,
    "max_score": 0.995,
    "display_info": False,
}


def give_score(weights) -> float:
    """ Higher weights give higher scores """
    return np.mean(weights)


LOCAL_GA = GA(_num_features=5, score_function=give_score)
LOCAL_GA.configure(TEST_CONFIGURATION)

for iteration in LOCAL_GA.evolve():
    print("Average score this generation:", np.mean(iteration))
