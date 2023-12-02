from pathlib import Path
import re
from unicodedata import digit

from polars import last

def day1_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    digit_pattern = re.compile(r"\d")

    sum = 0
    with input_file_dir.open('r') as input_file:
        for line in input_file:
            digits: list[str] = re.findall(digit_pattern, line)
            sum += int(digits[0] + digits[-1])
            
    print(sum)

def day1_pt2(working_dir: Path) -> None:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    regex_pattern = rf"(?=(\d|{'|'.join(number_map.keys())}))"
    print(regex_pattern)
    digit_pattern = re.compile(regex_pattern)

    total_sum = 0
    input_file_dir = working_dir / "input.txt"
    with input_file_dir.open('r') as input_file:
        for line in input_file:
            digits: list[str] = re.findall(digit_pattern, line)
            first_digit = digits[0]
            if first_digit in number_map:
                first_digit = number_map[first_digit]
            last_digit = digits[-1]
            if last_digit in number_map:
                last_digit = number_map[last_digit]

            sum = int(first_digit + last_digit)
            total_sum += sum
            
    print(total_sum)

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day1_pt2(working_dir)