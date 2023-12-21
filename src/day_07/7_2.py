import math
import re
from collections import Counter
from src.utils import get_input_file_contents

"""
To make things a little more interesting, the Elf introduces one additional rule.
Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2.
The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type;
for example, QJJQ2 is now considered four of a kind.
However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card
it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483

32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set.

What are the new total winnings?

"""

resource = "day_07.txt"
data = get_input_file_contents(resource)

card_values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]


def sort_hands(hands):
    return sorted(hands, key=lambda hand: (-get_hand_combination(hand), -get_hand_value_inprint(hand)), reverse=True)


def replace_j_with_common(hand):
    if hand.count('J') == len(hand):
        return hand

    most_common = Counter(hand).most_common(2)
    replacement_char = most_common[0][0] if most_common[0][0] != 'J' else most_common[1][0]

    return hand.replace('J', replacement_char)


def get_hand_combination(hand):
    card_counts = Counter(replace_j_with_common(hand)).values()
    power_mapping = {1: 7, 2: 6 if 4 in card_counts else 5, 3: 4 if 3 in card_counts else 3, 4: 2}

    return power_mapping.get(len(card_counts), 1)


def get_hand_value_inprint(hand):
    return int("".join(([str(card_values.index(card)).zfill(2) for card in list(hand)])))


def sort_and_combine():
    hands_and_values = [(hand.split(" ")[0], hand.split(" ")[1]) for hand in data]
    sorted_hands = sort_hands([hand for hand, value in hands_and_values])
    sorted_data = ["{} {}".format(hand, dict(hands_and_values)[hand]) for hand in sorted_hands]

    return sorted_data


def main():
    total = sum(int(datum.split(" ")[1]) * (i + 1) for i, datum in enumerate(sort_and_combine()))

    print(total)
    return total


if __name__ == '__main__':
    main()
