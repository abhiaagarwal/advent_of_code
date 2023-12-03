from pathlib import Path
import re


def day3_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    data = "".join(input_file_dir.read_text().splitlines())

    LINE_LENGTH: int = 140

    digit_locations: dict[tuple[int, int], int] = {}
    digit_regex = re.compile(r"\d+")
    for match in re.finditer(digit_regex, data):
        start, stop = match.span()
        digit_locations[(start, stop - 1)] = int(match.group(0))

    print(digit_locations)

    PARTS = {"$", "*", "=", "@", "/", "-", "+", "%", "&", "#"}
    part_positions: set[int] = set()
    for pos, char in enumerate(data):
        if char in PARTS:
            print(f"found {char} at ({pos})")
            part_positions.add(pos)

    directions: set[int] = {
        -(LINE_LENGTH + 1),  # above left
        -(LINE_LENGTH),  # above
        -(LINE_LENGTH - 1),  # above right
        -1,  # left
        1,  # right
        (LINE_LENGTH - 1),  # bottom left
        (LINE_LENGTH),  # bottom
        (LINE_LENGTH + 1),  # bottom right
    }
    sum: int = 0
    for position in part_positions:
        for direction in directions:
            for start, end in list(digit_locations.keys()):
                if start <= position + direction and position + direction <= end:
                    value = digit_locations.pop((start, end))
                    print(f"found {value} at start {start} and stop {end}")
                    sum += value
                    continue

    print(f"digit locations not found {digit_locations}")
    print(f"sum {sum}")


def day3_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    data = "".join(input_file_dir.read_text().splitlines())

    LINE_LENGTH: int = 140

    digit_locations: dict[tuple[int, int], int] = {}
    digit_regex = re.compile(r"\d+")
    for match in re.finditer(digit_regex, data):
        start, stop = match.span()
        digit_locations[(start, stop - 1)] = int(match.group(0))

    GEAR_SYMBOL: str = "*"
    gear_positions: set[int] = set()
    for pos, char in enumerate(data):
        if char == GEAR_SYMBOL:
            gear_positions.add(pos)

    directions: set[int] = {
        -(LINE_LENGTH + 1),  # above left
        -(LINE_LENGTH),  # above
        -(LINE_LENGTH - 1),  # above right
        -1,  # left
        1,  # right
        (LINE_LENGTH - 1),  # bottom left
        (LINE_LENGTH),  # bottom
        (LINE_LENGTH + 1),  # bottom right
    }

    sum: int = 0
    for position in gear_positions:
        matches: set[tuple[int, int]] = set()
        for direction in directions:
            for start, end in list(digit_locations.keys()):
                if start <= position + direction and position + direction <= end:
                    matches.add((start, end))
        print(f"for gear {position}, matches found {matches}")
        if len(matches) == 2:
            list_matches = list(matches)
            sum += digit_locations[list_matches[0]] * digit_locations[list_matches[1]]

    print(sum)


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day3_pt2(working_dir)
