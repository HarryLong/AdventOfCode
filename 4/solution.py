import argparse
import os
import sys

def is_fully_contained(inRange1 : list[str], inRange2 : list[str]):
    return (int(inRange1[0]) >= int(inRange2[0]) and int(inRange1[1]) <= int(inRange2[1])) or\
         (int(inRange2[0]) >= int(inRange1[0]) and int(inRange2[1]) <= int(inRange1[1]))

def is_overlapping(inRange1 : list[str], inRange2 : list[str]):
    return (int(inRange1[0]) >= int(inRange2[0]) and int(inRange1[0]) <= int(inRange2[1])) or\
         (int(inRange2[0]) >= int(inRange1[0]) and int(inRange2[0]) <= int(inRange1[1]))

def solve_part_1(input: str):
    _fullyContainedCounter = 0
    with open(input) as f:
        for _line in f:
            _line = _line.rstrip()
            _rangeSplit = _line.split(',')
            _range1 = _rangeSplit[0].split('-')
            _range2 = _rangeSplit[1].split('-')
            assert len(_range1) == len(_range2) == 2, f"Expected 2 values in range"
            if is_fully_contained(_range1, _range2):
                _fullyContainedCounter += 1

    print(f"Number of overlaps: {_fullyContainedCounter}")

def solve_part_2(input: str):
    _overlappingCounter = 0
    with open(input) as f:
        for _line in f:
            _line = _line.rstrip()
            _rangeSplit = _line.split(',')
            _range1 = _rangeSplit[0].split('-')
            _range2 = _rangeSplit[1].split('-')
            assert len(_range1) == len(_range2) == 2, f"Expected 2 values in range"
            if is_overlapping(_range1, _range2):
                print(f"Overlapping: {_range1} and {_range2}")
                _overlappingCounter += 1

    print(f"Number of overlaps: {_overlappingCounter}")


if __name__ == '__main__':
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    # solve_part_1(_input)
    solve_part_2(_input)

    sys.exit(0)

