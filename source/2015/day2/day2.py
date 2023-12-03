from pathlib import Path
import math

def day2_pt1(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    sum = 0
    with input_file_path.open("r") as input_file:
        for line in input_file:
            dims = [int(val) for val in line.split("x")]
            a1 = dims[0] * dims[1]
            a2 = dims[0] * dims[2]
            a3 = dims[1] * dims[2]
            square_feet = 2 * (a1 + a2 + a3) + min(a1, a2, a3)
            sum += square_feet
    print(sum)

def day2_pt2(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    sum = 0
    with input_file_path.open("r") as input_file:
        for line in input_file:
            dims = [int(val) for val in line.split("x")]
            dims.sort()
            smallest_perimeter = 2 * (dims[0] + dims[1])
            volume = math.prod(dims)
            sum += volume + smallest_perimeter
    print(sum)

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day2_pt2(working_dir)