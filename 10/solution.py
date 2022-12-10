from itertools import repeat
import os
import sys

class Instruction:
    def __init__(self, descriptor: str):
        if descriptor[:4] == 'noop':
            self.clock_cycles = 1
            self.registerIncrement = 0
        else:
            self.clock_cycles = 2
            self.registerIncrement = int(descriptor[5:])

    def cycle(self):
        self.clock_cycles -= 1
        return self.clock_cycles

class CPU:
    def __init__(self):
        self.registerX = 1
        self.instructions = []
        self.clock_cycle = 0
        self.sumOfSignalStrength = 0

    def execute(self, instruction: Instruction = None):
        self.clock_cycle += 1
        
        if instruction != None: 
            self.instructions.insert(0, instruction)
        
        if(len(self.instructions) == 0):
            return False

        # process latest instruction
        if self.instructions[-1].cycle() == 0:
            self.registerX += self.instructions[-1].registerIncrement
            self.instructions.pop()

        return True

class CRT:
    def __init__(self):
        self.currentPixel = 0
        self.width = 40
        self.height = 6
        self.monitor = list(repeat('.', self.width*self.height))

    def render(self, spritePos: int):
        _pixelRow = int(self.currentPixel / self.width)
        _startRow = _pixelRow * self.width
        _endRow = (_pixelRow+1) * self.width
        _realSpritePos = _startRow + spritePos
        if max(_startRow, _realSpritePos-1) == self.currentPixel or _realSpritePos == self.currentPixel  or min(_endRow, _realSpritePos+1) == self.currentPixel:
            self.monitor[self.currentPixel] = '#'
        
        self.currentPixel = (self.currentPixel+1) % len(self.monitor)
    
    def renderMonitor(self):
        for _y in range(self.height):
            _from = _y*self.width
            _to = (_y+1)*self.width
            print(self.monitor[_from:_to])

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')
    _cpu = CPU()
    with open(_input) as f:
        for _line in f:
            _instruction = Instruction(_line.strip())
            _cpu.execute(_instruction)
    
    _commandExecuted = _cpu.execute()
    while _commandExecuted:
        _commandExecuted = _cpu.execute()

    print(f"Sum of signal strengths: {_cpu.sumOfSignalStrength}")

def executeCrtAndCpu(cpu: CPU, crt: CRT, instruction: str = None):
    crt.render(cpu.registerX)
    return cpu.execute(instruction)

def solve_part_2():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')
    _cpu = CPU()
    _crt = CRT()
    with open(_input) as f:
        for _line in f:
            _instruction = Instruction(_line.strip())
            executeCrtAndCpu(cpu=_cpu, crt=_crt, instruction=_instruction)
    
    _commandExecuted = executeCrtAndCpu(cpu=_cpu, crt=_crt)
    while _commandExecuted:
        _commandExecuted = executeCrtAndCpu(cpu=_cpu, crt=_crt)
    
    _crt.renderMonitor()

if __name__ == '__main__':
    # solve_part_1()
    solve_part_2()
    sys.exit(0)

