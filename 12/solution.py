import copy
from itertools import repeat
import os
from re import X
import sys
from threading import Thread
import cProfile

_START = 'S'
_DESTINATION = 'E'

class Node:
    def __init__(self, height: str, destinationNode: bool, x: int, y: int):
        self.x = x
        self.y = y
        self.height = height
        self.distance = sys.maxsize
        self.destinationNode = destinationNode
        self.visited = False

class PathFinder:
    def __init__(self, heightmap: list[str]):
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.heightmap = []
        _row = 0
        for _line in heightmap:
            self.heightmap.append([])
            _column = 0
            for _char in _line.strip():
                _startNode = _char == _START
                _destinationNode = _char == _DESTINATION
                _node = Node(_char, destinationNode=_destinationNode, x=_column, y=_row)
                self.heightmap[-1].append(_node)
                if _startNode:
                    _node.distance = 0
                self.unvisited_nodes.append(_node)
                _column += 1
            _row += 1

    def inRange(self, position: list[int]):
        _xInRange = (0 <= position[0] < len(self.heightmap[0]))
        _yInRange = (0 <= position[1] < len(self.heightmap))
        return _xInRange and _yInRange

    def getNode(self, position: list[int]):
        return self.heightmap[position[1]][position[0]]   

    def getHeightDiff(self, currentPosition: list[int], nextPosition: list[int]):
        _currentHeight = self.getNode(currentPosition).height        
        _nextHeight = self.getNode(nextPosition).height 
        if _currentHeight == _START:
            _currentHeight = 'a'
        if _nextHeight == _DESTINATION:
            _nextHeight = 'z'

        return ord(_nextHeight) - ord(_currentHeight)

    def canExplore(self, currentPosition: list[int], nextPosition: list[int]):
        _heightDiff = self.getHeightDiff(currentPosition=currentPosition, nextPosition=nextPosition)
        _canExplore = _heightDiff <= 1
        return _canExplore

    def iterate(self):
        self.unvisited_nodes = sorted(self.unvisited_nodes, reverse = True, key=lambda x: x.distance) 
        _currentNode = self.unvisited_nodes.pop()

        # self.visited_nodes.append(_currentNode)
        _currentNode.visited = True

        _nextPositionsToExplore = []
        _currentPosition = [_currentNode.x, _currentNode.y]
        _currentDistance = _currentNode.distance
        if _currentDistance == sys.maxsize:
            print(f"No path found!")
            return sys.maxsize

        #left
        _nextPosition = [_currentPosition[0]-1, _currentPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #right
        _nextPosition = [_currentPosition[0]+1, _currentPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #up
        _nextPosition = [_currentPosition[0], _currentPosition[1]-1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #down
        _nextPosition = [_currentPosition[0], _currentPosition[1]+1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)

        for _position in _nextPositionsToExplore:
            _node = self.getNode(_position)
            if _node.destinationNode :
                return _currentDistance + 1
            if not _node.visited:
                _node.distance = min(_currentDistance+1, _node.distance)
        
        return -1

    def find_fastest_path(self):
        _currentDistance = self.iterate()
        while _currentDistance == -1:
            _currentDistance = self.iterate()
        
        print(f"Minimum distance: {_currentDistance}")

class PathFinder2:
    def __init__(self, heightmap: list[str]):
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.heightmap = []
        _row = 0
        for _line in heightmap:
            self.heightmap.append([])
            _column = 0
            for _char in _line.strip():
                _startNode = _char == _START
                _destinationNode = _char == _DESTINATION
                _node = Node(_char, destinationNode=_destinationNode, x=_column, y=_row)
                self.heightmap[-1].append(_node)
                if _startNode:
                    _node.distance = 0
                self.unvisited_nodes.append(_node)
                _column += 1
            _row += 1

    def inRange(self, position: list[int]):
        _xInRange = (0 <= position[0] < len(self.heightmap[0]))
        _yInRange = (0 <= position[1] < len(self.heightmap))
        return _xInRange and _yInRange

    def getNode(self, position: list[int]):
        return self.heightmap[position[1]][position[0]]   

    def getHeightDiff(self, currentPosition: list[int], nextPosition: list[int]):
        _currentHeight = self.getNode(currentPosition).height        
        _nextHeight = self.getNode(nextPosition).height 
        if _currentHeight == _START:
            _currentHeight = 'z'

        return ord(_nextHeight) - ord(_currentHeight)

    def canExplore(self, currentPosition: list[int], nextPosition: list[int]):
        _heightDiff = self.getHeightDiff(currentPosition=currentPosition, nextPosition=nextPosition)
        _canExplore = _heightDiff >= -1
        return _canExplore

    def iterate(self):
        self.unvisited_nodes = sorted(self.unvisited_nodes, reverse = True, key=lambda x: x.distance) 
        _currentNode = self.unvisited_nodes.pop()

        # self.visited_nodes.append(_currentNode)
        _currentNode.visited = True

        _nextPositionsToExplore = []
        _currentPosition = [_currentNode.x, _currentNode.y]
        _currentDistance = _currentNode.distance
        if _currentDistance == sys.maxsize:
            print(f"No path found!")
            return sys.maxsize

        #left
        _nextPosition = [_currentPosition[0]-1, _currentPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #right
        _nextPosition = [_currentPosition[0]+1, _currentPosition[1]]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #up
        _nextPosition = [_currentPosition[0], _currentPosition[1]-1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)
        #down
        _nextPosition = [_currentPosition[0], _currentPosition[1]+1]
        if self.inRange(_nextPosition) and self.canExplore(currentPosition=_currentPosition, nextPosition=_nextPosition):
            _nextPositionsToExplore.append(_nextPosition)

        for _position in _nextPositionsToExplore:
            _node = self.getNode(_position)
            if _node.height == 'a' :
                return _currentDistance + 1
            if not _node.visited:
                _node.distance = min(_currentDistance+1, _node.distance)
        
        return -1

    def find_fastest_path(self):
        _currentDistance = self.iterate()
        while _currentDistance == -1:
            _currentDistance = self.iterate()
        
        print(f"Minimum distance: {_currentDistance}")

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    with open(_input) as f:
        _lines = f.readlines()
        _pathFinder = PathFinder(heightmap=_lines)
        _pathFinder.find_fastest_path()


def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    with open(_input) as f:
        _lines = f.readlines()
        _pathFinder = PathFinder2(heightmap=_lines)
        _pathFinder.find_fastest_path()

if __name__ == '__main__':
    # cProfile.run('solve_part_1()')

    # solve_part_1()
    solve_part_2()
    sys.exit(0)

