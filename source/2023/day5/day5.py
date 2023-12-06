from functools import cache
from pathlib import Path
from typing import Self, NamedTuple
from dataclasses import dataclass, field
from itertools import pairwise
from pprint import pprint

class Map(NamedTuple):
    destination: int
    source: int
    range: int

    def go_to_next(self: Self, location: int) -> int | None:
        if self.source <= location and location <= self.source + self.range - 1:
            return (location - self.source) + self.destination
        return None

@dataclass
class CachedMapper:
    mappers: list[list[Map]]
    _cache: dict[tuple[int, int], int] = field(default_factory=dict)

    def get_seed_final_location(self: Self, seed: int) -> int:
        print(f"seed {seed}")
        new_location = seed
        past_res: list[tuple[int, int]] = []
        for level_num, level in enumerate(self.mappers):
            if final_location := self._cache.get((level_num, new_location), None):
                print(f"!!!hit!!!, found {seed} in cache at level {level_num} with value {final_location} \n")
                return final_location
            else:
                #print(f"can't find {seed} in cache at level {level_num}")
                pass
            for map in level:
                potential_val = map.go_to_next(new_location)
                if potential_val is not None:
                    new_location = potential_val
                    break
            #[][awse=-print(f"at level {level_num}, {seed} is {new_location}")
        self._cache.update(
            {res: new_location for res in past_res}
        )
        #print(f"final location for seed {seed} is {new_location}")
        #print(f"cache is now {self._cache}")
        #print("\n")
        return new_location

def day5_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    seeds: list[int] = []
    cached_mapper: CachedMapper

    with input_file_dir.open("r") as input_file:
        mappers: list[list[Map]] = []
        temp_mappers: list[Map] = []
        collecting: bool = False
        for line in input_file:
            try:
                if "seeds" in line:
                    seeds = [int(seed) for seed in line[6:].split()]
                elif "map" in line:
                    collecting = True
                elif line == "\n":
                    collecting = False
                    mappers.append(temp_mappers.copy())
                    temp_mappers.clear()
                elif collecting:
                    temp_mappers.append(Map(*[int(line) for line in line.split()])) # type: ignore
            except Exception:
                print(line)
                break
        mappers.append(temp_mappers.copy())
        mappers.pop(0)
        cached_mapper = CachedMapper(mappers=mappers)

    final_locations: list[int] = []
    for seed in seeds:
        new_location = cached_mapper.get_seed_final_location(seed)
        final_locations.append(new_location)

    print(min(final_locations))


def day5_pt2(working_dir: Path) -> None:
    input_file_dir = working_dir / "input.txt"
    seeds: list[int] = []
    cached_mapper: CachedMapper

    with input_file_dir.open("r") as input_file:
        mappers: list[list[Map]] = []
        temp_mappers: list[Map] = []
        collecting: bool = False
        for line in input_file:
            try:
                if "seeds" in line:
                    seeds = [int(seed) for seed in line[6:].split()]
                elif "map" in line:
                    collecting = True
                elif line == "\n":
                    collecting = False
                    mappers.append(temp_mappers.copy())
                    temp_mappers.clear()
                elif collecting:
                    temp_mappers.append(Map(*[int(line) for line in line.split()])) # type: ignore
            except Exception:
                print(line)
                break
        mappers.append(temp_mappers.copy())
        mappers.pop(0)
        cached_mapper = CachedMapper(mappers)


    final_locations: list[int] = []
    for starting_seed, range_val in list(pairwise(seeds))[::2]:
        for diff in range(0, range_val):
            seed: int = starting_seed + diff
            new_location = cached_mapper.get_seed_final_location(seed)
            final_locations.append(new_location)
            
    print(min(final_locations))


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day5_pt2(working_dir)
