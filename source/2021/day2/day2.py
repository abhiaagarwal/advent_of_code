from typing import *
import os
import pandas as pd

def day2() -> None:
    with open('input.txt') as input:
        df_directions: pd.DataFrame = pd.read_csv(input, sep = ' ', header = None)
        df_directions.columns = ["direction", "value"]

    grouped_df = df_directions.groupby(["direction"])["value"].sum()
    raw_value: int = (-grouped_df["up"] + grouped_df["down"]) * grouped_df["forward"]
    print(raw_value)

    aim = 0
    depth = 0
    horiz = 0
    for direction, value in df_directions.itertuples(index = False):
        if direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        elif direction == "forward":
            horiz += value
            depth += aim * value
        else:
            pass
    aimed_value = depth * horiz
    print(aimed_value)
    return None

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    day2()