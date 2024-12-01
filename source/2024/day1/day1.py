from pathlib import Path
from collections import Counter


def day1_pt1(working_dir: Path) -> None:
    left, right = [
        list(l)
        for l in zip(
            *[
                [int(val) for val in line.split()]
                for line in (working_dir / "input.txt").read_text().splitlines()
            ]
        )
    ]
    left.sort()
    right.sort()
    diff_sum = sum([abs(l - r) for l, r in zip(left, right)])
    print(diff_sum)


def day1_pt2(working_dir: Path) -> None:
    left, right = [
        Counter(l)
        for l in zip(
            *[
                [int(val) for val in line.split()]
                for line in (working_dir / "input.txt").read_text().splitlines()
            ]
        )
    ]

    key_sum = sum(
        [right.get(key, 0) * key * item for key, item in left.items()]
    )
    print(key_sum)


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day1_pt1(working_dir)
    day1_pt2(working_dir)
