""" Dynamic NEAT GA implemented in Python 3.7 - 27/12/2018 """

import sys
import operator

from typing import NoReturn, List, Tuple
from src.classes import Genome, Generation

from src.selection import roulette_selection
from src.mutation import *


class NEAT:
    """ TODO """
    def __init__(self,
                 _num_features: int,
                 iterate_evolution: bool = False,
                 generation_size: int = 100,
                 max_score: bool = None,
                 max_generations: bool = None):

        """
        :param _num_features: Number of input features
        :param iterate_evolution: True -> Yield every genome of every generation
                                  False -> Return only the best Genome from the final generation
        :param generation_size: How many genomes in each generation DEFAULT=100
        :param max_generations: An upper boundary for the needed generations to stop evolution
        :param max_score: An upper boundary for the needed score to stop evolution
        """

        #  Initialize Class
        self._num_features = _num_features
        self.iterate_evolution = iterate_evolution
        self.generation_size = generation_size

        self.max_generations = max_generations
        self.max_score = max_score

        self.fittest_genome = None

        #  TODO  Get algorithm choices from config
        self.ps_func = roulette_selection
        self.mutate_func = uniform

    def evolve(self) -> NoReturn or Genome:
        """
        :return: if iterate is True -> Yield every genome of every generation
                 if iterate is False -> Return only the best Genome from the final generation
        """

        import random

        #  Initialize Variables
        current_generation = None

        _num_genomes = int()
        _num_generations = int()

        #  Create Initial Population
        new_generation = Generation(_num_generations + 1, [])

        for _ in range(self.generation_size):
            new_generation.genomes.append(Genome(_num_genomes,
                                                 [random.uniform(0, 1) for _ in range(self._num_features)]))
            _num_genomes += 1
        _num_generations += 1

        while True:

            #  Test Genomes
            for genome in new_generation.genomes:

                #  Push genome to stdout
                sys.stdout.write(genome)

                #  Get genome score
                with open(sys.stdin) as stdin:
                    try:
                        genome.score = int(stdin.readlines()[0]) or None
                    except EOFError:
                        print("no score received")
                        raise
                    except TypeError:
                        print("Score input is of non-integer type")
                        raise

            #  Selection


            #  Reproduce
            for couple in parents:
                child = Genome(_num_genomes + 1, self.reproduce_func(couple))

                new_generation.genomes.append(child)
                _num_genomes += 1

            #  Mutate
            new_generation.genomes = map(self.mutate_func, new_generation.genomes)

            #  Find fittest genome in new generation
            fittest_genome = sorted(new_generation.genomes.items(),
                                    key=operator.itemgetter(1), reverse=True)[0]

            #  TODO  Return when score has stagnated
            #  Return logic
            if fittest_genome.score >= self.max_score or \
                    _num_generations >= self.max_generations:
                break

            if self.iterate_evolution:
                yield str(current_generation)

            #  Age population
            current_generation = new_generation

        self.fittest_genome = fittest_genome
        print(str(fittest_genome), fittest_genome.weights, sep='\,')
        exit("OK - Completed")
