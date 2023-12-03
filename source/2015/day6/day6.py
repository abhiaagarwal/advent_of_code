from pathlib import Path

import re


def day6_pt1(working_dir: Path) -> None:
    input_file_path: Path = working_dir / "input.txt"
    LENGTH = 1000
    HEIGHT = 1000

    bitfield = [False] * LENGTH * HEIGHT

    pattern = re.compile(r"(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)")
    with input_file_path.open("r") as input_file:
        for line in input_file:
            match = pattern.match(line)
            assert match is not None
            command = str(match.group(1))

            start_x = int(match.group(2))
            start_y = int(match.group(3))

            end_x = int(match.group(4))
            end_y = int(match.group(5))

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    actual_pos = y * LENGTH + x
                    if command == "toggle":
                        bitfield[actual_pos] = not bitfield[actual_pos]
                    elif command == "turn on":
                        bitfield[actual_pos] = True
                    elif command == "turn off":
                        bitfield[actual_pos] = False

    print(sum(bitfield))


def day6_pt2(working_dir: Path) -> None:
    input_file_path: Path = working_dir / "input.txt"
    LENGTH = 1000
    HEIGHT = 1000

    brightness = [0] * LENGTH * HEIGHT

    pattern = re.compile(r"(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)")
    with input_file_path.open("r") as input_file:
        for line in input_file:
            match = pattern.match(line)
            assert match is not None
            command = str(match.group(1))

            start_x = int(match.group(2))
            start_y = int(match.group(3))

            end_x = int(match.group(4))
            end_y = int(match.group(5))

            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    actual_pos = y * LENGTH + x
                    if command == "toggle":
                        brightness[actual_pos] += 2
                    elif command == "turn on":
                        brightness[actual_pos] += 1
                    elif command == "turn off":
                        if brightness[actual_pos] == 0:
                            continue
                        brightness[actual_pos] -= 1

    print(sum(brightness))


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day6_pt2(working_dir)
