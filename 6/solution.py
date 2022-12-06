import os
import sys

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    with open(_input) as f:
        _currentIdex = 0
        _subroutineFound = False
        _rollingWindow = [] 
        while not _subroutineFound:
            _currentIdex += 1
            _rollingWindow.insert(0, f.read(1))
            while len(_rollingWindow) > 4:
                _rollingWindow.pop()
            if len(_rollingWindow) == 4:
                _subroutineFound = len(set(_rollingWindow)) == 4
    assert _subroutineFound
    print(f"Subroutine found at index: {_currentIdex}")

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    with open(_input) as f:
        _currentIdex = 0
        _subroutineFound = False
        _rollingWindow = [] 
        while not _subroutineFound:
            _currentIdex += 1
            _rollingWindow.insert(0, f.read(1))
            while len(_rollingWindow) > 14:
                _rollingWindow.pop()
            if len(_rollingWindow) == 14:
                _subroutineFound = len(set(_rollingWindow)) == 14
    assert _subroutineFound
    print(f"Subroutine found at index: {_currentIdex}")

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)

