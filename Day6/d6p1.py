with open("input.txt", "r") as inputFile:
    data=inputFile.readlines()

points=[]
areas={}
for l in data:
    nums=list(map(int, l.strip().split(',')))
    points.append((nums[0], nums[1]))
    areas[tuple(nums)]=0
maxx=max(points, key=lambda k:k[0])[0]
minx=min(points, key=lambda k:k[0])[0]
maxy=max(points, key=lambda k:k[1])[1]
miny=min(points, key=lambda k:k[1])[1]
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        pointOfTwoAreas=False
        minDistance=-1
        for a, b in points:
            distance=abs(a-x)+abs(b-y)
            if distance==minDistance:
                pointOfTwoAreas=True
            elif minDistance==-1 or distance<minDistance:
                minDistance=distance
                minX , minY= a, b
                pointOfTwoAreas=False
        if not pointOfTwoAreas:
            if x!= minx and x !=maxx and y!=miny and y!=maxx:
                if (minX, minY) in areas:
                    areas[(minX, minY)]+=1
            else:
                #every point that is on the perimeter will be included in an point with an infinite area, so we can ignore that point
                areas.pop((minX, minY), None)
print(max(areas.values()))
