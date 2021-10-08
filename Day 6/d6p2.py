with open("input.txt", "r") as inputFile:
    data=inputFile.readlines()

points=[]
areas={}
for l in data:
    nums=list(map(int, l.strip().split(',')))
    points.append((nums[0], nums[1]))
maxx=max(points, key=lambda k:k[0])[0]
minx=min(points, key=lambda k:k[0])[0]
maxy=max(points, key=lambda k:k[1])[1]
miny=min(points, key=lambda k:k[1])[1]
count=0
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        sumDistance=0
        for a, b in points:
            sumDistance+=abs(a-x)+abs(b-y)
        if sumDistance<10000:
            count+=1
print(count)
