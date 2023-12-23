import re
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
    distance = get_distance_sum()

    print(distance)
    return distance


def part2(distance):
    average_increase_per_step = get_distance_sum(2) - distance

    target = 1000000
    print(distance + (average_increase_per_step * (target - 1)))


if __name__ == '__main__':
    part2(part1())
