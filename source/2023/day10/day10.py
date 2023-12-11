from operator import add
from pathlib import Path

def tuple_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(add, a, b))

def day10_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    pipe_map = [list(line) for line in input_file_dir.read_text().splitlines()]

    pipes: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
        "|": ((0, -1), (0, 1)),
        "-": ((-1, 0), (1, 0)),
        "L": ((0, 1), (1, 0)),
        "J": ((0, 1), (-1, 0)),
        "7": ((0, -1), (-1, 0)),
        "F": ((0, -1), (1, 0)),
    }

    directions: set[tuple[int, int]] = {
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    }

    print(pipe_map)

    starting_point: tuple[int, int]
    for y, row in enumerate(pipe_map):
        try:
            x = row.index("S")
            starting_point = (x, y)
            break
        except ValueError:
            pass

    assert starting_point
    walk_1: set[tuple[int, int]] = set()
    walk_1_pos = starting_point
    walk_2: set[tuple[int, int]] = set()
    walk_2_pos = starting_point

    while not walk_1.intersection(walk_2):
        for walk, pos in [(walk_1, walk_1_pos), (walk_2, walk_2_pos)]:
            for direction in directions:
                x, y = tuple_add(pos, direction)
                pipe_dir = pipes.get(pipe_map[y][x], None)
                if pipe_dir is None:
                    continue
                print(direction, pipe_dir)
                for item in pipe_dir:
                    if item == direction and item not in walk_1.union(walk_2):
                        
            break
        break


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day10_pt1(working_dir)
