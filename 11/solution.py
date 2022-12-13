from itertools import repeat
import os
import sys
import cProfile

class FactorTest:
    def __init__(self, factor: int, startingValue: int):
        self.factor = factor
        self.residue = startingValue % factor

    def add(self, add: int):
        self.residue += add
        self.residue = self.residue % self.factor
    
    def multiply(self, factor: int):
        if self.residue != 0:
            self.residue *= factor
            self.residue = self.residue % self.factor
    
    def square(self):
        self.residue = self.residue * self.residue
        self.residue = self.residue % self.factor
    
    def check(self):
        return self.residue % self.factor == 0

class Item:
    def __init__(self, worryLevel: int):
        self.startWorryLevel = worryLevel
        self.worryLevel = worryLevel
        self.factorTests = {
            2: FactorTest(factor=2, startingValue=worryLevel),
            3: FactorTest(factor=3, startingValue=worryLevel),
            5: FactorTest(factor=5, startingValue=worryLevel),
            7: FactorTest(factor=7, startingValue=worryLevel),
            11: FactorTest(factor=11, startingValue=worryLevel),
            13: FactorTest(factor=13, startingValue=worryLevel),
            17: FactorTest(factor=17, startingValue=worryLevel),
            19: FactorTest(factor=19, startingValue=worryLevel),
            23: FactorTest(factor=23, startingValue=worryLevel),
        }

    # def boredomDecrease(self):
    #     self.worryLevel = int(self.worryLevel/3)

    def add(self, addition : int):
        # self.worryLevel += addition
        for _ft in self.factorTests:
            self.factorTests[_ft].add(addition)  

    def square(self):
        # self.worryLevel *= self.worryLevel
        for _ft in self.factorTests:
            self.factorTests[_ft].square()  

    def multiply(self, factor: int):
        # self.worryLevel *= factor
        for _ft in self.factorTests:
            self.factorTests[_ft].multiply(factor)
    
class Test:
    def __init__(self, descriptor : list[str]):
        self.moduloArgument = int(descriptor[0].replace('Test: divisible by', '').strip())
        self.destinationMonkey = { True:  int(descriptor[1].replace('If true: throw to monkey', '').strip()),\
             False: int(descriptor[2].replace('If false: throw to monkey', '').strip())}

    def getDestinationMonkey(self, item: Item):
        _isModulo = item.factorTests[self.moduloArgument].check()
        return self.destinationMonkey[_isModulo]

class Monkey:
    def __init__(self, descriptor : list[str], monkeyIndex: int):
        self.items = []
        self.inspectionCount = 0
        _startingItems = descriptor[0].replace('Starting items:', '').strip().split(',')
        for _item in _startingItems:
            _item = Item(int(_item))
            self.items.append(_item)
        
        self.monkeyIndex = monkeyIndex
        # operationDescriptor = descriptor[1].replace('Operation: new = old ', '').strip()
        # if operationDescriptor[0] == '*':
        #     multiplier = int(operationDescriptor[1:].strip())
        #     self.operation = eval(f"lambda item : item.addPrimeness({multiplier})")
        # else:
        #     addition = int(operationDescriptor[1:].strip())
        #     self.operation = eval(f"lambda item : item.addValue({addition})")
        self.test = Test(descriptor[2:])

    def hasItems(self):
        return len(self.items) > 0

    def playTurn(self, boredomDecrease : bool):
        _item = self.items[-1]
        # inspect
        self.inspectionCount += 1
        # old = _item.worryLevel
        # self.operation(item=_item)

        self.adaptWorry(_item)

        #boredom decrease
        if boredomDecrease:
            _item.worryLevel = int(_item.worryLevel/3)
        
        # _item.worryLevel = _newWorryLevel
        # _item.adaptWorryLevel()
        _destinationMonkeyIdx = self.test.getDestinationMonkey(_item)
        return _destinationMonkeyIdx
    
    def addItem(self, item: Item):
        self.items.insert(0, item)

    def popItem(self):
        return self.items.pop()

    def getItem(self):
        for _item in self.items:
            print(f"{_item.worryLevel}, ")

    def adaptWorry(self, item: Item):
        # if self.monkeyIndex == 0:
        #     item.multiply(19)
        # elif self.monkeyIndex == 1:
        #     item.add(6)
        # elif self.monkeyIndex == 2:
        #     item.square()
        # elif self.monkeyIndex == 3:
        #     item.add(3)
        if self.monkeyIndex == 0:
            item.multiply(3)
        elif self.monkeyIndex == 1:
            item.add(8)
        elif self.monkeyIndex == 2:
            item.add(2)
        elif self.monkeyIndex == 3:
            item.add(4)
        elif self.monkeyIndex == 4:
            item.multiply(19)
        elif self.monkeyIndex == 5:
            item.add(5)
        elif self.monkeyIndex == 6:
            item.square()    
        elif self.monkeyIndex == 7:
            item.add(1)

def playOneRound(monkeys: list[Monkey], boredomDecrease : bool = True):
    _roundExchanges = 0
    for _monkeyIndex in range(len(monkeys)):
        while monkeys[_monkeyIndex].hasItems():
            _monkey = monkeys[_monkeyIndex]
            _destinationMonkeyIdx = _monkey.playTurn(boredomDecrease=boredomDecrease)
            monkeys[_destinationMonkeyIdx].addItem(_monkey.popItem())
            _roundExchanges += 1
    print(f"Exchanges: {_roundExchanges}")


def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')
    _monkeys = []
    with open(_input) as f:
        _lines = f.readlines()
        _currentLine = 1
        _monkeyIndex = 0
        while _currentLine < len(_lines):
            _monkey = Monkey(descriptor=_lines[_currentLine: _currentLine+5], monkeyIndex=_monkeyIndex)
            _monkeys.append(_monkey)
            _currentLine += 7
            _monkeyIndex += 1

    _nRounds = 20
    for _round in range(_nRounds):
        playOneRound(_monkeys)
        # print(f"Round {_round}\n")
        # for _monkeyIdx in range(len(_monkeys)):
        #     print(f"Monkey {_monkeyIdx+1}: ")
        #     _items = ''
        #     for _item in _monkeys[_monkeyIdx].items:
        #         _items += f' {_item.worryLevel}, '
        #     print(_items)

    _totalInspections = []
    for _monkeyIdx in range(len(_monkeys)):
        print(f"Monkey {_monkeyIdx+1} inspected {_monkeys[_monkeyIdx].inspectionCount} items")
        _totalInspections.append(_monkeys[_monkeyIdx].inspectionCount)
    
    _totalInspections.sort()
    _monkeyBusiness = _totalInspections[-2] * _totalInspections[-1]
    print(f"Monkey business: {_monkeyBusiness}")

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')
    _monkeys = []
    with open(_input) as f:
        _lines = f.readlines()
        _currentLine = 1
        _monkeyIndex = 0
        while _currentLine < len(_lines):
            _monkey = Monkey(descriptor=_lines[_currentLine: _currentLine+5], monkeyIndex=_monkeyIndex)
            _monkeys.append(_monkey)
            _currentLine += 7
            _monkeyIndex += 1

    _nRounds = 10000
    for _round in range(_nRounds):
        playOneRound(_monkeys, boredomDecrease=False)
        print(f"Round {_round} / {_nRounds}")
        # for _monkeyIdx in range(len(_monkeys)):
        #     print(f"Monkey {_monkeyIdx+1}: ")
        #     _items = ''
        #     for _item in _monkeys[_monkeyIdx].items:
        #         _items += f' {_item.worryLevel}, '
        #     print(_items)

    _totalInspections = []
    for _monkeyIdx in range(len(_monkeys)):
        print(f"Monkey {_monkeyIdx+1} inspected {_monkeys[_monkeyIdx].inspectionCount} items")
        _totalInspections.append(_monkeys[_monkeyIdx].inspectionCount)
    
    _totalInspections.sort()
    _monkeyBusiness = _totalInspections[-2] * _totalInspections[-1]
    print(f"Monkey business: {_monkeyBusiness}")

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    # cProfile.run('solve_part_2()')
    sys.exit(0)

