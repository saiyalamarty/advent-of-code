import os
import re


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )
    answer_1 = 0
    numbers = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            mapping = {}
            left, right = line.strip().split(" | ")

            out_1 = list(map(len, right.split()))
            out_1 = [each for each in out_1 if each in [2, 3, 4, 7]]
            answer_1 += len(out_1)

            right = ["".join(sorted(each)) for each in right.split()]
            left = sorted(["".join(sorted(each)) for each in left.split()], key=len)

            mapping[1], mapping[7], mapping[4], *left, mapping[8] = left
            # mapping[6] = [each for each in left if not check_substring(mapping[1], each) and len(each) == 6]

            while len(left):
                popper = ""
                for each in left:
                    match len(each):
                        case 6:
                            if not check_substring(mapping[1], each):
                                mapping[6] = each
                                popper = each
                                break
                            else:
                                pattern = "[" + each + "]"
                                new_string = re.sub(pattern, "", mapping[8])
                                if check_substring(new_string, mapping[4]):
                                    mapping[0] = each
                                    popper = each
                                    break
                                else:
                                    mapping[9] = each
                                    popper = each
                                    break

                        case 5:
                            if 6 not in mapping:
                                continue

                            if 5 not in mapping:
                                pattern = "[" + each + "]"
                                new_string = re.sub(pattern, "", mapping[6])
                                if len(new_string) == 1:
                                    mapping[5] = each
                                    popper = each
                                    break

                            if 5 in mapping:
                                pattern = "[" + each + "]"
                                new_string = re.sub(pattern, "", mapping[5])
                                if len(new_string) == 2:
                                    mapping[2] = each
                                    popper = each
                                    break
                                else:
                                    mapping[3] = each
                                    popper = each
                                    break

                if len(left) and popper:
                    left.remove(popper)

            new_mapper = {}
            for key, value in mapping.items():
                new_mapper[value] = key

            digit = ""
            for each in right:
                digit += str(new_mapper["".join(sorted(each))])

            numbers.append(int(digit))

    answer_2 = sum(numbers)

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def check_substring(sub, full):
    return all(letter in full for letter in sub)


def remove_substring(sub, full):
    return (lambda x, y: x.replace(y, ""))(full, sub)


if __name__ == '__main__':
    main()
