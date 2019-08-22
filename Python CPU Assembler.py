# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:11:48 2019

@author: dhyla
"""

def assembler(instructions): # creates instruction set in binary
    instSet = []
    for line in instructions:
        output = ''
        if (line.split()[0] == 'add'):
            output += '00001'
            regA = format(int(line.split()[1][2:-1]), 'b') # gives string of binary of register A
            regB = format(int(line.split()[2][2:-1]), 'b')
            regDest = format(int(line.split()[3][2:]), 'b')
            for i in range(5 - len(regA)):
                output += '0'
            output += regA
            for i in range(5 - len(regB)):
                output += '0'
            output += regB
            for i in range(5 - len(regDest)):
                output += '0'
            output += regDest
            for i in range(32 - len(output)):
                output += '0'

        elif (line.split()[0] == 'sub'):
            output += '00010'
            regA = format(int(line.split()[1][2:-1]), 'b')
            regB = format(int(line.split()[2][2:-1]), 'b')
            regDest = format(int(line.split()[3][2:]), 'b')
            for i in range(5 - len(regA)):
                output += '0'
            output += regA
            for i in range(5 - len(regB)):
                output += '0'
            output += regB
            for i in range(5 - len(regDest)):
                output += '0'
            output += regDest
            for i in range(32 - len(output)):
                output += '0'

        elif (line.split()[0] == 'cmp'):
            output += '00011'
            regA = format(int(line.split()[1][2:-1]), 'b')
            regB = format(int(line.split()[2][2:]), 'b')
            for i in range(5 - len(regA)):
                output += '0'
            output += regA
            for i in range(5 - len(regB)):
                output += '0'
            output += regB
            for i in range(32 - len(output)):
                output += '0'

        elif (line.split()[0][:2] == 'br'):
            output += '00100'
            if (line.split()[0][2:] == 'eq'): # equal
                output += '000'
            if (line.split()[0][2:] == 'ne'): # not equal
                output += '001'
            if (line.split()[0][2:] == 'lt'): # less than
                output += '010'
            if (line.split()[0][2:] == 'le'): # less than or equal to
                output += '011'
            if (line.split()[0][2:] == 'mt'): # more than
                output += '100'
            if (line.split()[0][2:] == 'me'): # more than or equal to
                output += '101'
            for i in range(16 - len(output)): # need last 16 digits for new location
                output += '0'
            memLoc = format(int(line.split()[3]), 'b')
            for i in range(16 - len(memLoc)):
                output += '0'
            output += memLoc
        instSet.append(output)
    return instSet

file = open("Improved Instruction Set.txt")
instructions = file.readlines()
instAll = assembler(instructions)

with open('Binary Instructions.txt', 'w') as file:
    for i in range(len(instAll)):
        file.write(instAll[i] + '\n')
