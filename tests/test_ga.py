""" Overall test for the PYGA framework"""

from src.ga import GA
import numpy as np

TEST_CONFIGURATION = {
    "generation_size": 100,
    "iterate_evolution": True,
    "max_fitness": 0.99,
    "display_info": False,
}


def give_score(weights) -> float:
    """ Higher weights give higher fitness """
    return np.mean(weights)


LOCAL_GA = GA(_num_weights=5, fitness_function=give_score)
LOCAL_GA.configure(TEST_CONFIGURATION)

for iteration in LOCAL_GA.evolve():
    mean_value = np.mean(iteration)
    print("Average fitness this generation:", mean_value)

assert mean_value >= 0.99

""" 
had iterate_evolution been set to false,
    instead of looping through LOCAL_GA.eolve()
    we would've simple said
    
    fittest_weights = LOCAL_GA.evolve()
"""
