def populatedPositions(grid):
    return [(x, y) for x in range(len(grid)) for y in range(len(grid[x]))]

def isCart(grid, point):
    return grid[point[0]][point[1]] in {"v", ">", "<", "^"}

def pointsToComplexNumbers(listOfPoints):
    return list( map(lambda z: complex(*z), listOfPoints))

def pointsOfCarts(grid):
    return list( filter( lambda point: isCart(grid, point) , populatedPositions(grid)))

class Cart:
    def __init__(self, pos, symbol, id):
        self.symbol = symbol
        self.pos = pos
        self.id = id
        self.plusPos = []
        self.turnCount = 0

    def __hash__(self):
        return self.id

    def __lt__(self, other):
        if other.pos.real == self.pos.real:
            return self.pos.imag < other.pos.imag
        else:
            return self.pos.real < other.pos.real

    def move(self, direction):
        self.pos += direction

    def addPlus(self, pos):
        self.plusPos.append(pos)

    def getIntersectionTurn(self):
        self.turnCount += 1
        right = {'v':'<', '<': '^', '^': '>', '>':'v'}
        left = {'<': 'v', 'v':'>', '>': '^', '^':'<'}
        if self.turnCount%3 == 1:
            return left[self.symbol]
        elif self.turnCount%3 == 2:
            return self.symbol
        else:
            return right[self.symbol]

def changeSymbol(cart, dire):
    if cart == ">":
        if dire == "\\":
            return "v"
        elif dire == "/":
            return "^"
    elif cart == "<":
        if dire == "\\":
            return "^"
        elif dire == "/":
            return "v"
    elif cart == "v":
        if dire == "\\":
            return ">"
        elif dire == "/":
            return "<"
    elif cart == "^":
        if dire == "\\":
            return "<"
        elif dire == "/":
            return ">"
    return cart


def partOne():
    with open("input.txt", "r") as inputFile:
        grid = []
        nextMap = {'v': 1, '>': 1j, '<': -1j, '^': -1}
        for line in inputFile:
            elems=[ x for x in line]
            grid.append(elems)
        carts = [Cart(p,grid[int(p.real)][int(p.imag)], id) for id, p in enumerate(pointsToComplexNumbers(pointsOfCarts(grid)))]
        
        maxLoopSize = 1000000
        for _ in range(maxLoopSize):
            carts = sorted(carts)
            for c in carts:
                curChar = grid[int(c.pos.real)][int(c.pos.imag)]
                if curChar == '+':
                    c.symbol = c.getIntersectionTurn()
                elif curChar in {'|', '\\', '/', '-'}:
                    c.symbol = changeSymbol(c.symbol, curChar)
                c.move(nextMap[c.symbol])
                for c2 in carts:
                    if c2.pos == c.pos and c.id != c2.id:
                        return str(int(c.pos.imag)) + ',' + str(int(c.pos.real))
    print("Not Found")

def partTwo():
    with open("input.txt", "r") as inputFile:
        grid = []
        nextMap = {'v': 1, '>': 1j, '<': -1j, '^': -1}
        for line in inputFile:
            elems=[ x for x in line]
            grid.append(elems)
        carts = [Cart(p,grid[int(p.real)][int(p.imag)], id) for id, p in enumerate(pointsToComplexNumbers(pointsOfCarts(grid)))]
        
        maxLoopSize = 1000000
        for _ in range(maxLoopSize):
            carts = sorted(carts)
            cartsNew = sorted(carts)
            for c in carts:
                curChar = grid[int(c.pos.real)][int(c.pos.imag)]
                if curChar == '+':
                    c.symbol = c.getIntersectionTurn()
                elif curChar in {'|', '\\', '/', '-'}:
                    c.symbol = changeSymbol(c.symbol, curChar)
                c.move(nextMap[c.symbol])
                for c2 in carts:
                    if c2.pos == c.pos and c.id != c2.id:
                        cartsNew.remove(c2)
                        cartsNew.remove(c)
                        if len(cartsNew) == 1:
                            return print(str(int(cartsNew[0].pos.imag)) + ',' + str(int(cartsNew[0].pos.real)))
            carts = cartsNew

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
