from collections import deque

class Player:
    def __init__(self, pos, mode, att = 3, hp = 200):
        self.pos = pos
        self.hp = hp
        self.att = att
        self.mode = mode
        self.readingOrder = -1

    def getsAttacked(self, damage):
        self.hp -= damage

    def isDead(self):
        return self.hp <= 0

    def moveTo(self, newPos):
        self.pos = newPos

    def setReadingOrder(self, order):
        self.readingOrder = order

def getMovement(grid, player, enemies):
    #bfs
    adjPos = {'n': 1j, 's': -1j, 'w': -1, 'e': 1}
    targets = set()
    for enemy in enemies:
        for z in [enemy.pos + adjPos[a] for a in adjPos]:
            if grid[int(z.real)][int(z.imag)] == '.':
                targets.add(z)

    queue = deque()

    for x in sorted([player + adjPos[adj] for adj in adjPos], key = lambda k: (k.real, k.imag)):
        if grid[int(x.real)][int(x.imag)] == '.':
            queue.append(x)

    if len(targets) == 0 or len(queue) == 0:
        return player

    discovered = set()
    discovered.add(x for x in queue)
    depth = 1
    depthQueue = deque()
    for _ in range(len(queue)):
        depthQueue.append(1)
    path = deque()
    for x in queue:
        path.append([x])
    foundPaths = []
    shortestPath  = -1
    while queue:
        v = queue.popleft()
        curPath = path.popleft()
        depth = depthQueue.popleft()

        if shortestPath != -1:
            if depth > shortestPath:
                break
        if v in targets:
            foundPaths.append((curPath[0], v))
            shortestPath = depth

        for k in adjPos:
            adj = v + adjPos[k]
            if grid[int(adj.real)][int(adj.imag)] == '.':
                if adj not in discovered:
                    discovered.add(adj)
                    queue.append(adj)
                    depthQueue.append(depth + 1)
                    path.append(curPath + [adj])
    if foundPaths == []:
        return player
    return sorted(foundPaths, key = lambda k: (k[1].real, k[1].imag, k[0].real, k[0].imag))[0][0]

def attack(player, grid, enemies):
    adjPos = {'n': 1j, 's': -1j, 'w': -1, 'e': 1}
    candidateTargets = []
    playerAdjPos = set(player.pos + adjPos[k] for k in adjPos)
    for attackingTarget in enemies:
        if attackingTarget.pos in playerAdjPos:
            candidateTargets.append(attackingTarget)
    if candidateTargets == []:
        return False
    finalAttackingTarget = sorted(candidateTargets, key = lambda k: (k.hp, k.readingOrder))[0]
    finalAttackingTarget.getsAttacked(player.att)
    if finalAttackingTarget.isDead():
        grid[int(finalAttackingTarget.pos.real)][int(finalAttackingTarget.pos.imag)] = '.'
        enemies.remove(finalAttackingTarget)
    return True

def partOne():
    with open("input.txt", "r") as inputFile:
        grid = []
        for line in inputFile:
            grid.append([c for c in line.strip()])

        elves = []
        goblins = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'E':
                    curPlayer = Player(complex(i, j), "elf")
                    elves.append(curPlayer)
                elif grid[i][j] == 'G':
                    curPlayer = Player(complex(i, j), "goblin")
                    goblins.append(curPlayer)
        roundCounter = 0
        while True:
            playingOrder = sorted(elves + goblins, key = lambda x: (x.pos.real, x.pos.imag))
            for i, p in enumerate(playingOrder):
                p.setReadingOrder(i)

            earlyStop = False
            for j, player in enumerate(playingOrder):
                if player.isDead():
                    continue
                if not attack(player, grid, goblins if player.mode == "elf" else elves):
                    newPos = getMovement(grid, player.pos, goblins if player.mode == "elf" else elves)
                    grid[int(newPos.real)][int(newPos.imag)] = grid[int(player.pos.real)][int(player.pos.imag)]
                    if player.pos != newPos:
                        grid[int(player.pos.real)][int(player.pos.imag)] = '.'
                    player.moveTo(newPos)
                    attack(player, grid, goblins if player.mode == "elf" else elves)

                if (len(elves) == 0 or len(goblins) == 0):
                    if j < len(playingOrder)-1:
                        earlyStop = True
                        break
            if earlyStop:
                break
            roundCounter += 1
        return roundCounter * sum(x.hp for x in elves + goblins)


def partTwo():
    with open("input.txt", "r") as inputFile:
        grid = []
        for line in inputFile:
            grid.append([c for c in line.strip()])

        elves = []
        goblins = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'E':
                    curPlayer = Player(complex(i, j), "elf")
                    elves.append(curPlayer)
                elif grid[i][j] == 'G':
                    curPlayer = Player(complex(i, j), "goblin")
                    goblins.append(curPlayer)
        origElves = elves
        origGoblins = goblins
        origGrid = grid
        c = 0
        while True:
            goblins = [Player(x.pos, x.mode) for x in origGoblins]
            elves = [Player(x.pos, x.mode, 4+c) for x in origElves]
            grid = [[x for x in row] for row in origGrid]
            c += 1
            roundCounter = 0
            while len(elves) == len(origElves) and len(goblins) > 0:

                playingOrder = sorted(elves + goblins, key = lambda x: (x.pos.real, x.pos.imag))
                for i, p in enumerate(playingOrder):
                    p.setReadingOrder(i)

                earlyStop = False
                for j, player in enumerate(playingOrder):
                    if player.isDead():
                        continue
                    if not attack(player, grid, goblins if player.mode == "elf" else elves):
                        newPos = getMovement(grid, player.pos, goblins if player.mode == "elf" else goblins)
                        grid[int(newPos.real)][int(newPos.imag)] = grid[int(player.pos.real)][int(player.pos.imag)]
                        if player.pos != newPos:
                            grid[int(player.pos.real)][int(player.pos.imag)] = '.'
                        player.moveTo(newPos)

                        attack(player, grid, goblins if player.mode == "elf" else elves)

                    if (len(elves) != len(origElves)  or len(goblins) == 0):
                        if j < len(playingOrder)-1:
                            earlyStop = True
                            break

                if earlyStop:
                    break

                roundCounter += 1
            if len(goblins) == 0:
                break

    return roundCounter * sum(x.hp for x in elves)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
