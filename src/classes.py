""" Collection of classes to be used in ga.py"""


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
        """ Sample output:

        Genome 584: 3525
          - weights: [0.34, 0.22, 0.95]
        """

        return "Genome {0}: {1}\n  - weights: {2}".format(
            self.id, self.score, self.weights
        )


class Generation:
    """ Data storage class for nodes in a generation"""

    def __init__(self, generation_id: int, genomes: list):
        """
        :param generation_id: Unique integer ID number for generation, e.g. 6th generation
        :param genomes: List of Genome types
        """

        self.id = generation_id
        self.genomes = genomes

    @property
    def average_score(self):
        return sum([genome.score for genome in self.genomes]) / len(self.genomes)

    def __str__(self):
        """ Sample output:

            Generation: 9
                - Genome 4: 39432
                    - weights: [0.43, 0.12, 0.83]

                - Genome 5: 423
                    ...

                - Genome 6: -5
                    ...
            """

        return "Generation: {0}\n    {1}".format(
            self.id, "\n\n    ".join([str(genome) for genome in self.genomes])
        )
