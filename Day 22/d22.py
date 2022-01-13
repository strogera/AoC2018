import heapq
from functools import lru_cache

def erosion(geoIndex, depth):
    return (geoIndex + depth) % 20183

@lru_cache(None)
def geoIndex(x, y, depth, targetx, targety):
    if x == 0 and y == 0:
        return 0
    if x == 0:
        return  y * 48271
    if y == 0:
        return x * 16807
    if x == targetx and y == targety:
        return 0
    return erosion(geoIndex(x - 1, y, depth, targetx, targety), depth) * erosion(geoIndex(x, y - 1, depth, targetx, targety), depth)


def partOne():
    with open("input.txt", "r") as inputFile:
        depth = 0
        target = []
        for line in inputFile:
            if 'depth' in line:
                depth = int(line.strip().split(' ')[-1])
            elif 'target' in line:
                target = list(map(int, line.strip().split(' ')[-1].split(',')))
        riskLevel = 0
        for x in range(target[0]+1):
            for y in range(target[1]+1):
                riskLevel += erosion(geoIndex(x, y, depth, *target), depth)% 3
        return riskLevel


def changeEquipment(equipment, posErosion):
    if posErosion % 3 == 0:
        if equipment == 'climb':
            return 'torch'
        elif equipment == 'torch':
            return 'climb'
    elif posErosion % 3 == 1:
        if equipment == 'climb':
            return 'neither'
        elif equipment == 'neither':
            return 'climb'
    else:
        if equipment == 'torch':
            return 'neither'
        elif equipment == 'neither':
            return 'torch'
    print("illegal equipment")
    assert(False)

def findShortestPath(depth, target):
    #dijkstra
    queue = []
    heapq.heappush(queue, (0, 0, 0, 'torch'))
    dist = {}
    dist[(0, 0, 'torch')] = 0
    adjList = {1, -1, 1j, -1j}
    while queue:
        cost, posx, posy, equipment = heapq.heappop(queue)
        pos = complex(posx, posy)
        posErosion = erosion(geoIndex(posx, posy, depth, *target), depth)
        if posx == target[0] and posy == target[1] and equipment == 'torch':
            return cost
        for adj in adjList:
            adj += pos
            x, y = int(adj.real), int(adj.imag)
            if x < 0 or y < 0:
                continue
            adjErosion = erosion(geoIndex(x, y, depth, *target), depth)
            if ((adjErosion % 3 == 0 and equipment != 'neither') or
                 adjErosion % 3 == 1 and equipment != 'torch' or
                 adjErosion % 3 == 2 and equipment != 'climb') :
                newCost = cost + 1
                if (x, y, equipment) not in dist or newCost < dist[(x, y, equipment)]:
                    heapq.heappush(queue, (newCost, x, y, equipment))
                    dist[(x, y, equipment)] = newCost

        changedEq = changeEquipment(equipment, posErosion)
        if(posx, posy, changedEq) not in dist or cost + 7 < dist[(posx, posy, changedEq)]:
            heapq.heappush(queue, (cost + 7, posx, posy, changedEq))
            dist[(posx, posy, changedEq)] = cost + 7


def partTwo():
    with open("input.txt", "r") as inputFile:
        depth = 0
        target = []
        for line in inputFile:
            if 'depth' in line:
                depth = int(line.strip().split(' ')[-1])
            elif 'target' in line:
                target = list(map(int, line.strip().split(' ')[-1].split(',')))
        return findShortestPath(depth, target)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
