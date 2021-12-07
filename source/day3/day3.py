from typing import *
import os
import pandas as pd
from pandas.core.window import rolling 

def day3() -> None:
    with open('input.txt') as input:
        df_code: pd.DataFrame = pd.read_csv(input, header = None, dtype = str)
        df_code = df_code[0].apply(lambda x: pd.Series(list(x)))
    mode_code: str = df_code.mode().apply(lambda row: ''.join(row.values), axis = 1)[0]
    invert_mode_code: str = ''.join(['1' if i == '0' else '0' for i in mode_code])
    print(mode_code)

    gamma = int(mode_code, 2)
    epsilon = int(invert_mode_code, 2)
    raw_value = gamma * epsilon
    print(raw_value)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    day3()