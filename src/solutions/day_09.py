import numpy as np
from numpy.polynomial import Polynomial
from src.utils import get_input_file_contents

resource = "day_09.txt"
data = get_input_file_contents(resource)


def predict_next(sequence):
    indices = np.arange(len(sequence))

    polynomial_model = Polynomial.fit(
        indices,
        np.array(sequence), deg=min(30, len(indices) - 1)
    )

    return int(round(polynomial_model(len(sequence))))


def part1():
    total = 0
    for line in data:
        sequence = [int(number) for number in line.split(" ")]
        total += predict_next(sequence)
    print(total)


def part2():
    total = 0
    for line in data:
        sequence = [int(number) for number in line.split(" ")][::-1]
        total += predict_next(sequence)
    print(total)


if __name__ == '__main__':
    part1()
    part2()
