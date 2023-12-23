import re
import math
from src.utils import get_input_file_contents

resource = "day_11.txt"
universe = get_input_file_contents(resource)


def vertical_expansion(data, times=1):
    expanded_data = []
    for index, line in enumerate(data):
        expanded_data.append(line)
        if len(re.findall(r"\.", line)) == len(line):
            for i in range(times - 1):
                expanded_data.append('.' * len(line))

    return expanded_data


def flip_perspective(data):
    flipperino = []
    for i in range(len(data[0])):
        flipperino.append(''.join([line[i] for line in data]))

    return flipperino


def expand_universe(times=1):
    data = universe
    data = vertical_expansion(data, times)
    data = flip_perspective(data)
    data = vertical_expansion(data, times)

    return flip_perspective(data)


def get_galaxies_coordinates(data):
    galaxies = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))

    return galaxies


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_distance_sum(expansion_multiplier=1):
    total = 0
    data = expand_universe(expansion_multiplier)
    galaxies = get_galaxies_coordinates(data)
    for i, galaxy in enumerate(galaxies):
        distances = []
        for other_galaxy in galaxies[i + 1:]:
            distances.append(manhattan_distance(galaxy, other_galaxy))

        total += sum(distances)

    return total


def part1():
    print(get_distance_sum())


def part2():
    range_limit = 10
    distances = [get_distance_sum(i) for i in range(1, range_limit)]

    average_increase_per_step = int((distances[-1] - distances[0]) / (len(distances) - 1))

    target = 1000000
    print(distances[1] + (average_increase_per_step * (target - 2)))


if __name__ == '__main__':
    part1()
    part2()
