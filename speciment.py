import numpy as np
import random


class Speciment:

    def __init__(self, signs=None, genes=None):
        if signs is None:
            self.signs = np.arange(0.1, 10.1, 0.1)
            self.genes = np.arange(-0.7, 1.3, 0.02)
        else:
            self.signs = signs
            self.genes = genes

    def mutation(self, age):
        random_mutation = random.randint(0, 1)
        for i in range(random.randint(10, len(self.genes))):
            self.genes[i] = self.genes[i] + random.uniform(-0.2 / (age / 100 * random.randint(1, 99)),
                                                           0.2 / (age / 100 * random.randint(1, 99))) \
                if random_mutation // 2 == 0 else self.genes[i] - random.uniform(
                -0.2 / (age / 100 * random.randint(0, 99)),
                0.2 / (age / 100 * random.randint(0, 99)))
