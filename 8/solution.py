import os
import sys

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    # build the 2d array
    _flattenedTreeMap = []
    _treeMapWidth = 0
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            if _treeMapWidth == 0:
                _treeMapWidth = len(_line)
            for _char in _line:
                _flattenedTreeMap.append(int(_char))
    
    _treeMapHeight = int(len(_flattenedTreeMap)/_treeMapWidth)
    _visibleTrees = _treeMapHeight * 2 + _treeMapWidth * 2 - 4 # The 4 corner points have been considered twice
    _visibleTreeIndices = set()
    # Horizontal Left -> Right and Right -> Left
    for _treeRowIdx in range(1, _treeMapHeight-1):
        _startTreeIdxX = _treeRowIdx * _treeMapWidth
        _currentMax = _flattenedTreeMap[_startTreeIdxX]
        # Left -> Right
        for _treeIdxX in range(0, _treeMapWidth-1):
            _idx = _startTreeIdxX+_treeIdxX
            _treeHeight = _flattenedTreeMap[_idx]
            if _treeHeight > _currentMax:
                _currentMax = _treeHeight
                _visibleTreeIndices.add(_idx)
                _visibleTrees += 1
        _treeLineMax = _currentMax
        # Right -> Left
        _startTreeIdxX = (_treeRowIdx+1)*_treeMapWidth-1
        _currentMax = _flattenedTreeMap[_startTreeIdxX]
        for _treeIdxX in range(0, _treeMapWidth-1):
            _idx = _startTreeIdxX-_treeIdxX
            _treeHeight = _flattenedTreeMap[_idx]
            if _treeHeight > _currentMax:
                if not _idx in _visibleTreeIndices: 
                    _visibleTreeIndices.add(_idx)
                    _visibleTrees += 1
                _currentMax = _treeHeight
            if _treeHeight == _treeLineMax: # optimization: No need to continue if we have reached the heighest tree
                break

    # Vertical Top -> Bottom and Bottom to Top
    for _treeColumnIdx in range(1, _treeMapWidth-1):
        _startTreeIdxY = _treeColumnIdx
        _currentMax = _flattenedTreeMap[_startTreeIdxY]
        # Top -> Bottom
        for _treeIdx in range(_treeMapHeight-1):
            _idx = _startTreeIdxY+_treeIdx*_treeMapWidth
            _treeHeight = _flattenedTreeMap[_idx]
            if _treeHeight > _currentMax:
                if not _idx in _visibleTreeIndices: 
                    _visibleTreeIndices.add(_idx)
                    _visibleTrees += 1
                _currentMax = _treeHeight
        _treeLineMax = _currentMax
        # Bottom -> Top
        _startTreeIdxY = _treeMapHeight * _treeMapWidth - _treeColumnIdx - 1
        _currentMax = _flattenedTreeMap[_startTreeIdxY]
        for _treeIdx in range(_treeMapHeight-1):
            _idx = _startTreeIdxY-_treeIdx*_treeMapWidth
            _treeHeight = _flattenedTreeMap[_idx]
            if _treeHeight > _currentMax:
                if not _idx in _visibleTreeIndices:
                    _visibleTreeIndices.add(_idx)
                    _visibleTrees += 1
                _currentMax = _treeHeight
            if _treeHeight == _treeLineMax: # optimization: No need to continue if we have reached the heighest tree
                break    

    print(f"Visible tress: {_visibleTrees}")

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    # build the 2d array
    _flattenedTreeMap = []
    _treeMapWidth = 0
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            if _treeMapWidth == 0:
                _treeMapWidth = len(_line)
            for _char in _line:
                _flattenedTreeMap.append(int(_char))
    
    _treeMapHeight = int(len(_flattenedTreeMap)/_treeMapWidth)
    _maxScenicScore = 0
    _maxIndex = 0
    # Horizontal Left -> Right and Right -> Left
    for _treeIdx in range(_treeMapWidth+1, (_treeMapHeight-1)*_treeMapWidth-1): # no need to process the edges
        if _treeIdx % _treeMapWidth == 0 or _treeIdx % _treeMapWidth == (_treeMapWidth-1) :
            continue  

        _leftScore = 0
        _rightScore = 0
        _bottomScore = 0
        _topScore = 0
        _column = _treeIdx % _treeMapWidth
        _row = int(_treeIdx / _treeMapWidth)

        _limitLeft = _row * _treeMapWidth
        _limitRight = (_row+1) * _treeMapWidth-1
        _limitUp = _column
        _limitDown = _column + (_treeMapHeight-1) * _treeMapWidth  
        _treeHeight = _flattenedTreeMap[_treeIdx]
        # Left of tree
        _viewBlocked = False
        _idx = _treeIdx
        while _idx - 1 >= _limitLeft and not _viewBlocked:
            _leftScore += 1
            _idx = _idx - 1
            _height = _flattenedTreeMap[_idx]
            _viewBlocked = _height >= _treeHeight 
        # Right of tree
        _viewBlocked = False
        _idx = _treeIdx
        while _idx + 1 <= _limitRight and not _viewBlocked:
            _rightScore += 1
            _idx = _idx + 1
            _height = _flattenedTreeMap[_idx] 
            _viewBlocked = _height >= _treeHeight 
        # Top of tree
        _viewBlocked = False
        _idx = _treeIdx
        while _idx - _treeMapWidth >= _limitUp and not _viewBlocked:
            _topScore += 1
            _idx = _idx - _treeMapWidth
            _height = _flattenedTreeMap[_idx] 
            _viewBlocked = _height >= _treeHeight 
        # Bottom of tree
        _viewBlocked = False
        _idx = _treeIdx
        while _idx + _treeMapWidth <= _limitDown and not _viewBlocked:
            _bottomScore += 1
            _idx = _idx + _treeMapWidth
            _height = _flattenedTreeMap[_idx] 
            _viewBlocked = _height >= _treeHeight 

        _score =  _leftScore*_rightScore*_topScore*_bottomScore
        if _score > _maxScenicScore:
            _maxScenicScore = _score
            _maxIndex = _treeIdx


    print(f"Max score: {_maxScenicScore}")
    print(f"Max tree index: {_maxIndex}")


if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)

