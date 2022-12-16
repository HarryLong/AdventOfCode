import os
import sys

ROCK = '#'
AIR = '.'
RANGE_TO = '->'
SAND_START_POS_X, SAND_START_POS_Y  = 500, 0

class World:
    def __init__(self, width: int, height: int,) -> None:
        self.xmin = 0
        self.width = width
        self.height = height

        self.world = []
        for _y in range(self.height):
            self.world.append([AIR] * self.width)

    def addRockLine(self, xStart: int, yStart: int, xEnd: int, yEnd: int):
        _xStart = min(xStart, xEnd)
        _yStart = min(yStart, yEnd)
        _xEnd  = max(xStart, xEnd)
        _yEnd = max(yStart, yEnd)

        if _yStart == _yEnd:
            for _x in range(_xStart, _xEnd+1):
                self.world[_yStart][_x] = ROCK
        else:
            for _y in range(_yStart, _yEnd+1):
                self.world[_y][_xStart] = ROCK
    
    def addRock(self, xPos:int, yPos: int):
        self.world[yPos][xPos] = ROCK

    def canGoDown(self, _sandPosX: int, _sandPosY: int):
        _y = _sandPosY+1
        if 0 <= _y < self.height:
            return self.world[_y][_sandPosX] != ROCK

    def canGoDownLeft(self, _sandPosX: int, _sandPosY: int):
        _x, _y = _sandPosX-1, _sandPosY+1
        if 0 <= _x < self.width and \
            0 <= _y < self.height:
                return self.world[_y][_x] != ROCK
        return False

    def canGoDownRight(self, _sandPosX: int, _sandPosY: int):
        _x, _y = _sandPosX+1, _sandPosY+1
        if 0 <= _x < self.width and \
            0 <= _y < self.height:
                return self.world[_y][_x] != ROCK
        return False

    def singleSimulationIteration(self):
        _sandPosX, _sandPosY = SAND_START_POS_X, SAND_START_POS_Y
        if self.world[_sandPosY][_sandPosX] == ROCK:
            self.blocked = True
            return
        while True:
            # It can go down
            if self.canGoDown(_sandPosX, _sandPosY):
                _sandPosY += 1
            elif self.canGoDownLeft(_sandPosX, _sandPosY):
                _sandPosX -= 1
                _sandPosY += 1
            elif self.canGoDownRight(_sandPosX, _sandPosY):
                _sandPosX += 1
                _sandPosY += 1
            else:
                if _sandPosY == self.height-1:
                    self.reachedTheAbyss = True
                else:
                    self.restedSand += 1 
                    self.addRock(_sandPosX, _sandPosY)
                break

    def startSimulation(self):
        self.printToFile(f"C:\\tmp\\sand\\start.txt")
        self.reachedTheAbyss = False
        self.blocked = False
        self.restedSand = 0
        while not self.reachedTheAbyss and not self.blocked:
            self.singleSimulationIteration()
            # self.printToFile(f"C:\\tmp\\sand\\iteration_{_iterationCount}.txt")
        print(f"Number of sand that rested: {self.restedSand}")
        print(f"Reached the abyss: {self.reachedTheAbyss}")
        print(f"Blocked: {self.blocked}")

    def print(self):
        _row = 0
        for _level in self.world:
            print(f"{_row} {_level}")
            _row += 1
    
    def printToFile(self, name: str):
        with open(name, 'w') as f:
            for _level in self.world:
                f.write(f"{_level}\n")

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

    _world = World(width=_xmax+1, height=_ymax+1)
    with open(_input) as f:
        for _line in f:
            _xyPairs = _line.split(RANGE_TO)
            _xStart, _yStart = parsePosition(_xyPairs[0])
            for _pos in _xyPairs[1:]:
                _xEnd, _yEnd = parsePosition(_pos)
                _world.addRockLine(xStart=_xStart, yStart=_yStart, xEnd=_xEnd, yEnd=_yEnd)
                _xStart, _yStart = _xEnd, _yEnd

    # _world.print()
    _world.startSimulation()

def solve_part_2():
    _xmin, _xmax, _ymin, _ymax = findWorldExtremeties()
    print(f"World : {_xmin, _xmax, _ymin, _ymax}")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _world = World(width=_xmax*2, height=_ymax+3) # two more units for the 'infinite' floor
    with open(_input) as f:
        for _line in f:
            _xyPairs = _line.split(RANGE_TO)
            _xStart, _yStart = parsePosition(_xyPairs[0])
            for _pos in _xyPairs[1:]:
                _xEnd, _yEnd = parsePosition(_pos)
                _world.addRockLine(xStart=_xStart, yStart=_yStart, xEnd=_xEnd, yEnd=_yEnd)
                _xStart, _yStart = _xEnd, _yEnd
    
    _world.addRockLine(xStart=0, yStart=_ymax+2, xEnd=_xmax*2-1, yEnd=_ymax+2)

    # _world.print()
    _world.startSimulation()

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)
