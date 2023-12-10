from pathlib import Path

from itertools import pairwise


def day9_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    sum: int = 0
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            vals = [int(num) for num in line.split()]
            diffs_list: list[list[int]] = [vals]
            while True:
                last_diffs = diffs_list[-1]
                diffs = [y-x for (x, y) in pairwise(last_diffs)]
                if all(diff == 0 for diff in diffs):
                    break
                diffs_list.append(diffs)
            
            last_val: int = 0
            while diffs_list:
                last_val += diffs_list.pop()[-1]
            sum += last_val

    print(sum)

def day9_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    sum: int = 0
    with input_file_dir.open("r") as input_file:
        for line in input_file:
            vals = [int(num) for num in line.split()]
            vals.reverse()
            diffs_list: list[list[int]] = [vals]
            while True:
                last_diffs = diffs_list[-1]
                diffs = [y-x for (x, y) in pairwise(last_diffs)]
                if all(diff == 0 for diff in diffs):
                    break
                diffs_list.append(diffs)
            
            last_val: int = 0
            while diffs_list:
                last_val += diffs_list.pop()[-1]
            sum += last_val

    print(sum)

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day9_pt2(working_dir)
