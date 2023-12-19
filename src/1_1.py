import re
from utils import get_input_file_contents

"""
On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number.

For example:
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

In this example, the calibration values of these four lines are
12, 38, 15, and 77.

Adding these together produces 142.
Consider your entire calibration document (resource).
What is the sum of all of the calibration values?
"""

resource = "1_1.txt"


def extract_digits(text):
    return re.findall(r'\d', text)


def get_first_and_last_number(text):
    numbers = extract_digits(text)
    return int("".join([numbers[0], numbers[-1]]))


def main():
    total = 0
    for line in get_input_file_contents(resource):
        total += get_first_and_last_number(line)

    print(total)


if __name__ == '__main__':
    main()