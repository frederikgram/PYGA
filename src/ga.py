""" Dynamic GA implemented in Python 3.7 """

import sys
from typing import NoReturn

from src.classes import Genome, Generation
from src.selection import *
from src.mutation import *
from src.crossover import *


class GA:
    """ TODO """

    def __init__(self, _num_weights: int, fitness_function: callable):
        """
        :param _num_weights: Number of weights to evolve
        :param fitness_function: Callable where a list of weights can be input,
                               and a fitness as a float can be returned
        """

        #  Initialize Class
        self._num_weights = _num_weights
        self.fitness_function = fitness_function
        self.iterate_evolution = False
        self.generation_size = 100
        self.mutation_chance = 7
        self.max_generations = None
        self.max_fitness = None

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
                print(
                    "type of value for",
                    key,
                    "should be of type",
                    type(getattr(self, key)),
                    "\nbut has type",
                    type(value),
                )
                raise

    def evolve(self):
        """ Write a docstring lol """

        import random

        #  Initialize Variables
        _num_genomes = int()
        _num_generations = int()

        #  Create Initial Population
        current_generation = Generation(_num_generations + 1, [])

        #  Assign random weights to each genome
        for _ in range(self.generation_size):
            current_generation.genomes.append(
                Genome(
                    _num_genomes + 1,
                    [random.uniform(0, 1) for _ in range(self._num_weights)],
                )
            )
            _num_genomes += 1
        _num_generations += 1

        while True:
            # Start evolutionary loop

            #  Test Genomes
            for genome in current_generation.genomes:
                #  Get genome fitness
                genome.fitness = self.fitness_function(genome.weights)

            if self.display_info is True:
                sys.stdout.write(str(current_generation))

            #  Selection
            couples = list()
            for _ in range(len(current_generation.genomes)):
                couple = self.selection_function(current_generation.genomes, "fitness")
                couples.append(couple)

            new_generation = Generation(_num_generations + 1, [])
            _num_generations += 1

            #  Crossover
            for couple in couples:
                child = Genome(
                    _num_genomes + 1,
                    self.crossover_function([couple[0].weights, couple[1].weights]),
                )
                new_generation.genomes.append(child)
                _num_genomes += 1

            #  Elitist repopulation
            new_generation.genomes.extend(
                sorted(
                    current_generation.genomes,
                    key=lambda obj: getattr(obj, "fitness"),
                    reverse=True,
                )[: self.generation_size - len(new_generation.genomes)]
            )

            #  Mutate
            for genome in new_generation.genomes:
                if random.randint(0, self.mutation_chance) == 0:
                    genome.weights = self.mutation_function(genome.weights)

            #  Find fittest genome in new generation
            fittest_genome = sorted(
                current_generation.genomes,
                key=lambda obj: getattr(obj, "fitness"),
                reverse=True,
            )[0]

            # Store new generation
            current_generation = new_generation

            #  Return logic
            if (
                self.max_fitness is not None
                and fittest_genome.fitness >= self.max_fitness
                or self.max_generations is not None
                and _num_generations >= self.max_generations
            ):
                break
            elif self.iterate_evolution is True:
                yield fittest_genome.weights
        yield fittest_genome.weights
