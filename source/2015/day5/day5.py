from pathlib import Path

import hashlib


def day5_pt1(working_dir: Path) -> None:
    naughty_combos = {"ab", "cd", "pq", "xy"}
    vowels = {"a", "e", "i", "o", "u"}

    input_file_path = working_dir / "input.txt"
    nice_word_count = 0
    with input_file_path.open("r") as input_file:
        for word in input_file:
            naughty: bool = False
            for naughty_combo in naughty_combos:
                if naughty_combo in word:
                    naughty = True
                    break
            if naughty:
                print(f"{word} is naughty because combo")
                continue

            vowel_counter: int = 0
            naughty = True
            for vowel in vowels:
                vowel_counter += word.count(vowel)
                if vowel_counter >= 3:
                    naughty = False
                    break
            if naughty:
                print(f"{word} is naughty because vowels")
                continue

            naughty = True
            for first, second in zip(word[1:], word[:-1]):
                if first == second:
                    naughty = False
                    break
            if naughty:
                print(f"{word} is naughty because doubles")
                continue

            print(f"{word} is nice")
            nice_word_count += 1

    print(nice_word_count)



def day5_pt2(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    nice_word_count = 0
    with input_file_path.open("r") as input_file:
        for word in input_file:
            pairs = [first + second for first, second in zip(word[1:], word[:-1])]
            naughty = True
            for pos, pair in enumerate(pairs):
                temp_list = (pairs[:pos-1] + pairs[pos+2:])
                print(pairs, temp_list, pair)
                if pair in temp_list:
                    naughty = False
                    break
            if naughty:
                print(f"{word} is naughty because no pair")
                continue


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day5_pt2(working_dir)
