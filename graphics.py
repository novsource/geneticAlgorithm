import matplotlib.pyplot as plt
import numpy as np

import generic
import speciment


def draw_pyplot(argument, log_function):
    plt.plot(argument, log_function)
    plt.show()


def euclid_distance(spec, log_fuction=generic.generic_log_function()[1]):
    new_sum = 0
    count = 0
    for i in log_fuction:
        new_sum += np.sqrt(np.square(i - spec.signs[count]))
    print(np.sqrt(new_sum))