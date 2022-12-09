import copy
from email import header
import os
import sys

class Knot:
    def __init__(self, parent):
        self.parent = parent
        self.previousPos = [0,0]
        self.pos = [0,0]
        self.visitedPositions = set()
        self.visitedPositions.add((0,0))

    def isHead(self):
        return self.parent == None
    
    def move(self, dir: str):
        self.previousPos = copy.deepcopy(self.pos)
        if dir == 'L':
            self.pos[0] -= 1
        elif dir == 'R':
            self.pos[0] += 1
        elif dir == 'U':
            self.pos[1] += 1
        elif dir == 'D':
            self.pos[1] -= 1
        else:
            assert False, f"Unknown direction{dir}"
    
    def adapt_from_parent(self):
        if(self.parent == None):
            return
        _distance = [self.parent.pos[0] - self.pos[0], self.parent.pos[1] - self.pos[1]]
        _squareDistance = [pow(_distance[0],2), pow(_distance[1],2)]
        if _squareDistance[0] > 1 or _squareDistance[1] > 1:
            self.pos = copy.deepcopy(self.parent.previousPos)
            self.visitedPositions.add((self.pos[0], self.pos[1]))


def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _head = Knot(parent=None)
    _tail = Knot(parent=_head)

    _visitedPositions = set()
    _visitedPositions.add((0,0))
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            _direction, _amount =  _line.split(" ")
            _amount = int(_amount)
            while _amount > 0:
                _amount -= 1
                _head.move(_direction)
                _tail.adapt_from_parent()
                
    print(f"Number of visited positions: {len(_tail.visitedPositions)}")

if __name__ == '__main__':
    # solve_part_1()
    solve_part_1()
    sys.exit(0)

