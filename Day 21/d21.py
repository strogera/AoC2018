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
        inp = inputFile.readlines()
        registers = [1] + [0] * 5
        boundedRegister = int(inp[0].split(' ')[-1].strip())
        ip = 0
        instructions = [x.strip().split(' ') for x in inp[1:]]
        while ip < len(instructions):
            if instructions[ip][0] == 'eqrr' and instructions[ip][2] == '0':
                return registers[int(instructions[ip][1])]
            registers[boundedRegister] = ip
            registers[int(instructions[ip][-1])] = opsMap[instructions[ip][0]](registers, int(instructions[ip][1]), int(instructions[ip][2]))
            ip = registers[boundedRegister] + 1


def partTwo():
    with open("input.txt", "r") as inputFile:
        inp = inputFile.readlines()
        registers = [1] + [0] * 5
        boundedRegister = int(inp[0].split(' ')[-1].strip())
        ip = 0
        instructions = [x.strip().split(' ') for x in inp[1:]]
        haltingNumbers = set()
        countLoops = 0
        prev = None
        while ip < len(instructions):
            if instructions[ip][0] == 'eqrr' and instructions[ip][2] == '0':
                countLoops += 1
                if countLoops % 1000 == 0:
                    print('Current loop:', countLoops)
                num = registers[int(instructions[ip][1])]
                if prev == None:
                    prev = num
                if num in haltingNumbers:
                    return prev
                else:
                    haltingNumbers.add(num)
                    prev = num
            registers[boundedRegister] = ip
            registers[int(instructions[ip][-1])] = opsMap[instructions[ip][0]](registers, int(instructions[ip][1]), int(instructions[ip][2]))
            ip = registers[boundedRegister] + 1


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
