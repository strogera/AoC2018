from collections import defaultdict

def partOne(partTwo = False):
    with open("input.txt", "r") as inputFile:
        reg = inputFile.readlines()[0].strip()[1:]
        direction = {'E': 1, 'N': 1j, 'S': -1j, 'W': -1}
        pos = 0j
        stack = []
        dist = defaultdict(int)
        for command in reg:
            if command in direction:
                prevRoom = pos
                pos += direction[command] #door
                pos += direction[command] #room
                if dist[pos] != 0:
                    dist[pos] = min(dist[pos], dist[prevRoom] + 1)
                else:
                    dist[pos] = dist[prevRoom] + 1
            elif command == '(':
                stack.append(pos)
            elif command == ')':
                pos = stack.pop()
            elif command == '|':
                pos = stack[-1]
            elif command == '$':
                break
        if not partTwo:
            return max(dist.values())
        else:
            return len(list(filter(lambda x: x >= 1000, dist.values())))


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(True))
