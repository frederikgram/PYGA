from typing import List, Tuple
from src.GA import NEAT
import argparse

if __name__ == "__main__":
    """
    
    :param features: List
    :param outputs: List
    
    
    :option iterate_evolution: 
    :option max_score:
    :option max_generations:
    
    """

    parser = argparse.ArgumentParser(description='Interface for the NEAT Genetic Algorithm')
    parser.add_argument('features')
    parser.add_argument('outputs')

    args = parser.parse_args()

    #  Initialize GA instance
    LOCAL_NEAT = NEAT()

    # Configure NEAT Inputs
    LOCAL_NEAT.features = parser.features
    LOCAL_NEAT.outputs = parser.outputs

    # Set Evolutionary Boundaries
    if parser.max_score:
        LOCAL_NEAT.max_score = parser.max_score
    if parser.max_generations:
        LOCAL_NEAT.max_generations = parser.max_generations

    # Evolve
    if parser.iterate_evolution is True:
        for generation in LOCAL_NEAT:
            print(generation, sep=",", end="\n: ")
    else:
        result = LOCAL_NEAT.fast_evolve()
        print(result)
