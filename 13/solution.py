import copy
from itertools import repeat
import os
from re import X
import re
import sys
from threading import Thread
import cProfile  
    
class Packet:
    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        self.values = []
        _packet = ''
        _openLists = 0
        for _char in descriptor[1:-1]:
            if _char == ',':
                if _openLists > 0:
                    _packet += _char
                elif len(_packet) > 0:
                    self.values.append(_packet)
                    _packet = ''
                continue
            
            _packet += _char
            # option 1: it's list 
            if _char == ']':
                _openLists -= 1
                if _openLists == 0:
                    self.values.append(Packet(_packet))
                    _packet = ''
            if _char == '[':
                _openLists += 1            

        if len(_packet) > 0:
            self.values.append(_packet)

# is packet 1 smaller than packet 2
def isSmaller(packet1, packet2):
    _nElementsPacket1 = len(packet1.values)
    _nElementsPacket2 = len(packet2.values)
    _range = max(_nElementsPacket1, _nElementsPacket2)
    for _i in range(_range):
        print(f"Comparing {packet1.descriptor} and {packet2.descriptor}")
        if len(packet2.values) <= _i:
            print(f"False --> current: {_i} | Packet 1 length: {_nElementsPacket1} | Packet 2 length: {_nElementsPacket2}")
            return False
        if len(packet1.values) <= _i:
            print(f"True --> current: {_i} | Packet 1 length: {_nElementsPacket1} | Packet 2 length: {_nElementsPacket2}")
            return True
        _packet1Value = packet1.values[_i]
        _packet2Value = packet2.values[_i]
        # transform packet 1 to list:
        if type(_packet1Value) is Packet and type(_packet2Value) is not Packet:
            _packet2Value = Packet("[" + _packet2Value + "]")
        # transform packet 2 to list:
        elif type(_packet2Value) is Packet and type(_packet1Value) is not Packet:
            _packet1Value = Packet("[" + _packet1Value + "]")        
        
        if type(_packet1Value) is Packet and type(_packet2Value) is Packet:
            _smaller = isSmaller(_packet1Value, _packet2Value)
            if _smaller != None:
                return _smaller
        else:
            assert type(_packet1Value) is not Packet and type(_packet2Value) is not Packet, "This should never happen"
            if int(_packet1Value) > int(_packet2Value):
                print(f"False ( {_packet1Value} > {_packet2Value} )")
                return False
            if int(_packet2Value) > int(_packet1Value):
                print(f"True ( {_packet2Value} > {_packet1Value} )")
                return True

def solve_part_1():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    _input = os.path.join(__location__, 'input.txt')

    _packetsInCorrectOrder = []
    _packetId = 0
    _sumOfPacketsInCorrectOrder = 0
    with open(_input) as f:
        _lines = f.readlines()
        for _i in range(0, len(_lines), 3):
            _packetId += 1
            _packet1 = Packet(_lines[_i].strip())
            _packet2 = Packet(_lines[_i+1].strip())
            print(f"Packet1: {_packet1.descriptor}")
            print(f"Packet2: {_packet2.descriptor}")
            _smaller = isSmaller(_packet1, _packet2)
            if _smaller == None:
                assert False, "This should not happen"
            else:
                if _smaller:
                    _packetsInCorrectOrder.append(_packetId)
                    _sumOfPacketsInCorrectOrder += _packetId
        
    print(f"Packets in correct order: {_packetsInCorrectOrder}")
    print(f"Sum of packets in correct order: {_sumOfPacketsInCorrectOrder}")

if __name__ == '__main__':
    solve_part_1()
    sys.exit(0)
