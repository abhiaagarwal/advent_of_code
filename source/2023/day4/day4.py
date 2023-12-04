from pathlib import Path
from collections import Counter


def day4_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    sum: int = 0
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            numbers = [numbers.split() for numbers in line[10:-1].split(" | ")]

            matching_numbers = [
                given_number
                for given_number in numbers[1]
                if given_number in numbers[0]
            ]
            if (size := len(matching_numbers)) > 0:
                value = 2 ** (size - 1)
                sum += value
    print(sum)


def day4_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    card_num: int = 1
    card_counter: Counter[int] = Counter()
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            card_counter.update({card_num: 1})
            numbers = [numbers.split() for numbers in line[10:-1].split(" | ")]

            matching_numbers = [
                given_number
                for given_number in numbers[1]
                if given_number in numbers[0]
            ]
            if (size := len(matching_numbers)) > 0:
                scratches_won = {
                    new_card + 1: 1 * card_counter[card_num]
                    for new_card in range(card_num, card_num + size)
                }
                card_counter.update(scratches_won)
            card_num += 1
    print(card_counter.total())


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day4_pt2(working_dir)
