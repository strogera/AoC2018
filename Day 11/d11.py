def findGridSquareMaxPower(grid, squareSize):
    #https://en.wikipedia.org/wiki/Summed-area_table 
    #https://www.youtube.com/watch?v=5ceT8O3k6os
    summedAreaTable = []
    for x in range(len(grid)):
        summedAreaTable.append([])
        for y in range(len(grid[0])):
            summ = grid[x][y]
            if x - 1 >= 0:
                summ += summedAreaTable[x-1][y]
            if y - 1 >= 0:
                summ += summedAreaTable[x][y-1]
            if x - 1 >= 0 and y - 1 >= 0:
                summ -= summedAreaTable[x-1][y-1]
            summedAreaTable[x].append(summ)
    
    maxValue = -9999999
    maxCoords = (0, 0)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if x - squareSize < 0 or y - squareSize < 0:
                continue
            value = (summedAreaTable[x][y] -
              summedAreaTable[x-squareSize][y] -
              summedAreaTable[x][y-squareSize] +
              summedAreaTable[x-squareSize][y - squareSize])
            if value >= maxValue:
                maxValue = value
                maxCoords = (x, y)
    return (maxCoords[0] - (squareSize - 1) + 1, maxCoords[1] - (squareSize - 1) + 1, squareSize, maxValue)


def partOne():
    with open("input.txt", "r") as inputFile:
        serialNumber = 0
        for line in inputFile:
            serialNumber = int(line.strip())
        power = []
        for x in range(1, 301):
            power.append([])
            for y in range(1, 301):
                power[x - 1].append(0)
                rackId = x + 10
                power[x - 1][y - 1] = (rackId * y + serialNumber) * rackId
                power[x - 1][y - 1] = str(power[x - 1][y - 1])
                power[x - 1][y - 1] = int(power[x - 1][y - 1][-3] if len(power[x - 1][y - 1]) >= 3 else 0)
                power[x - 1][y - 1] -= 5
        sqr = findGridSquareMaxPower(power, 3)
        return str(sqr[0]) + ',' + str(sqr[1])
                    



def partTwo():
    with open("input.txt", "r") as inputFile:
        serialNumber = 0
        for line in inputFile:
            serialNumber = int(line.strip())
        power = []
        for x in range(1, 301):
            power.append([])
            for y in range(1, 301):
                power[x - 1].append(0)
                rackId = x + 10
                power[x - 1][y - 1] = (rackId * y + serialNumber) * rackId
                power[x - 1][y - 1] = str(power[x - 1][y - 1])
                power[x - 1][y - 1] = int(power[x - 1][y - 1][-3] if len(power[x - 1][y - 1]) >= 3 else 0)
                power[x - 1][y - 1] -= 5
        sqrs = []
        for i in range(301):
            sqrs.append(findGridSquareMaxPower(power, i))
        sqr = max(sqrs, key = lambda x: x[-1])

        return str(sqr[0]) + ',' + str(sqr[1]) + ',' + str(sqr[2])

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
