import copy
import os
import sys

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _currentHeadPos = [0,0]
    _previousHeadPos = [-1,-1]
    _currentTailPos = [0,0]
    _visitedPositions = set()
    _visitedPositions.add((0,0))
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            _direction, _amount =  _line.split(" ")
            _amount = int(_amount)
            while _amount > 0:
                _amount -= 1
                _previousHeadPos = copy.deepcopy(_currentHeadPos)
                if _direction == 'L':
                    _currentHeadPos[0] -= 1
                elif _direction == 'R':
                    _currentHeadPos[0] += 1
                elif _direction == 'U':
                    _currentHeadPos[1] += 1
                elif _direction == 'D':
                    _currentHeadPos[1] -= 1
                else:
                    assert False, f"Unknown direction{_direction}"
                # Adapt the tail position
                _distance = [_currentHeadPos[0] - _currentTailPos[0], _currentHeadPos[1] - _currentTailPos[1]]
                _squareDistance = [pow(_distance[0],2), pow(_distance[1],2)]
                if _squareDistance[0] > 1 or _squareDistance[1] > 1:
                    _currentTailPos = copy.deepcopy(_previousHeadPos)
                    _visitedPositions.add((_currentTailPos[0], _currentTailPos[1]))

                
    print(f"Number of visited positions: {len(_visitedPositions)}")

if __name__ == '__main__':
    # solve_part_1()
    solve_part_1()
    sys.exit(0)

