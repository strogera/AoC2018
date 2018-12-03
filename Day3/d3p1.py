import re
data = [[int(n) for n in re.split(",|:|@|x", line.replace('#', ''))] for line in open("input.txt", "r")]

countOverlap=set()
for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        x1, x1End=data[i][1], data[i][1]+data[i][3]
        x2, x2End=data[j][1], data[j][1]+data[j][3]
        y1, y1End=data[i][2], data[i][2]+data[i][4]
        y2, y2End=data[j][2], data[j][2]+data[j][4]
        overlapx=max(x1, x2)
        overlapxEnd=min(x1End, x2End)
        overlapy=max(y1, y2)
        overlapyEnd=min(y1End, y2End)
        for x in range(overlapx, overlapxEnd):
            for y in range(overlapy, overlapyEnd):
                countOverlap.add((x,y))
print(len(countOverlap))

