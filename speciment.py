import struct
from base64 import decode

import numpy as np
import random


class Speciment:

    def __init__(self, signs=None):
        if signs is None:
            self.signs = np.arange(0, 10, 0.1)
        else:
            self.signs = signs

    def mutation(self):
        mutant = random.choice(self.signs)
        print("До мутации: ", mutant)
        print("После: ", self.float_to_bin(mutant))

    def bin_to_float(self, b):
        bf = self.int_to_bytes(int(b, 2), 8)
        return struct.unpack('>d', bf)[0]

    def int_to_bytes(self, n, length):
        return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]

    def float_to_bin(self, value):
        [d] = struct.unpack(">Q", struct.pack(">d", value))
        return '{:064b}'.format(d)

    def get_parts_bin(self):
        result_parts = []
        for i in self.signs:
            sign = self.float_to_bin(i)
            l = sign.__len__() + 1

            part_1 = sign[0:l // 2]

            part_2 = sign[l // 2:]
            result_parts.append([part_1, part_2])
        return result_parts

    def translate_signs_in_float(self):
        count = 0
        for i in self.signs:
            self.signs[count] = self.bin_to_float(i)
