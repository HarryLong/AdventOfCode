import argparse
import os
import sys

def get_intersection(inInput : list[str]) -> set[str]:
    _intersection = set(inInput[0])
    for _list in inInput[1:]:
        _intersection &= set(_list) 
    return _intersection

def get_priority(inInput1: str) -> int:
    if inInput1.islower():
        return ord(inInput1) - ord('a') + 1
    return ord(inInput1) - ord('A') + 27

def solve_part_1(input: str):
    _intersectionPriority = 0
    with open(input) as f:
        for _line in f:
            _line = _line.rstrip()
            _halfLen = int(len(_line)/2)
            _compartment1 = _line[:_halfLen]
            _compartment2 = _line[_halfLen:]
            _intersection = get_intersection([_compartment1, _compartment2])
            assert len(_intersection) == 1, _intersection
            _intersectionPriority += get_priority(_intersection.pop())
    print(f"Total priority: {_intersectionPriority}")

def solve_part_2(input: str):
    _combinedPack = []
    _badgePrioritySum = 0
    with open(input) as f:
        for _line in f:
            _line = _line.rstrip()
            _combinedPack.append(_line)
            if len(_combinedPack) == 3:
                _intersection = get_intersection(_combinedPack)
                assert len(_intersection) == 1, _intersection
                _badgePrioritySum += get_priority(_intersection.pop())
                _combinedPack = []
    print(f"Total priority: {_badgePrioritySum}")

if __name__ == '__main__':
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    # solve_part_1(_input)
    solve_part_2(_input)

    sys.exit(0)

