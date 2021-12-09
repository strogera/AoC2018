from collections import defaultdict

def parseFromBeforeOrAfter(string):
    return [int(x) for x in string.replace('[', ']').split(']')[-2].split(',')]

opsMap = {
    'addr': lambda registers, a, b: registers[a] + registers[b],
    'addi': lambda registers, a, b: registers[a] + b,
    'mulr': lambda registers, a, b: registers[a] * registers[b],
    'muli': lambda registers, a, b: registers[a] * b,
    'banr': lambda registers, a, b: registers[a] & registers[b],
    'bani': lambda registers, a, b: registers[a] & b,
    'borr': lambda registers, a, b: registers[a] | registers[b],
    'bori': lambda registers, a, b: registers[a] | b,
    'setr': lambda registers, a, _: registers[a],
    'seti': lambda registers, a, _: a,
    'gtir': lambda registers, a, b: 1 if a > registers[b] else 0,
    'gtri': lambda registers, a, b: 1 if registers[a] > b else 0,
    'gtrr': lambda registers, a, b: 1 if registers[a] > registers[b] else 0,
    'eqir': lambda registers, a, b: 1 if a == registers[b] else 0,
    'eqri': lambda registers, a, b: 1 if registers[a] == b else 0,
    'eqrr': lambda registers, a, b: 1 if registers[a] == registers[b] else 0,
}

def partOne():
    with open("input.txt", "r") as inputFile:
        elems = inputFile.read().split('\n\n')
        A = 1
        B = 2
        C = 3
        count = 0
        for e in elems:
            if len(e) == 0 or e[0] == '\n':
                break
            else:
                countPossibleOpcodes = 0
                curStr = e.strip().split('\n')
                before, instruction, after = curStr
                before = parseFromBeforeOrAfter(before)
                instruction = [int(x) for x in instruction.split(' ')]
                after = parseFromBeforeOrAfter(after)
                for op in opsMap:
                    result = opsMap[op](before, instruction[A], instruction[B])
                    if result == after[instruction[C]]:
                        countPossibleOpcodes += 1
                if countPossibleOpcodes >=3:
                    count += 1
        return count

def partTwo():
    with open("input.txt", "r") as inputFile:
        elems = inputFile.read().split('\n\n')
        OP = 0
        A = 1
        B = 2
        C = 3
        program = []
        readProgram = False
        possibleOpCodes = defaultdict(set)
        for e in elems:
            if readProgram or len(e) == 0 or e[0] == '\n':
                readProgram = True
                if len(e) < 4:
                    continue
                program = [[int(x) for x in y.strip().split(' ')] for y in e.strip().split('\n')]
                break
            else:
                curStr = e.strip().split('\n')
                before, instruction, after = curStr
                before = parseFromBeforeOrAfter(before)
                instruction = [int(x) for x in instruction.split(' ')]
                after = parseFromBeforeOrAfter(after)
                for op in opsMap:
                    result = opsMap[op](before, instruction[A], instruction[B])
                    if result == after[instruction[C]]:
                        possibleOpCodes[instruction[OP]].add(op)

        while any(len(x) != 1 for x in possibleOpCodes.values()):
            for opNumber in possibleOpCodes:
                if len(possibleOpCodes[opNumber]) == 1:
                    for opNumber2 in possibleOpCodes:
                        if opNumber2 != opNumber:
                            possibleOpCodes[opNumber2] -= (possibleOpCodes[opNumber])
        opCodes = {}
        for k in possibleOpCodes:
            opCodes[k] = list(possibleOpCodes[k])[0]

        registers = [0, 0, 0, 0]
        for instruction in program:
            registers[instruction[C]] = opsMap[opCodes[instruction[OP]]](registers, instruction[A], instruction[B])

        return registers[OP]

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
