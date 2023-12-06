from math import ceil, sqrt, floor
from pathlib import Path


def quadratic_formula(a: int, b: int, c: int) -> tuple[float, float]:
    discriminant = sqrt(b**2 - 4 * a * c)
    return ((-b + discriminant) / (2 * a), (-b - discriminant) / (2 * a))


def day6_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    data = [
        [int(val) for val in line[11:].split()]
        for line in input_file_dir.read_text().splitlines()
    ]
    races: list[tuple[int, int]] = list(zip(*data))

    product: int = 1
    for race in races:
        # (distance - time) * t >= limit
        # (d - t) * t - l >= 0
        # -1 * t^2 + d * t + (-l) >= 0
        lower_bound, upper_bound = quadratic_formula(-1, race[0], -(race[1] + 1))
        cor_lower = ceil(lower_bound)
        cor_upper = floor(upper_bound)
        ways_to_win = cor_upper - cor_lower + 1
        product *= ways_to_win

    print(product)


def day6_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    race: tuple[int, int] = tuple(
        [
            int("".join(line[11:].split()))
            for line in input_file_dir.read_text().splitlines()
        ]
    )  # type: ignore

    lower_bound, upper_bound = quadratic_formula(-1, race[0], -(race[1] + 1))
    cor_lower = ceil(lower_bound)
    cor_upper = floor(upper_bound)
    ways_to_win = cor_upper - cor_lower + 1

    print(ways_to_win)


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day6_pt2(working_dir)
