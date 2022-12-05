import os
import re
import sys

def build_stacks(stacks_filename : str) -> list[list[str]]:
    _stacks = [[]]
    with open(stacks_filename) as f:
        _lines = f.readlines()
        for _i in range(len(_lines)-2, -1, -1):
            _line = _lines[_i]
            matches = re.finditer(r"[A-Z]", _line)
            for match in matches:
                stack_index = int(match.start()/4)
                while len(_stacks) < stack_index+1:
                    _stacks.append([])
                _stacks[stack_index].append(match.group(0))
    return _stacks

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input_stacks = os.path.join(__location__, 'input_stacks.txt')
    _input_moves = os.path.join(__location__, 'input_moves.txt')

    _stacks = build_stacks(_input_stacks)
    with open(_input_moves) as f:
        for _line in f:
            _line = _line.rstrip()
            _matches = re.findall(r"\d+", _line)
            _nMoves = int(_matches[0])
            _srcStackIdx = int(_matches[1])-1
            _dstStackIdx = int(_matches[2])-1
            for _i in range(_nMoves):
                _stacks[_dstStackIdx].append(_stacks[_srcStackIdx].pop())

    _topLine = ''
    for _stack in _stacks:
        _topLine += _stack[len(_stack) - 1]
    print(_topLine)

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input_stacks = os.path.join(__location__, 'input_stacks.txt')
    _input_moves = os.path.join(__location__, 'input_moves.txt')

    _stacks = build_stacks(_input_stacks)
    with open(_input_moves) as f:
        for _line in f:
            _line = _line.rstrip()
            _matches = re.findall(r"\d+", _line)
            _nMoves = int(_matches[0])
            _srcStackIdx = int(_matches[1])-1
            _dstStackIdx = int(_matches[2])-1
            _srcStack = _stacks[_srcStackIdx]
            _dstStack = _stacks[_dstStackIdx]
            _srcCrates = _srcStack[len(_srcStack) - _nMoves:]
            _dstStack += _srcCrates
            del _srcStack[-_nMoves:]
            print(_srcStack)

    _topLine = ''
    for _stack in _stacks:
        _topLine += _stack[len(_stack) - 1]
    print(_topLine)

if __name__ == '__main__':
    solve_part_2()
    sys.exit(0)

