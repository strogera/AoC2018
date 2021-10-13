class Marble:
    def __init__(self, id):
        self.id = id
        self.prev = self
        self.next = self

    def addAfter(self, newMarble):
        oldnext = self.next
        oldnext.prev = newMarble
        self.next = newMarble
        newMarble.next = oldnext
        newMarble.prev = self
        return newMarble
    
    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


def partOne(part2 = False):
    with open("input.txt", "r") as inputFile:
        players = 0
        targetMarble = 0
        for line in inputFile:
            elems=line.strip().split()
            players = int(elems[0])
            targetMarble = int(elems[-2])
        currentMarble = Marble(0)
        scores = {}
        for p in range(players):
            scores[p] = 0
        if part2:
            targetMarble *= 100
        for turn in range(1, targetMarble+1):
            if turn % 23 == 0:
                scores[turn%players] += turn
                for _ in range(7):
                    currentMarble = currentMarble.prev
                scores[turn%players] += currentMarble.id
                currentMarble = currentMarble.delete()
            else:
                for _ in range(1):
                    currentMarble = currentMarble.next
                currentMarble = currentMarble.addAfter(Marble(turn))
        return max(scores.values())
                

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(True))