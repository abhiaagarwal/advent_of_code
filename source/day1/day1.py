from typing import *
import os
import pandas as pd
from pandas.core.window import rolling 

def day1() -> None:
    def count(lines: pd.Series) -> int:
        increasing: int = 0
        for index in range(1, len(lines)):
            beginning_element: int = lines[index - 1]
            next_element: int = lines[index]
            if next_element > beginning_element:
                increasing += 1
        return increasing

    with open('input.txt') as input:
        input_lines: List[int] = [int(line) for line in input.readlines()]

    lines: pd.Series = pd.Series(input_lines)
    rolling_sum: pd.Series = lines.rolling(3).sum()

    raw_increasing = count(input_lines)
    rolling_increasing = count(rolling_sum)

    print(raw_increasing)
    print(rolling_increasing)
    
    return None

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    day1()