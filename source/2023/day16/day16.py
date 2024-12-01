from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from enum import Enum
from abc import ABC, abstractmethod
from operator import add
from collections import deque


def tuple_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return tuple(map(add, a, b))


@dataclass(frozen=True)
class Reflector(ABC):
    pos: tuple[int, int]

    @abstractmethod
    def reflect(self, beam: Beam) -> set[Beam]:
        pass


@dataclass(frozen=True)
class Mirror(Reflector):
    ne: bool  # true "/" false "\"

    def reflect(self, beam: Beam) -> set[Beam]:
        if self.ne:  # /
            direction_map = {
                Direction.RIGHT: Direction.DOWN,
                Direction.DOWN: Direction.RIGHT,
                Direction.LEFT: Direction.UP,
                Direction.UP: Direction.LEFT,
            }
        else:  # \
            direction_map = {
                Direction.RIGHT: Direction.UP,
                Direction.UP: Direction.RIGHT,
                Direction.LEFT: Direction.DOWN,
                Direction.DOWN: Direction.LEFT,
            }
        new_direction = direction_map[beam.direction]
        return {Beam(new_direction, tuple_add(beam.pos, new_direction.value))}


@dataclass(frozen=True)
class Splitter(Reflector):
    horizontal: bool

    def reflect(self, beam: Beam) -> set[Beam]:
        if self.horizontal:  # -
            direction_map = {
                Direction.RIGHT: {Direction.RIGHT},
                Direction.DOWN: {Direction.RIGHT, Direction.LEFT},
                Direction.LEFT: {Direction.LEFT},
                Direction.UP: {Direction.RIGHT, Direction.LEFT},
            }
        else:  # |
            direction_map = {
                Direction.RIGHT: {Direction.UP, Direction.DOWN},
                Direction.DOWN: {Direction.DOWN},
                Direction.LEFT: {Direction.UP, Direction.DOWN},
                Direction.UP: {Direction.UP},
            }
        new_directions = direction_map[beam.direction]
        return {
            Beam(new_direction, tuple_add(beam.pos, new_direction.value))
            for new_direction in new_directions
        }


class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    UP = (0, -1)


@dataclass(frozen=True)
class Beam:
    direction: Direction
    pos: tuple[int, int]


def day16_pt1(working_dir: Path) -> None:
    input_file_dir = working_dir / "known_input.txt"

    reflectors: set[Reflector] = set()

    height: int = 0
    width: int = 0
    with input_file_dir.open("r") as input_file:
        for y, line in enumerate(input_file):
            if width == 0:
                width = len(line) - 1
            reflectors.update(
                [
                    Mirror(ne=True, pos=(match.start(), y))
                    for match in re.finditer(r"\/", line)
                ]
            )
            reflectors.update(
                [
                    Mirror(ne=False, pos=(match.start(), y))
                    for match in re.finditer(r"\\", line)
                ]
            )
            reflectors.update(
                [
                    Splitter(horizontal=True, pos=(match.start(), y))
                    for match in re.finditer(r"\-", line)
                ]
            )
            reflectors.update(
                [
                    Splitter(horizontal=False, pos=(match.start(), y))
                    for match in re.finditer(r"\|", line)
                ]
            )
            height = y

    def in_bounds(pos: tuple[int, int]) -> bool:
        return (0 <= pos[0] <= width) and (0 <= pos[1] <= height)

    beams: deque[Beam] = deque([Beam(Direction.RIGHT, (0, 0))])
    visited: set[tuple[int, int]] = set()
    while beams:
        print(beams)
        visited.update(beam.pos for beam in beams)
        beam = beams.popleft()

        reflector = next((reflector for reflector in reflectors if reflector.pos == beam.pos), None) # guaranteed to only be one
        new_beams: set[Beam] = set()
        if reflector is None:
            potential_pos = tuple_add(beam.pos, beam.direction.value)
            if in_bounds(potential_pos):
                new_beams.add(Beam(beam.direction, potential_pos))
        else:
            new_beams.update({beam for beam in reflector.reflect(beam) if in_bounds(beam.pos)})
        beams.extend(new_beams)

    print(visited)

def day16_pt2(working_dir: Path) -> None:
    return


if __name__ == "__main__":
    working_dir = Path(__file__).parent
    day16_pt1(working_dir)
