from pathlib import Path
from operator import add

def day3_pt1(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    data = input_file_path.read_text()
    direction_mapping: dict[str, tuple[int, int]] = {
        "^": (0, 1),
        "v": (0, -1),
        ">": (1, 0),
        "<": (-1, 0),
    }

    houses_visited: set[tuple[int, int]] = set()
    pos: tuple[int, int] = (0, 0)
    houses_visited.add(pos)
    for direction in data:
        moved = direction_mapping[direction]
        pos = tuple(map(add, moved, pos))
        houses_visited.add(pos)
    print(len(houses_visited))

def day3_pt2(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    data = input_file_path.read_text()
    direction_mapping: dict[str, tuple[int, int]] = {
        "^": (0, 1),
        "v": (0, -1),
        ">": (1, 0),
        "<": (-1, 0),
    }

    houses_visited: set[tuple[int, int]] = set()
    pos: tuple[int, int] = (0, 0)
    robo_pos: tuple[int, int] = (0, 0)
    houses_visited.add(pos)
    robo: bool = False
    for direction in data:
        moved = direction_mapping[direction]
        if robo:
            robo_pos = tuple(map(add, moved, robo_pos))
            houses_visited.add(robo_pos)
            robo = False
        else:
            pos = tuple(map(add, moved, pos))
            houses_visited.add(pos)
            robo = True
    print(len(houses_visited))

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day3_pt2(working_dir)