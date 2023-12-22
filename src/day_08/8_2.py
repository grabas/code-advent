import itertools
import math
from src.utils import get_input_file_contents

"""
The sandstorm is upon you and you aren't any closer to escaping the wasteland.
You had the camel follow the instructions, but you've barely left your starting position.
It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime?
Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact:
the number of nodes with names ending in A is equal to the number ending in Z!
If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same
time until they all simultaneously end up at nodes that end with Z.

For example:

    LR
    
    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right
instruction, use that instruction to simultaneously navigate away from both nodes you're currently on.
Repeat this process until all of the nodes you're currently on end with Z. 
(If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.)
In this example, you would proceed as follows:
    
    Step 0: You are at 11A and 22A.
    Step 1: You choose all of the left paths, leading you to 11B and 22B.
    Step 2: You choose all of the right paths, leading you to 11Z and 22C.
    Step 3: You choose all of the left paths, leading you to 11B and 22Z.
    Step 4: You choose all of the right paths, leading you to 11Z and 22B.
    Step 5: You choose all of the left paths, leading you to 11B and 22C.
    Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
    
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A
 
How many steps does it take before you're only on nodes that end with Z?
"""

resource = 'day_08.txt'
data = get_input_file_contents(resource)

instructions = data[0].replace("L", "0").replace("R", "1")
data = data[2:]


def least_common_multiple(array):
    lcm = array[0]

    for i in range(1,len(array)):
        lcm = lcm*array[i]//math.gcd(lcm, array[i])

    return lcm


def create_lookup():
    lookup = {}
    for line in data:
        key, values = line.split(' = ')
        values = values.strip('()').split(', ')
        lookup[key] = values
    return lookup


lookup_dict = create_lookup()


def main():
    steps = []
    starting_points = [key for key in lookup_dict.keys() if key.endswith("A")]
    for starting_point in starting_points:
        step = 0
        current_key = starting_point
        for instruction in itertools.cycle(instructions):
            step += 1
            current_key = lookup_dict.get(current_key)[int(instruction)]
            if current_key.endswith("Z"):
                steps.append(step)
                break

    lcm = least_common_multiple(steps)

    print(lcm)
    return lcm


if __name__ == '__main__':
    main()
