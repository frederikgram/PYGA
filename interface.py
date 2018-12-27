import sys
import argparse

from src.neat import NEAT

if __name__ == "__main__":
    """
    :param features: List
    :param outputs: List
    
    
    :option iterate_evolution: 
    :option max_score:
    :option max_generations:
    
    """

    parser = argparse.ArgumentParser(description='Interface for the NEAT Genetic Algorithm')
    parser.add_argument('n_features')
    parser.add_argument('outputs')

    args = parser.parse_args()

    #  Initialize GA instance
    LOCAL_NEAT = NEAT()

    # Configure NEAT Inputs
    LOCAL_NEAT._num_features = parser.n_features

    # Set Evolutionary Boundaries
    if parser.max_score:
        LOCAL_NEAT.max_score = parser.max_score
    if parser.max_generations:
        LOCAL_NEAT.max_generations = parser.max_generations

    # Evolve
    if parser.iterate_evolution is True:
        for generation in LOCAL_NEAT.evolve():
            print(generation)
    else:
        LOCAL_NEAT.evolve()
        print("Fittest:", str(LOCAL_NEAT.fittest_genome))

    # Label feature weights
    feature_weights = zip(range(parser.n_features), LOCAL_NEAT.fittest_genome.weights)

    # Return the weights
    sys.stdout.write(feature_weights)

