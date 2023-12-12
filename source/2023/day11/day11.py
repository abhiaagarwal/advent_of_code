from pathlib import Path
import re
from itertools import combinations


def day11_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    galaxies: set[tuple[int, tuple[int, int]]] = set()
    empty_rows: set[int] = set()
    counter: int = 1
    with input_file_dir.open("r") as input_file:
        for y, line in enumerate(input_file):
            matches = list(re.finditer("#", line))
            if not matches:
                empty_rows.add(y)
            else:
                for match in matches:
                    galaxies.add((counter, (match.start(), y)))
                    counter += 1

    LENGTH_OF_LINE: int = 140
    empty_columns: set[int] = set(range(LENGTH_OF_LINE)).difference(
        {galaxy[1][0] for galaxy in galaxies}
    )

    sum: int = 0
    for (gal_1, (x_l, y_l)), (gal_2, (x_r, y_r)) in combinations(galaxies, 2):
        skipped_rows = [
            empty_row
            for empty_row in empty_rows
            if min(y_l, y_r) < empty_row < max(y_r, y_l)
        ]
        skipped_columns = [
            empty_column
            for empty_column in empty_columns
            if min(x_l, x_r) < empty_column < max(x_r, x_l)
        ]

        diff = (
            abs(x_l - x_r) + abs(y_l - y_r) + len(skipped_rows) + len(skipped_columns)
        )
        print(gal_1, (x_l, y_l), gal_2, (x_r, y_r), skipped_rows, skipped_columns, diff)
        sum += diff

    print(sum)


def day11_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "known_input.txt"

    galaxies: set[tuple[int, tuple[int, int]]] = set()
    empty_rows: set[int] = set()
    counter: int = 1
    with input_file_dir.open("r") as input_file:
        for y, line in enumerate(input_file):
            matches = list(re.finditer("#", line))
            if not matches:
                empty_rows.add(y)
            else:
                for match in matches:
                    galaxies.add((counter, (match.start(), y)))
                    counter += 1

    LENGTH_OF_LINE: int = 10
    empty_columns: set[int] = set(range(LENGTH_OF_LINE)).difference(
        {galaxy[1][0] for galaxy in galaxies}
    )

    sum: int = 0
    for (gal_1, (x_l, y_l)), (gal_2, (x_r, y_r)) in combinations(galaxies, 2):
        skipped_rows = [
            empty_row
            for empty_row in empty_rows
            if min(y_l, y_r) < empty_row < max(y_r, y_l)
        ]
        skipped_columns = [
            empty_column
            for empty_column in empty_columns
            if min(x_l, x_r) < empty_column < max(x_r, x_l)
        ]

        diff = (
            abs(x_l - x_r) + abs(y_l - y_r) + (len(skipped_rows) + len(skipped_columns)) * (99)
        )
        print(gal_1, (x_l, y_l), gal_2, (x_r, y_r), skipped_rows, skipped_columns, diff)
        sum += diff

    print(sum)


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day11_pt2(working_dir)
