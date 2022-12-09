import os
import sys

class Knot:
    def __init__(self, parent):
        self.parent = parent
        self.pos = [0,0]
        self.visitedPositions = set()
        self.visitedPositions.add((0,0))

    def isHead(self):
        return self.parent == None
    
    def move(self, dir: str, track: bool = True):
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
        if track:
            self.visitedPositions.add((self.pos[0], self.pos[1]))

    def adapt_from_parent(self):
        if(self.parent == None):
            return
        _distance = [self.parent.pos[0] - self.pos[0], self.parent.pos[1] - self.pos[1]]
        if abs(_distance[0]) < 2 and abs(_distance[1]) < 2:
            return
        if abs(_distance[0]) > 1 and _distance[1] == 0: # horizontal movement
            _direction = 'R' if _distance[0] > 0 else 'L'
            self.move(_direction)
        elif abs(_distance[1]) > 1 and _distance[0] == 0: # vertical movement
            _direction = 'U' if _distance[1] > 0 else 'D'
            self.move(_direction)
        else: # Diagonal
            _horizontalDirection = 'R' if _distance[0] > 0 else 'L'
            _verticalDirection = 'U' if _distance[1] > 0 else 'D'
            self.move(_horizontalDirection, track=False)
            self.move(_verticalDirection, track=True)


def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _head = Knot(parent=None)
    _tail = Knot(parent=_head)

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

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _parent = None
    _knots = []
    for _knotIndex in range(10):
        _knots.append(Knot(parent=_parent))
        _parent = _knots[-1]

    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            _direction, _amount =  _line.split(" ")
            _amount = int(_amount)
            while _amount > 0:
                _amount -= 1
                _knots[0].move(_direction)
                for _knotIndex in range(1,10):
                    _knots[_knotIndex].adapt_from_parent()
                
    print(f"Number of visited positions: {len(_knots[-1].visitedPositions)}")

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)

