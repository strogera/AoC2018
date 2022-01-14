def manhattanDistance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def partOne():
    with open("input.txt", "r") as inputFile:
        points = []
        for line in inputFile:
            points.append(tuple(map(int, line.split(','))))

        constellations = {}
        c = 1
        while True:
            found = False
            for i in range(len(points)):
                if points[i] not in constellations:
                    c += 1
                    constellations[points[i]] = c
                for j in range(i + 1, len(points)):
                    if manhattanDistance(points[i], points[j]) <= 3:
                        if points[j] in constellations:
                            if constellations[points[j]] != constellations[points[i]]:
                                found = True
                                for p in constellations.keys():
                                    if constellations[p] == constellations[points[j]]:
                                        constellations[p] = constellations[points[i]]
                        else:
                            constellations[points[j]] = constellations[points[i]]
                    else:
                        if points[j] not in constellations:
                            c += 1
                            constellations[points[j]] = c
            if not found:
                break
        return len(set(constellations.values()))





def partTwo():
    return 'Click the button on the site after getting all the other 49 stars'

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
