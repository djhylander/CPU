# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:48:32 2019

Uses a binary instruction set and 

@author: dhyla
"""

file = open("Binary Instructions.txt")
instructions = file.readlines()

regs = [2, 2, 4, 1]
for i in range(32 - len(regs)):
    regs.append(0)

dmem = []
for i in range(2 ** 16):
    dmem.append(0)

mask5 = '11111'
def opFinder(inst): # takes string instruction and returns binary op after shifting and masking
    zero  = ''
    op = format(int(inst, 2) >> 27 & int(mask5, 2), 'b')
    for i in range(5 - len(op)):
        zero = zero + '0'
    op = zero + op
    return op

def decode(inst): # returns sources and destination for add, subtract, and compare
    s1 = int(inst, 2) >> 22 & int(mask5, 2)
    s2 = int(inst, 2) >> 17 & int(mask5, 2)
    dest = int(inst, 2) >> 12 & int(mask5, 2)
    return s1, s2, dest

mask3 = '111'
mask16 = '1111111111111111'
def decodeBranch(inst): # return cc and new location for branching
    zero = ''
    cc = str(format(int(inst, 2) >> 24 & int(mask3, 2), 'b'))
    for i in range(3 - len(cc)):
        zero = zero + '0'
    cc = zero + cc
    loc = int(inst, 2) & int(mask16, 2)
    return cc, loc

opAdd = '00001'
opSub = '00010'
opComp = '00011'
opBranch = '00100'

ccEq = '000'
ccNotEq = '001'
ccLess = '010'
ccLessEq = '011'
ccGreater = '100'
ccGreaterEq = '101'

lessThan = 0
equal = 0
pc = 0
while True: # infinite loop to read all instructions
    if (pc >= len(instructions)):
        break
    instCurr = instructions[pc]
    op = opFinder(instCurr)

    if (op == opAdd):
        s1, s2, dest = decode(instCurr)
        regs[dest] = regs[s1] + regs[s2]
        pc += 1
    elif (op == opSub):
        s1, s2, dest = decode(instCurr)
        regs[dest] = regs[s1] - regs[s2]
        pc += 1
    elif (op == opComp):
        s1, s2, dest = decode(instCurr)
        if (regs[s1] < regs[s2]):
            lessThan = 1
        else:
            lessThan = 0
        if (regs[s1] == regs[s2]):
            equal = 1
        else:
            equal = 0
        pc += 1
    elif (op == opBranch):
        cc, loc = decodeBranch(instCurr)
        if (cc == ccEq):
            if (equal):
                pc = loc
            else:
                pc += 1
        elif (cc == ccNotEq):
            if (not equal):
                pc = loc
            else:
                pc += 1
        elif (cc == ccLess):
            if (lessThan):
                pc = loc
            else:
                pc += 1
        elif (cc == ccLessEq):
            if (lessThan or equal):
                pc = loc
            else:
                pc += 1
        elif (cc == ccGreater):
            if (not lessThan and not equal):
                pc = loc
            else:
                pc += 1
        elif (cc == ccGreaterEq):
            if (not lessThan):
                pc = loc
            else:
                pc += 1
    if (pc == 13):
        print("done")
        exit




