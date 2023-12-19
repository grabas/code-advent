import re
from numwords_to_nums.numwords_to_nums import NumWordsToNum
from src.utils import get_input_file_contents


"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are
29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""

resource = "1_1.txt"
num = NumWordsToNum()


def extract_digits(string):
    return re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", string)


def join_first_and_last_number(text):
    numbers = extract_digits(text)

    if not numbers:
        return 0

    first_number = num.numerical_words_to_numbers(numbers[0])
    last_number = num.numerical_words_to_numbers(numbers[-1])

    return int(f"{first_number}{last_number}")


def main():
    total = 0
    for line in get_input_file_contents(resource):
       total += join_first_and_last_number(line)

    print(total)
    return total


if __name__ == '__main__':
    main()