import copy
from itertools import repeat
import os
from re import X
import sys
from threading import Thread
import cProfile


class PacketValue:
    def __init__(self, descriptor: str):
        self.value = descriptor
        self.isList = descriptor[0] == '['

class Packet:
    def __init__(self, descriptor: str):
        self.elements = []
        _packet = ''
        _openLists = 0
        for _char in descriptor:
            if _char == ',':
                if _openLists > 0:
                    _packet += _char
                elif len(_packet) != 0:
                    self.elements.append(PacketValue(_packet))
                    _packet = ''
                continue
            
            _packet += _char
            # option 1: it's list 
            if _char == ']':
                _openLists -= 1
                if _openLists == 0:
                    self.elements.append(PacketValue(_packet))
                    _packet = ''
            if _char == '[':
                _openLists += 1            


        if len(_packet) > 0:
            self.elements.append(PacketValue(_packet))
        

def compare(packet1: Packet, packet2: Packet):
    return True

def compare(packet1: str, packet2: str):
    return True

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _packetsInCorrectOrder = 0
    with open(_input) as f:
        _lines = f.readlines()
        for _i in range(0, len(_lines), 3):
            _packet1 = Packet(_lines[_i].strip()[1:-1])
            _packet2 = Packet(_lines[_i+1].strip()[1:-1])
            if compare(_packet1, _packet2):
                _packetsInCorrectOrder += 1
        
    print(f"Packets in correct order: {_packetsInCorrectOrder}")

if __name__ == '__main__':
    solve_part_1()
    sys.exit(0)
