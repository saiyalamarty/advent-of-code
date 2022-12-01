import os


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    with open(file_path, "r") as input_file:
        for line in input_file:
            ...


if __name__ == "__main__":
    main()
