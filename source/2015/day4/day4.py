from pathlib import Path

import hashlib

def day4_pt1(working_dir: Path) -> None:
    secret_val = "yzbqklnj"
    for val in range(100000, 999999 + 1):
        new_val = secret_val + str(val)
        md5 = hashlib.md5(new_val.encode()).hexdigest()
        if md5.startswith("00000"):
            print(val)
            break

def day4_pt2(working_dir: Path) -> None:
    secret_val = "yzbqklnj"
    for val in range(1000000, 9999999 + 1):
        new_val = secret_val + str(val)
        md5 = hashlib.md5(new_val.encode()).hexdigest()
        if md5.startswith("000000"):
            print(val)
            break

if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day4_pt2(working_dir)