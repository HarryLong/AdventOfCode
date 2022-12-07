import os
import sys

class Node:
    def __init__(self, name: str, size: int, parent):
        self.size = size
        self.name = name
        self.parent = parent
        self.children = []

    def isLeafNode(self):
        return self.size != 0
    
    def addChild(self, name: str, size: int, parent):
        _childNode = Node(name=name,size=size, parent=parent)
        self.children.append(_childNode)
        return _childNode 

    def getChild(self, name:str):
        for _child in self.children:
            if _child.name == name:
                return _child
        assert False, "Shouldn't get here"
    
    def getSize(self):
        _size = self.size
        for _child in self.children:
            _size += _child.getSize()
        
        return _size

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _rootNode = Node(name='root', size=0, parent=None)
    _currentNode = _rootNode
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            if _line.startswith('$'):
                _line = _line[1:].strip()
                if _line.startswith("cd"): 
                    _line = _line[2:].strip()
                    if _line == '..':
                        _currentNode = _currentNode.parent
                    else:
                        _currentNode = _currentNode.getChild(_line)
            else:
                if _line.startswith('dir'):
                    _line = _line[3:].strip()
                    _currentNode.addChild(name=_line, size=0, parent=_currentNode)
                else: # File
                    _split = _line.split(' ')
                    _size = int(_split[0].strip())
                    _name = _split[1].strip()
                    _currentNode.addChild(name=_name, size=_size, parent=_currentNode)
    
    _dirSizes = {}
    _nodesToProcess = [_rootNode]
    
    _sumLessThan100000 = 0

    while len(_nodesToProcess) > 0:
        _node = _nodesToProcess.pop()
        for _childNode in _node.children:
            if not _childNode.isLeafNode():
                _size = _childNode.getSize()
                if _size <= 100000:
                    _sumLessThan100000 += _size
                _dirSizes[_childNode.name] = _childNode.getSize()
                _nodesToProcess.append(_childNode)
    
    print(_sumLessThan100000)
    
def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _rootNode = Node(name='root', size=0, parent=None)
    _currentNode = _rootNode
    with open(_input) as f:
        for _line in f:
            _line = _line.strip()
            if _line.startswith('$'):
                _line = _line[1:].strip()
                if _line.startswith("cd"): 
                    _line = _line[2:].strip()
                    if _line == '..':
                        _currentNode = _currentNode.parent
                    else:
                        _currentNode = _currentNode.getChild(_line)
            else:
                if _line.startswith('dir'):
                    _line = _line[3:].strip()
                    _currentNode.addChild(name=_line, size=0, parent=_currentNode)
                else: # File
                    _split = _line.split(' ')
                    _size = int(_split[0].strip())
                    _name = _split[1].strip()
                    _currentNode.addChild(name=_name, size=_size, parent=_currentNode)
    
    _totalDiskSize = 70000000
    _requiredSpace = 30000000
    _rootNodeSize = _rootNode.getSize()
    _currentAvailable = _totalDiskSize - _rootNodeSize

    _currentBestDir = 99999999999
    _nodesToProcess = [_rootNode]
    while len(_nodesToProcess) > 0:
        _node = _nodesToProcess.pop()
        for _childNode in _node.children:
            if not _childNode.isLeafNode():
                _nodesToProcess.append(_childNode)
                _size = _childNode.getSize()
                if _currentAvailable + _size >= _requiredSpace:
                    _currentBestDir = min(_size, _currentBestDir)
    
    print(_currentBestDir)

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)

