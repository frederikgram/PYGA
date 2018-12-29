""" Interface to use weights to control a paddle in pong"""

from src.ga import GA
from .pong import play

BEST_OF_THREE_CONFIGURATION = {
                        "generation_size": 1000,
                        "selection_function": "roulette_selection",
                        "mutation_function": "uniform",
                        "iterate_evolution": False,
                        "max_score": 3,
                        }

LOCAL_GA = GA(4, play)
LOCAL_GA.configure(BEST_OF_THREE_CONFIGURATION)

best_weight = GA.evolve()
