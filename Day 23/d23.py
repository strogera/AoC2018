import heapq

class Nanobot():
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

def manhattanDistance(pos1, pos2):
    return sum([abs(a - b) for a, b in zip(pos1, pos2)])

def partOne():
    with open("input.txt", "r") as inputFile:
        botList = []
        for line in inputFile:
            pos, r = line.strip().split(' ')
            r = int(r.split('=')[-1].strip())
            pos = list(map(int, pos.split('<')[-1][:-2].split(',')))
            botList.append(Nanobot(pos, r))
        strongestBot = max(botList, key = lambda k: k.r)
        count = 0
        for bot in botList:
            if manhattanDistance(bot.pos, strongestBot.pos) <= strongestBot.r:
                count += 1
        return count


def partTwo():
    # solution from:
    #https://www.reddit.com/r/adventofcode/comments/a8s17l/comment/ecdqzdg/?utm_source=share&utm_medium=web2x&context=3
    with open('input.txt', 'r') as inputFile:
        q = []
        for line in inputFile:
            pos, r = line.strip().split(' ')
            r = int(r.split('=')[-1].strip())
            pos = list(map(int, pos.split('<')[-1][:-2].split(',')))
            d = manhattanDistance([0, 0, 0], pos)
            heapq.heappush(q, (max(0, d - r),1))
            heapq.heappush(q, (d + r + 1,-1))
        count = 0
        maxCount = 0
        result = 0
        while q:
            dist, e = heapq.heappop(q)
            count += e
            if count > maxCount:
                result = dist
                maxCount = count
        return result

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
