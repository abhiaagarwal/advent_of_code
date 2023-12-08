from pathlib import Path
from math import lcm

from itertools import repeat


def day8_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    directions: str
    camel_map: dict[str, tuple[str, str]] = {}
    with input_file_dir.open("r") as input_file:
        for index, line in enumerate(input_file):
            if index == 0:
                directions = line.strip()
                continue
            elif index == 1:
                continue

            start, finish = line.split(" = ")
            camel_map[start] = tuple(finish.strip()[1:-1].split(", "))

    print(camel_map)

    final_step: int = 0
    starting_location: str = "AAA"
    new_location = starting_location
    for step, direction in enumerate(char for rep in repeat(directions) for char in rep):
        index = 0 if direction == "L" else 1
        new_location = camel_map[new_location][index]
        if new_location == "ZZZ":
            final_step = step + 1
            break

    print(final_step)

def day8_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    directions: str
    camel_map: dict[str, tuple[str, str]] = {}
    with input_file_dir.open("r") as input_file:
        for index, line in enumerate(input_file):
            if index == 0:
                directions = line.strip()
                continue
            elif index == 1:
                continue

            start, finish = line.split(" = ")
            camel_map[start] = tuple(finish.strip()[1:-1].split(", "))

    starting_locations = [start for start in camel_map.keys() if start.endswith("A")]
    new_locations = starting_locations.copy()
    rotation_stop: list[int] = []
    for step, direction in enumerate(char for rep in repeat(directions) for char in rep):
        index = 0 if direction == "L" else 1

        temp_list: list[str] = []
        while new_locations:
            location = new_locations.pop()
            new_location = camel_map[location][index]
            if new_location.endswith("Z"):
                rotation_stop.append(step + 1)
            else:
                temp_list.append(new_location)

        if temp_list:
            new_locations = temp_list[:]
        else:
            break

    print(lcm(*rotation_stop))

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day8_pt2(working_dir)
