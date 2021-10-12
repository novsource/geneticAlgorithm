import random

import numpy as np
import speciment


def generic_log_function():
    argument = np.arange(0.1, 10.1, 0.1)
    log_function = np.log10(2*argument)
    return [argument, log_function]


def reproduction_speciment(parent_father=speciment, parent_mother=speciment):
    parts_father = parent_father.get_parts_bin()
    parts_mother = parent_mother.get_parts_bin()

    descendant_signs = []

    count = 0
    for i in parts_mother:
        descendant_signs.append(list(parts_father)[count][0] + i[1])
        count += 1

    descendant = speciment.Speciment(descendant_signs)
    descendant.translate_signs_in_float()
    print(descendant.signs)


