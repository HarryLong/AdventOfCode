import copy
from itertools import repeat
import os
import sys
from threading import Thread
import cProfile

_START = 'S'
_DESTINATION = 'E'

class Path:
    def __init__(self):
        self.path = []
        self.reached_destination = False

    def add(self, position: list[int]):
        self.path.append([position[0], position[1]])
    
    def steps(self):
        return len(self.path) - 1 # Start position isn't a move

class PathFinder:
    def __init__(self, heightmap: list[str]):
        self.currentMin = sys.maxsize
        self.heightmap = []
        self.start = [-1,-1]
        self.destination = [-1,-1]
        self.deadends = set()
        _row = 0
        for _line in heightmap:
            self.heightmap.append([])
            _column = 0
            for _char in _line.strip():
                if _char == _START:
                    self.start = [_row, _column]
                if _char == _DESTINATION:
                    self.destination = [_row, _column]
                self.heightmap[-1].append(_char)
                _column += 1
            _row += 1
        assert self.start[0] != -1 and self.destination[0] != -1, "Should not happen"

    def inRange(self, nextPosition: list[int]):
        _xInRange = (0 <= nextPosition[1] < len(self.heightmap[0]))
        _yInRange = (0 <= nextPosition[0] < len(self.heightmap))
        return _xInRange and _yInRange

    def getHeightDiff(self, currentPosition: list[int], nextPosition: list[int]):
        _currentHeight = self.heightmap[currentPosition[0]][currentPosition[1]]        
        _nextHeight = self.heightmap[nextPosition[0]][nextPosition[1]]
        if _currentHeight == _START:
            _currentHeight = 'a'
        if _nextHeight == _DESTINATION:
            _nextHeight = 'z'

        return ord(_nextHeight) - ord(_currentHeight)

    def canExplore(self, currentPosition: list[int], nextPosition: list[int]):
        _heightDiff = self.getHeightDiff(currentPosition=currentPosition, nextPosition=nextPosition)
        _canExplore = _heightDiff <= 1
        return _canExplore

    def explore(self, path: Path):
        # print(f"Checking path: {path.path}")

        _lastPosition = path.path[-1]
        _height = self.heightmap[_lastPosition[0]][_lastPosition[1]]
        # print(f"Current height: {_height}")
        if _lastPosition == self.destination:
            path.reached_destination = True
            # print(f"Reached destination in {path.steps()} steps.")
            self.currentMin = min(path.steps(), self.currentMin)
            return
        
        _currentSteps = path.steps()
        if _currentSteps > self.currentMin: # give up
            # print(f"Giving up on path as it is already longer than the current minimum.")
            return

        _nextPositionsToExplore = []
        #left
        _nextPosition = [_lastPosition[0], _lastPosition[1]-1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_lastPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #right
        _nextPosition = [_lastPosition[0], _lastPosition[1]+1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_lastPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #up
        _nextPosition = [_lastPosition[0]-1, _lastPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_lastPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #down
        _nextPosition = [_lastPosition[0]+1, _lastPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_lastPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)

        if len(_nextPositionsToExplore) == 0: # Dead end
            self.deadends.add((_lastPosition[0], _lastPosition[1]))
            return

        # order to prioritise climbing
        _nextPositionsToExplore = sorted(_nextPositionsToExplore, key=lambda x: self.getHeightDiff(_lastPosition, x), reverse=True)

        _currentDepth = len(path.path)
        # print(f"Depth: {_currentDepth}")
        for _position in _nextPositionsToExplore:
            path.path = path.path[:_currentDepth] 
            _deadEnd = (_position[0], _position[1]) in self.deadends
            _alreadyBeen = _position in path.path
            if not _deadEnd and not _alreadyBeen:
                path.add(_position)
                self.explore(path)

    def find_fastest_path(self):
        _path = Path()
        _path.add(self.start)
        self.explore(_path)

        return self.currentMin

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    with open(_input) as f:
        _lines = f.readlines()
        _pathFinder = PathFinder(heightmap=_lines)
        _fastest = _pathFinder.find_fastest_path()
        print(f"Fastest path: {_fastest}")    

if __name__ == '__main__':
    # cProfile.run('solve_part_1()')

    solve_part_1()
    # solve_part_2()
    sys.exit(0)

