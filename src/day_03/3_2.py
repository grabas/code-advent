import re
import math
from src.utils import get_input_file_contents

"""
Before you can explain the situation, she suggests that you look out the window.
There stands the engineer, holding a phone in one hand and waving with the other.
You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out
which gear needs to be replaced.

Consider the same engine schematic again:
    
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

In this schematic, there are two gears.
The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
The second gear is in the lower right; its gear ratio is 451490.
(The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

resource = "day_03.txt"

engine_schematic = get_input_file_contents(resource)
line_range = range(len(engine_schematic))


def get_symbol_coordinates():
    return {(line_index, char_index): [] for line_index in line_range for char_index in line_range
            if engine_schematic[line_index][char_index] != '.' and not engine_schematic[line_index][char_index].isdigit()}


def filter_valid_numbers():
    symbols = get_symbol_coordinates()
    for line_index in line_range:
        for number in re.finditer(r'\d+', engine_schematic[line_index]):
            adjacent_numbers = {(adjacent_lines, number_edge) for adjacent_lines in (line_index - 1, line_index, line_index + 1)
                    for number_edge in range(number.start() - 1, number.end() + 1)}

            for coordinates in adjacent_numbers & symbols.keys():
                symbols[coordinates].append(int(number.group()))

    return symbols


def main():
    symbol_coordinates = filter_valid_numbers()
    total = sum(math.prod(number) for number in symbol_coordinates.values() if len(number) == 2)

    print(total)
    return total


if __name__ == '__main__':
    main()

