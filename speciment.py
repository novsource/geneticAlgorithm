import struct
from codecs import decode

import numpy as np
import random


class Speciment:

    def __init__(self, signs=None):
        if signs is None:
            self.signs = np.arange(0, 10, 0.1)
        else:
            self.signs = signs

    def mutation(self):
        parts = self.get_parts_bin()

        count = 0
        print("Мутация в деле, границы типов на пределе: ")
        for i in parts:
            random_part = int(random.random())
            random_razr = random.randint(0, 16)

            # Мой индус-код (пока не трогаем, работает)
            number = "1" if i[random_part][random_razr] == "0" else "0"
            parts[count][random_part] = parts[count][random_part][:random_razr] + \
                                        number + \
                                        parts[count][random_part][random_razr + 1:]
            self.signs[count] = self.bin_to_float(parts[count][0] + parts[count][1])
            count += 1

    def int_to_bytes(self, n, length):  # Helper function
        return decode('%%0%dx' % (length << 1) % n, 'hex')[-length:]

    def bin_to_float(self, b, length=8):
        # hx = hex(int(b, 2))
        # return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]
        bf = self.int_to_bytes(int(b, 2), 8)
        return struct.unpack('>d', bf)[0]

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
            count += 1
