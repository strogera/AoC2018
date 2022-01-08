def runDecoded(r0, x1, x2):
    r5 = x1 + r0 * x2
    n = 1
    result = 0
    while n < r5 ** 0.5:
        if r5 % n == 0:
            result += n + r5 // n
        n += 1
    return result

def checkRegisterInput():
    #runs the input as is
    #useful to find the values for the decoded version
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
    with open("input.txt", "r") as inputFile:
        inp = inputFile.readlines()
        registers = [1] + [0] * 5
        boundedRegister = int(inp[0].split(' ')[-1].strip())
        ip = 0
        instructions = [x.strip().split(' ') for x in inp[1:]]
        while ip < len(instructions):
            if instructions[ip][0] == 'addr' and ip > 30:
                print(ip, registers)
                print("probable values: x1 = ", registers[5], ', x2 = ', registers[2])
                return
            registers[boundedRegister] = ip
            registers[int(instructions[ip][-1])] = opsMap[instructions[ip][0]](registers, int(instructions[ip][1]), int(instructions[ip][2]))
            ip = registers[boundedRegister] + 1
        return registers[0]

def partOne(partTwo = False):
    #checkRegisterInput() #run this to find the values for your input
    return runDecoded(1, 964, 10550400) if partTwo else runDecoded(0, 964, 10550400)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(True))
