class Point:
    def __init__(self, pos, vel = [0, 0]):
        self.posX = pos[0]
        self.posY = pos[1]
        self.velX = vel[0]
        self.velY = vel[1]

    def __eq__(self, p):
        return self.posX == p.posX and self.posY == p.posY



class Image:

    def __init__(self):
        self.points = []
        self.time = 0
        self.maxX = -999999
        self.maxY = -999999
        self.minX = 999999
        self.minY = 999999

    def addPoint(self, point):
        self.points.append(point)

    def clickTime(self):
        self.maxX = -999999
        self.maxY = -999999
        self.minX = 999999
        self.minY = 999999

        self.time += 1

        for point in self.points:
            point.posX += point.velX
            if point.posX > self.maxX:
                self.maxX = point.posX
            if point.posX < self.minX:
                self.minX = point.posX
            point.posY += point.velY
            if point.posY > self.maxY:
                self.maxY = point.posY
            if point.posY < self.minY:
                self.minY = point.posY

    def printImage(self):
        for point in self.points:
            if not(Point([point.posX+1, point.posY]) in self.points or (
             Point([point.posX+1, point.posY+1]) in self.points) or (
             Point([point.posX, point.posY+1]) in self.points) or (
             Point([point.posX-1, point.posY]) in self.points) or (
             Point([point.posX-1, point.posY-1]) in self.points) or (
             Point([point.posX, point.posY-1]) in self.points) or (
             Point([point.posX+1, point.posY-1]) in self.points) or (
             Point([point.posX-1, point.posY+1]) in self.points)):
             return -1

        rX = self.maxX - self.minX
        rY = self.maxY - self.minY
        print("Answer for part 1: ")
        for y in range(rY + 1):
            line = []
            for x in range(rX + 1):
                if Point([x+ self.minX, y + self.minY], [0,0]) in self.points:
                    line.append('#')
                else:
                    line.append(".")
            print(''.join(line))
        return self.time


def partOne(part2):
    with open("input.txt", "r") as inputFile:
        image = Image()
        for line in inputFile:
            line = line.strip().replace("<", ">")
            posvel = line.split(">")
            pos = [ int(x) for x in posvel[1].split(",") ]
            vel = [ int(x) for x in posvel[3].split(",") ]
            image.addPoint(Point(pos, vel))

        while True:
            image.clickTime()
            time = image.printImage()
            if time != -1:
                if part2:
                    print("Answer for part 2: ")
                    print(time)
                break

partOne(True)