from pathlib import Path
from collections import Counter
from pprint import pprint


def day7_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    ORDER: list[str] = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def custom_key(items: list[str]) -> list[int]:
        return [ORDER.index(char) for char in items]

    hands: list[tuple[int, int, list[str]]] = []
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            hand, val = line.split()
            cards_in_hand = list(hand)
            counter = Counter(cards_in_hand)

            # 7 types of hands => rank 7-1
            counts = counter.most_common()
            rank = 1
            if counts[0][1] == 5:  # 5 of a kind
                rank = 7
            elif counts[0][1] == 4:  # 4 of a kind
                rank = 6
            elif counts[0][1] == 3 and counts[1][1] == 2:  # full house
                rank = 5
            elif counts[0][1] == 3:  # 3 of a kind
                rank = 4
            elif counts[0][1] == 2 and counts[1][1] == 2:  # two pair
                rank = 3
            elif counts[0][1] == 2:  # one pair
                rank = 2
            else:
                pass
            hands.append((rank, int(val), cards_in_hand))

    hands.sort(key=lambda hand: (-hand[0], custom_key(hand[2])), reverse=True)
    val = sum([(index + 1) * hand[1] for index, hand in enumerate(hands)])
    print(val)

def day7_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "known_input.txt"

    ORDER: list[str] = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def custom_key(items: list[str]) -> list[int]:
        return [ORDER.index(char) for char in items]

    hands: list[tuple[int, int, list[str]]] = []
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            hand, val = line.split()
            cards_in_hand = list(hand)
            counter = Counter(cards_in_hand)

            print(hand)

            joker_count = counter.pop("J", 0)
            if joker_count == 5:
                hands.append((7, int(val), cards_in_hand))
                continue

            # 7 types of hands => rank 7-1
            counts = counter.most_common()
            rank = 1
            if counts[0][1] == 5:               # 5 of a kind
                rank = 7                        #
            elif counts[0][1] == 4:             # 4 of a kind
                if joker_count == 1:            # actually, 5 of a kind
                    rank = 7                    #
                else:                           #
                    rank = 6                    #
            elif counts[0][1] == 3:             # 3 of a kind
                if joker_count == 2:            # actually, 5 of a kind
                    rank = 7                    # 
                elif joker_count == 1:          # actually, 4 of a kind
                    rank = 6                    #
                elif counts[1][1] == 2:         # actually, a full house
                    rank = 5                    #
                else:                           #
                    rank = 4                    #
            elif counts[0][1] == 2:             # one pair
                if joker_count == 3:            # actually, a 5 of a kind
                    rank = 7                    #
                elif joker_count == 2:          # actually, 4 of a kind
                    rank = 6                    #
                elif joker_count == 1:          #
                    if counts[1][1] == 1:       # actually, full house
                        rank = 5                #
                    else:                       # actually, 3 of a kind
                        rank = 4                #
                elif counts[1][1] == 2:         # actually, two pair
                    rank = 3                    #
                else:                           #
                    rank = 2                    #
            else:
                if joker_count == 0:
                    rank = 1
                if joker_count == 1:
                    rank = 1
                else:
                    rank = 7 - (5 - joker_count)

            hands.append((rank, int(val), cards_in_hand))

    hands.sort(key=lambda hand: (-hand[0], custom_key(hand[2])), reverse=True)
    pprint(hands)
    val = sum([(index + 1) * hand[1] for index, hand in enumerate(hands)])
    print(val)

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day7_pt2(working_dir)
