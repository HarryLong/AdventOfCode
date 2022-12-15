import os
import sys

ROCK = '#'
AIR = '.'
RANGE_TO = '->'

class World:
    def __init__(self, xmin: int, width: int, height: int,) -> None:
        self.xmin = xmin
        self.width = width
        self.height = height

        self.world = []
        for _y in range(self.height):
            self.world.append([AIR] * self.width)

    def toWorld(self, posX: int, posY: int):
        return posX - self.xmin, posY

    def addRockLine(self, xStart: int, yStart: int, xEnd: int, yEnd: int):
        _xStart = min(xStart, xEnd)
        _yStart = min(yStart, yEnd)
        _xEnd  = max(xStart, xEnd)
        _yEnd = max(yStart, yEnd)


        for _x in range(_xStart, _xEnd+1):
            for _y in range(_yStart, _yEnd+1):
                _worldPosX, _worldPosY = self.toWorld(_x, _y)
                self.world[_worldPosY][_worldPosX] = ROCK
    
    def print(self):
        _row = 0
        for _level in self.world:
            print(f"{_row} {_level}")
            _row += 1

def parsePosition(pos: str):
    _xy = pos.split(',')
    _x = int(_xy[0].strip())
    _y = int(_xy[1].strip())
    return _x, _y

def findWorldExtremeties():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')
    
    _xMin = sys.maxsize
    _xMax = -1
    _yMin = sys.maxsize
    _yMax = -1

    with open(_input) as f:
        for _line in f:
            _xyPairs = _line.split(RANGE_TO)
            for _pair in _xyPairs:
                _x, _y = parsePosition(_pair)
                _xMin = min(_xMin, _x)
                _xMax = max(_xMax, _x)
                _yMin = min(_yMin, _y)
                _yMax = max(_yMax, _y)
    
    return _xMin, _xMax, _yMin, _yMax

def solve_part_1():
    _xmin, _xmax, _ymin, _ymax = findWorldExtremeties()
    print(f"World : {_xmin, _xmax, _ymin, _ymax}")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _world = World(xmin=_xmin, width=_xmax-_xmin+1, height=_ymax+1)
    with open(_input) as f:
        for _line in f:
            _xyPairs = _line.split(RANGE_TO)
            _xStart, _yStart = parsePosition(_xyPairs[0])
            for _pos in _xyPairs[1:]:
                _xEnd, _yEnd = parsePosition(_pos)
                _world.addRockLine(xStart=_xStart, yStart=_yStart, xEnd=_xEnd, yEnd=_yEnd)
                _xStart, _yStart = _xEnd, _yEnd

    _world.print()

if __name__ == '__main__':
    solve_part_1()
    # solve_part_2()
    sys.exit(0)
