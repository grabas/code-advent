from collections import defaultdict
import re
from src.utils import get_input_file_contents

"""
The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even
diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
    
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; 
their sum is 4361.

Of course, the actual engine schematic is much larger.

What is the sum of all of the part numbers in the engine schematic?
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
    total = sum(sum(number) for number in symbol_coordinates.values())

    print(total)
    return total


if __name__ == '__main__':
    main()

