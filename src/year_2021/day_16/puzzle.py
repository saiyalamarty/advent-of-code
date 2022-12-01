import math
import os
from functools import reduce


def pop_binary(binary, length, int_cast=True):
    left, right = binary[:length], binary[length:]
    if int_cast:
        left = int(left, 2)

    return left, right


class Packet:
    def __init__(self, binary: str):
        self.binary = binary

        self.version, self.binary = pop_binary(self.binary, 3)
        self.type, self.binary = pop_binary(self.binary, 3)

        self.value = None

        self.length_type = None
        self.sub_packets = []


def process_binary(packet: Packet, binary: str) -> (Packet, str):
    if not binary or int(binary, 2) == 0:
        return packet

    if packet.type == 4:
        start_bit = 1
        number_b = ""
        while start_bit:
            group_b, binary = pop_binary(binary, 5, False)
            start_bit, group_b = pop_binary(group_b, 1)
            number_b += group_b
        packet.value = int(number_b, 2)
        return packet, binary
    else:
        length_type, binary = pop_binary(binary, 1)
        if length_type == 0:
            sub_packet_length, binary = pop_binary(binary, 15)
            sub_packet_binary, binary = pop_binary(binary, sub_packet_length, False)
            while sub_packet_binary and int(sub_packet_binary, 2) != 0:
                p = Packet(sub_packet_binary)
                sub_packet_binary = p.binary

                p, sub_packet_binary = process_binary(p, sub_packet_binary)

                packet.sub_packets.append(p)
        else:
            sub_packet_count, binary = pop_binary(binary, 11)
            for _ in range(sub_packet_count):
                p = Packet(binary)
                binary = p.binary

                p, binary = process_binary(p, binary)

                packet.sub_packets.append(p)
        return packet, binary


def version_total(packet: Packet, total: int):
    total += packet.version

    if not packet.sub_packets:
        return total

    for p in packet.sub_packets:
        total = version_total(p, total)

    return total


def packet_value(packet: Packet):
    if not packet.sub_packets:
        return packet.value

    sub_packet_values = [packet_value(p) for p in packet.sub_packets]
    value = 0
    match packet.type:
        case 0:
            value = sum(sub_packet_values)
        case 1:
            value = math.prod(sub_packet_values)
        case 2:
            value = min(sub_packet_values)
        case 3:
            value = max(sub_packet_values)
        case 5:
            value = int(sub_packet_values[0] > sub_packet_values[1])
        case 6:
            value = int(sub_packet_values[0] < sub_packet_values[1])
        case 7:
            value = int(sub_packet_values[0] == sub_packet_values[1])

    return value


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    with open(file_path, "r") as input_file:
        for line in input_file:
            hexadecimal = line

    binary = reduce(lambda bi, he: bi + "{0:04b}".format(int(he, 16)), hexadecimal, "")
    packet = Packet(binary)
    packet, _ = process_binary(packet, packet.binary)

    answer_1 = version_total(packet, 0)
    answer_2 = packet_value(packet)

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


if __name__ == "__main__":
    main()
