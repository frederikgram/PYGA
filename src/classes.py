""" Collection of classes to be used in neat.py"""


class Genome:
    """ Data storage class for feature weights """
    def __init__(self, genome_id: int, weights: list, score: int or None = None):
        """
        :param genome_id: Unique integer ID number for node, e.g. 194th node)
        :param weights: Ordered importance of self.features as a list of floats
        """

        self.id = genome_id
        self.weights = weights
        self.score = score

    def __str__(self):
        return "Genome {0}: {1}".format(self.id, self.score)


class Generation:
    """ Data storage class for nodes in a generation"""

    def __init__(self, generation_id: int, genomes: list):
        """
        :param generation_id: Unique integer ID number for generation, e.g. 6th generation
        :param genomes: List of Genome types
        """

        self.id = generation_id
        self.genomes = genomes

    def __str__(self):
        """ Sample output:

            Generation: 9
                - Genome 4: 39432
                - Genome 5: 423
                - Genome 6: -5
            """

        return "Generation: {0}{1}".format(self.id,
                                           '\n'.join(["    -".join(str(genome)) for genome in self.genomes]))

