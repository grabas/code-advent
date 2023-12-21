import re
import math
from src.utils import get_input_file_contents

"""
As the race is about to start, you realize the piece of paper with race times and record distances you 
got earlier actually just has very bad kerning.
There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

    Time:      7  15   30
    Distance:  9  40  200

now instead means this:

    Time:      71530
    Distance:  940200

Now, you have to figure out how many ways there are to win this single race.
In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters.
You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?

"""

resource = "day_06.txt"
data = get_input_file_contents(resource)


def get_data():
    return int("".join(re.findall(r'(\d+)', data[0]))), int("".join(re.findall(r'(\d+)', data[1])))


def brute_force_number_of_winning(record):
    time, distance = record

    number_of_winning = 0
    for i in range(1, time):
        distance_traveled = i * (time - i)
        number_of_winning += 1 if distance_traveled > distance else 0

    return number_of_winning


def main():
    total = brute_force_number_of_winning(get_data())

    print(total)
    return total


if __name__ == '__main__':
    main()
