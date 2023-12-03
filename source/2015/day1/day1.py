from pathlib import Path

def day1_pt1(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    data = input_file_path.read_text()
    up = data.count("(")
    down = data.count(")")
    diff = up-down
    print(diff)

def day1_pt2(working_dir: Path) -> None:
    input_file_path = working_dir / "input.txt"
    data = input_file_path.read_text()

    level: int = 0
    for count, char in enumerate(data):
        if char == "(":
            level = level + 1
        elif char == ")":
            level = level - 1
        
        if level < 0:
            print(count + 1)
            break

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day1_pt2(working_dir)