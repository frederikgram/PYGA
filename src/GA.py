""" Dynamic NEAT GA implemented in Python 3.7 - 27/12/2018 """

import sys
import operator

from typing import NoReturn, List, Tuple
from .parent_selection import roulette_selection


class Genome:
    """ Data storage class for feature weights """
    def __init__(self, genome_id: int, score: int or None, weights: List):
        """
        :param genome_id: Unique integer ID number for node, e.g. 194th node)
        :param weights: Ordered importance of self.features as a list of floats
        """

        self.id = genome_id
        self.score = score
        self.weights = weights

    def __str__(self):
        return "Genome {0}: {1}".format(self.id, self.score)


class Generation:
    """ Data storage class for nodes in a generation"""

    def __init__(self, generation_id: int, genomes: List[Genome]):
        """
        :param generation_id: Unique integer ID number for generation, e.g. 6th generation
        :param genomes: List of Genome types
        """

        self.id = generation_id
        self.genomes = genomes

    def __str__(self):
        return "Generation: {0}{1}".format(self.id, ["\n    ".join(str(genome)) for genome in self.genomes])


class NEAT:

    def __init__(self,
                 features: List,
                 outputs: List,
                 iterate_evolution: bool=False,
                 generation_size: int=100,
                 max_score: bool=None,
                 max_generations: bool=None):

        """
        :param features: A list of features as floats
        :param outputs: A list of possible outputs as integers
        :param iterate_evolution: True -> Yield every genome of every generation
                                  False -> Return only the best Genome from the final generation
        :param generation_size: How many genomes in each generation DEFAULT=100
        :param max_generations: An upper boundary for the needed generations to stop evolution
        :param max_score: An upper boundary for the needed score to stop evolution
        """

        #  Initialize Class
        self.features = features
        self.outputs = outputs

        self.iterate_evolution = iterate_evolution
        self.generation_size = generation_size

        self.max_generations = max_generations
        self.max_score = max_score

        self.latest_generation = None

        #  Set standard parent selection function
        self.parent_selection = roulette_selection

    def evolve(self) -> NoReturn or Genome:
        """
        :return: if self.iterate_evolution is True -> Yield every genome of every generation
                 elif self.iterate_evolution is False -> Return only the best Genome from the final generation
        """

        #  Initialize Variables
        current_generation = None

        _num_genomes = int()
        _num_generations = int()

        while True:
            """ Evolve new generation """

            new_generation = Generation(_num_generations + 1, [])

            #  Find parents
            parents: List[Tuple] = self.parent_selection(current_generation, "score")

            #  Reproduce
            for couple in parents:
                child = Genome(_num_genomes + 1, self.reproduction(couple))

                new_generation.genomes.append(child)
                _num_genomes += 1

            #  Mutate
            new_generation.genomes = map(self.mutate, new_generation.genomes)

            #  Test Genomes
            for genome in new_generation:

                sys.stdout.write(genome)

                #  Read current score
                with open(sys.stdin) as stdin:
                    try:
                        genome.score = int(stdin.readlines()[0]) or None
                    except EOFError:
                        print("no score received")
                        raise
                    except TypeError:
                        print("Score input is of non-integer type")
                        raise

            #  Find fittest genome in new generation
            fittest_genome = sorted(new_generation.genomes.items(), key=operator.itemgetter(1), reverse=True)[0]

            #  Return logic
            if fittest_genome.score >= self.max_score or \
                    _num_generations >= self.max_generations:
                    break

            if self.iterate_evolution:
                print(current_generation, sep=",", end='\n: ')
            else:
                continue

            #  Age population
            current_generation = new_generation

        print(fittest_genome)
        exit("OK - Completed")


