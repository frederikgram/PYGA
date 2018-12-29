""" Dynamic GA implemented in Python 3.7 """

import sys
from typing import NoReturn, Generator

from src.classes import Genome, Generation
from src.selection import *
from src.mutation import *
from src.crossover import *


class GA:
    """ TODO """
    def __init__(self, _num_features: int, score_function: callable):
        """
        :param _num_features: Number of input features
        :param score_function: Callable where a list of weights can be input,
                               and a score as a float can be returned
        """

        #  Initialize Class
        self._num_features = _num_features
        self.score_function = score_function
        self.iterate_evolution = False
        self.generation_size = 100
        self.mutation_chance = 7
        self.max_generations = None
        self.max_score = None

        #  Debug and logging
        self.display_info = False

        #  Set standard functions
        self.selection_function = roulette_selection
        self.mutation_function = uniform
        self.crossover_function = mean_crossover

    def configure(self, settings: dict) -> NoReturn:
        """ Mass configure GA using a dictionary
            Example settings can be found in configuration_guide.md
        """

        for key, value in settings.items():
            try:
                setattr(self, key, value)
            except AttributeError:
                print(key, "is not a valid attribute")
                raise
            except TypeError:
                print("type of value for", key, "should be of type", type(getattr(self, key)), '\n',
                      "but has type", type(value))
                raise

    def evolve(self):
        """ Write a docstring lol """

        import random

        #  Initialize Variables
        _num_genomes = int()
        _num_generations = int()

        #  Create Initial Population
        current_generation = Generation(_num_generations + 1, [])

        for _ in range(self.generation_size):
            current_generation.genomes.append(Genome(_num_genomes + 1,
                                                     [random.uniform(0, 1) for _ in range(self._num_features)]))
            _num_genomes += 1
        _num_generations += 1

        while True:
            # Start evolutionary loop

            if self.display_info is True:
                sys.stdout.write(str(current_generation))

            #  Test Genomes
            for genome in current_generation.genomes:
                #  Get genome score
                genome.score = self.score_function(genome.weights)

            #  Selection
            couples = list()
            for _ in range(len(current_generation.genomes)):
                couple = self.selection_function(current_generation.genomes, "score")
                couples.append(couple)

            new_generation = Generation(_num_generations + 1, [])
            _num_generations += 1

            #  Crossover
            for couple in couples:
                child = Genome(_num_genomes +1, self.crossover_function([couple[0].weights, couple[1].weights]))
                new_generation.genomes.append(child)
                _num_genomes += 1

            #  Elitism repopulation
            new_generation.genomes.extend(sorted(current_generation.genomes,
                                                 key=lambda obj: getattr(obj, "score"), reverse=True)
                                          [:self.generation_size - len(new_generation.genomes)])

            #  Mutate
            for genome in new_generation.genomes:
                if random.randint(0, self.mutation_chance) == 0:
                    genome.weights = self.mutation_function(genome.weights)

            #  Find fittest genome in new generation
            fittest_genome = sorted(current_generation.genomes,
                                    key=lambda obj: getattr(obj,
                                                            "score"), reverse=True)[0]

            # Store new generation
            current_generation = new_generation

            #  TODO  Return when score has stagnated
            #  Return logic
            if self.max_score is not None and fittest_genome.score >= self.max_score or \
               self.max_generations is not None and _num_generations >= self.max_generations:
                break
            elif self.iterate_evolution is True:
                yield fittest_genome.weights

        yield fittest_genome.weights
