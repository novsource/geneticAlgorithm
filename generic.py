import random

import numpy as np

import graphics
from speciment import Speciment


def reproduction_speciment(parent_father=Speciment, parent_mother=Speciment):
    random_range_of_reproduction = random.randint(1, len(parent_mother.genes))

    gen_father_first = parent_father.genes[0: random_range_of_reproduction]

    gen_mother_second = parent_mother.genes[random_range_of_reproduction:len(parent_mother.genes)]
    gen_father_second = parent_father.genes[0:random_range_of_reproduction]

    gen_mother_first = parent_mother.genes[random_range_of_reproduction:len(parent_father.genes)]

    if random.randint(0, 1) == 0:
        descendants = (Speciment(genes=np.hstack([gen_father_first, gen_mother_second]), signs=parent_mother.signs))
    else:
        descendants = (Speciment(genes=np.hstack([gen_father_second, gen_mother_first]), signs=parent_mother.signs))

    return descendants


def population_reproduction(population):
    for i in range(population.__len__() // 2):
        for j in range(2):
            random_father = population[random.randint(0, population.__len__() - 1)]
            random_mother = population[random.randint(0, population.__len__() - 1)]
            descendant = reproduction_speciment(random_father, random_mother)
            population.append(descendant)
    return population


def population_mutation(population, age):
    for i in range(random.randint(10, population.__len__()-1)):
        random_speciment = random.randint(0, population.__len__() // 2)
        population[random_speciment].mutation(age)
    return population


def population_selection(population):
    euclid_distance_of_population = graphics.euclid_distance(population)
    for i in range(population.__len__() // 2):
        index_for_del = euclid_distance_of_population.index(max(euclid_distance_of_population))
        population.pop(index_for_del)
        euclid_distance_of_population.pop(index_for_del)
    return population
