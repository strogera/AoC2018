def fillLeft(grid, x, ystart):
    i = ystart - 1
    while i >= 0:
        if grid[x][i] == '#':
            return (-1, -1)
        else:
            if grid[x][i] == '.' or grid[x][i] == '|':
                grid[x][i] = '|'
                if x + 1 >= len(grid) or (grid[x+1][i] == '.' or grid[x+1][i] == '|'):
                    break
            else:
                break
        i -= 1
    return (x, i)

def fillRight(grid, x, ystart):
    i = ystart + 1
    while i < len(grid[x]):
        if grid[x][i] == '#':
            return (-1, -1)
        else:
            if grid[x][i] == '.' or grid[x][i] == '|':
                grid[x][i] = '|'
                if x + 1 >= len(grid) or grid[x+1][i] == '.':
                    break
            else:
                break
        i += 1
    return (x, i)

def fillDrop(grid, xstart, y):
    stack = [(xstart, y)]
    for i in range(xstart+1, len(grid)):
        if grid[i][y] == '.':
            grid[i][y] = '|'
            stack.append((i, y))
        else:
            if grid[i][y] == '|' :
                return
            while stack and fillRow(grid, *stack.pop()):
                pass
            if grid[i][y] == '#' or grid[i][y] == '~':
                break

def flood(grid, i, j):
    z = j + 1
    while grid[i][z] == '|':
        if grid[i+1][z] == '~' or grid[i+1][z] == '#':
            grid[i][z] = '~'
        z += 1
    z = j
    while grid[i][z] == '|':
        if grid[i+1][z] == '~' or grid[i+1][z] == '#':
            grid[i][z] = '~'
        z -= 1

def fillRow(grid, i, j):
    if i == (len(grid) - 1):
        return False
    wall, _  = fillRight(grid, i, j)
    wall2, _ = fillLeft(grid, i, j)
    if wall == -1 and wall2 == -1:
        flood(grid, i, j)
        return True
    return False


def fill(grid):
    curSpring = getSpring(grid)
    while curSpring:
        fillDrop(grid, curSpring[0], curSpring[1])
        curSpring = getSpring(grid)

def countWater(grid, partTwo = False):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '~':
                count += 1
            if not partTwo and grid[i][j] == '|':
                    count += 1
    return count

def getSpring(grid):
    for i in range(len(grid) - 2):
        for j in range(len(grid[i])):
            if grid[i][j] == '|' and (grid[i+1][j] == '.' or isFloodedBelow(grid, i, j)):
                return (i, j)
    return None


def isFloodedBelow(grid, i, j):
    return grid[i+1][j] == '~' and (grid[i][j+1] == '.' or grid[i][j-1] == '.')

def partOne(partTwo = False):
    with open("input.txt", "r") as inputFile:
        clayPos = set()
        for line in inputFile:
            a, b = line.strip().split(',')

            xrange = ''
            yrange = ''
            if 'x' in b:
                xrange = b.split('=')[-1]
            else:
                yrange = b.split('=')[-1]

            if 'y' in a:
                xmin, xmax = xrange.split('..')
                y = int(a.split('=')[-1])
                for i in range(int(xmin), int(xmax) + 1):
                    clayPos.add((i, y))
            if 'x' in a:
                ymin, ymax = yrange.split('..')
                x = int(a.split('=')[-1])
                for i in range(int(ymin), int(ymax) + 1):
                    clayPos.add((x, i))
        grid = []
        maxy = max(clayPos, key = lambda k: k[1])[1]
        miny = min(clayPos, key = lambda k: k[1])[1]
        maxx = max(clayPos, key= lambda k: k[0])[0]
        for y in range(0, maxy + 1):
            grid.append([])
            for x in range(0, maxx + 2):
                grid[-1].append('.' if (x, y) not in clayPos else '#')

        grid[0][500] = '|'
        fill (grid)
        return countWater(grid[miny:], partTwo)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(True))
