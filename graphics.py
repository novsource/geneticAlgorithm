import matplotlib.pyplot as plt
import numpy as np

from speciment import Speciment


def log_function():
    argument = np.arange(0.1, 10.1, 0.1)
    log_func = np.log10(2 * argument)
    return [argument, log_func]


def draw_pyplot(argument, log_fun):
    plt.plot(argument, log_fun)
    plt.show()


def draw_two_plot(func_speciment = Speciment):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot = (log_function()[0], log_function()[1])
    ax2.plot = (func_speciment.signs, func_speciment.genes)
    ax1.legend()
    ax2.legend()
    plt.show()


def euclid_distance(population):
    new_sum = 0
    count = 0

    euclid_distance_of_population = []

    for spec in population:
        # np.asarray(spec.signs[count], dtype='float')
        for i in log_function()[1]:
            new_sum += np.sqrt(np.square(i - spec.genes[count]))
        euclid_distance_of_population.append(new_sum)
        print("Евклидово расстояние: ", np.sqrt(new_sum))
        new_sum = 0
    return euclid_distance_of_population
