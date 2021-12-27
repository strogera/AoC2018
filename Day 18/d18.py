import copy

def partOne(limit = 10):
    with open("input.txt", "r") as inputFile:
        grid = []
        for line in inputFile:
            grid.append([x for x in line.strip()])

    seen = {}
    step = 0
    while step < limit:
        newGrid = copy.deepcopy(grid)
        for i in range(len(newGrid)):
            for j in range(len(newGrid[i])):
                curPos = complex(i, j)
                treeCount = 0
                lumbCount = 0
                for adj in {1, -1, -1j, 1j, 1+1j, 1-1j, -1+1j, -1-1j}:
                    adjPos = curPos + adj
                    adjPosx, adjPosy = int(adjPos.real), int(adjPos.imag)
                    if adjPosx in range(len(grid)) and adjPosy in range(len(grid[i])):
                        if grid[adjPosx][adjPosy] == '|':
                            treeCount += 1
                        if grid[adjPosx][adjPosy] == '#':
                            lumbCount += 1
                if grid[i][j] == '.' and treeCount >= 3:
                    newGrid[i][j] = '|'
                    continue
                if grid[i][j] == '|' and lumbCount >= 3:
                    newGrid[i][j] = '#'
                    continue
                if grid[i][j] == '#' and not(lumbCount >= 1 and treeCount >= 1):
                    newGrid[i][j] = '.'
                    continue
                newGrid[i][j] = grid[i][j]
        newGridFlatStr = ''.join(sum(newGrid, []))
        if newGridFlatStr in seen:
            leap = step - seen[newGridFlatStr]
            while step + leap < 1000000000:
                step += leap
        else:
            seen[newGridFlatStr] = step

        grid = newGrid
        step += 1
    flatGrid = sum(grid, [])
    return flatGrid.count('|') * flatGrid.count('#')

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(1000000000))
