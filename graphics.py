import matplotlib.pyplot as plt
import numpy as np
from numpy import sort

from speciment import Speciment


def log_function():
    argument = np.arange(0.1, 10.1, 0.1)
    log_func = 4 * np.square(argument)
    return [argument, log_func]


def draw_pyplot(argument, log_fun):
    plt.plot(argument, log_fun)
    plt.show()


def draw_two_plot(func_speciment=Speciment):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(log_function()[0], log_function()[1], label='Функция приспосабливания')
    ax2.plot(func_speciment.signs, func_speciment.genes, label='Особь')
    ax1.legend()
    ax2.legend()
    plt.show()


def euclid_distance(population):
    new_sum = 0
    euclid_distance_of_population = []

    for i in range(len(population)):
        for count in range(len(population[i].genes)):
            # new_sum += np.linalg.norm(log_function()[1][count] - population[i].genes[count])
            new_sum += np.square(log_function()[1][count] - population[i].genes[count])
        euclid_distance_of_population.append(np.sqrt(new_sum))
        # print("Евклидово расстояние: ", new_sum)
        new_sum = 0
    return euclid_distance_of_population


def euclid_distance_test(population):
    new_sum = 0
    euclid_distance_of_population = []

    for i in range(len(population)):
        for count in range(len(population[i].genes)):
            # new_sum += np.linalg.norm(log_function()[1][count] - population[i].genes[count])
            x = log_function()[1][count]
            y = population[i].genes[count]
            new_sum += np.square(x - y)
        euclid_distance_of_population.append(np.sqrt(new_sum))
        # print("Евклидово расстояние: ", new_sum)
        new_sum = 0
    return euclid_distance_of_population
