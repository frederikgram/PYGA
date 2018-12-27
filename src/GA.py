""" Dynamic NEAT GA implemented in Python 3.7 - 27/12/2018 """

from typing import NoReturn, List, Tuple
import sys


class Genome:
    """ Data storage class for feature weights """
    def __init__(self, genome_id: int, score: int, weights: List):
        """
        :param node_id: Unique integer ID number for node, e.g. 194th node)
        :param weights: Ordered importance of self.features as a list of floats
        """

        self.genome_id = genome_id
        self.score = score
        self.weights = weights


class Generation:
    """ Data storage class for nodes in a generation"""

    def __init__(self, generation_id: int, genomes: List[Genome]):
        """
        :param generation_id: Unique integer ID number for generation, e.g. 6th generation
        :param genomes: List of Genome types
        """

        self.id = generation_id
        self.genomes = genomes


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
        self.parent_selection = self.roulette_selection

    def evolve(self) -> NoReturn or Genome:
        """
        :return: if self.iterate_evolution is True -> Yield every genome of every generation
                 elif self.iterate_evolution is False -> Return only the best Genome from the final generation
        """

        #  Initialize Variables
        current_score = int()
        current_generation = None

        _num_genomes = int()
        _num_generations = int()

        while True:

            new_generation = list()

            """ Create new generation """

            #  Find parents
            parents: List[Tuple] = self.parent_selection(current_generation, "score")

            #  Reproduce
            for couple in parents:
                new_generation.append(self.reproduction(couple))

            #  Mutate
            new_generation = map(self.mutate, new_generation)

            current_generation = new_generation

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

            #  Store results locally
            self.latest_generation = current_generation

            #  Return logic
            if current_score >= self.max_score or \
                    _num_generations >= self.max_generations:
                    break

            if self.iterate_evolution:
                print(current_generation, sep=",", end='\n: ')
            else:
                continue

        print(current_generation)
        exit("OK - Completed")

    def mutate(self, parents: Tuple[Genome]) -> Genome:
        """
        :param parents: Tuple of two parent genomes
        :return: Genome
        """

        mutated_weights = [None]

        return Genome(self.num_genomes, mutated_weights)

    @staticmethod
    def rank_selection(objects: object, fitness_attribute: str) -> Tuple[object]:
        """ Parent Rank Selection Algorithm """

        for obj in objects:
            try:
                score = getattr(obj, fitness_attribute)
            except AttributeError:
                print("Invalid fitness attribute")
                raise

        return None

    @staticmethod
    def roulette_selection(objects: object, fitness_attribute: str) -> Tuple[object]:
        """ Roulette Wheel Parent Selection Algorithm """

        import operator
        import random

        #  Calculate total sum of fitness values
        fitness_sum = sum([getattr(obj, fitness_attribute) for obj in object])

        #  Find random point
        point = random.uniform(0, fitness_sum)

        # Find the object which fitness attribute exceeds the variable point
        for obj in sorted(objects.items(), key=getattr(operator.itemgetter(1), fitness_attribute)):
            if fitness_sum > obj:
                return obj

            return tuple()

    @staticmethod
    def stochastic_sampling(objects: object, fitness_attribute: str) -> Tuple[object]:
        """ Stochastic Universal Sampling Parent Selection Algorithm """
        pass
