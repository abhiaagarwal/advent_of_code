from pathlib import Path
import re
from collections import defaultdict
import math

def day2_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    sum = 0
    with input_file_dir.open('r') as input_file:
        for line in input_file:
            game, values = line.split(": ")
            for round in values.split("; "):
                result = {color_value_split[1]: int(color_value_split[0]) for pair in round.split(', ') if (color_value_split := pair.split())}
                for color, limit in limits.items():
                    value = result.get(color, 0)
                    if value > limit:
                        #print(f"{result} is not valid")
                        break
                else:
                    continue
                break
            else:
                game_num = int(game.split(" ")[1])
                #print(f"game {game_num} is valid")
                sum += game_num
    
    print(sum)

def day2_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    value_regex = re.compile(r'(\d+) (\w+)')

    sum = 0
    with input_file_dir.open('r') as input_file:
        for line in input_file:
            _, values = line.split(": ")
            result_dict: defaultdict[str, list[int]] = defaultdict(list)

            matches = re.findall(value_regex, values)
            for value, color in matches:
                result_dict[color].append(int(value))
            
            val = math.prod([max(item) for item in result_dict.values()])
            sum += val
    
    print(sum)

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day2_pt2(working_dir)