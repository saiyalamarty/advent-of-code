import os
from functools import reduce


class Packet:
    def __init__(self, binary: str):
        self.version = int(binary[:3].zfill(4), 2)
        self.type = int(binary[3:6].zfill(4), 2)
        if self.type == 4:
            start_bit = 1
            group_count = 0
            number_b = ""
            while start_bit:
                group_b = binary[6 + (5*group_count):6 + (5*(group_count + 1))]
                start_bit, group_b = group_b[:1], group_b[1:]
                number_b += group_b
            self.value = int(number_b, 2)


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )

    with open(file_path, "r") as input_file:
        for line in input_file:
            hexadecimal = line

    binary = reduce(lambda bi, he: bi + "{0:04b}".format(int(he, 16)), hexadecimal, "")
    ...


if __name__ == '__main__':
    main()
