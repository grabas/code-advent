import re
from src.utils import get_input_file_contents

"""
To get information, once a bag has been loaded with cubes,
the Elf will reach into the bag, grab a handful of random cubes,
show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (resource file).
Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets
of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    
In game 1, three sets of cubes are revealed from the bag (and then put back again).
The first set is 3 blue cubes and 4 red cubes;
the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once;
similarly,game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded
with only 12 red cubes, 13 green cubes, and 14 blue cubes.

What is the sum of the IDs of those games?
"""

resource = "2_1.txt"

cube_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_game_id(game_record):
    return int(game_record.split(": ")[0].split(" ")[1])


def resolve_possible(game_record):
    rounds = [game_round.strip() for game_round in re.split(r'Game \d+:|[,;]', game_record) if game_round.strip()]
    for game_round in rounds:
        cubes = game_round.split(" ")
        if cube_limits[cubes[1]] < int(cubes[0]):
            return False

    return True


def main():
    total = 0
    for game_record in get_input_file_contents(resource):
        total += get_game_id(game_record) if resolve_possible(game_record) else 0

    print(total)
    return total


if __name__ == '__main__':
    main()