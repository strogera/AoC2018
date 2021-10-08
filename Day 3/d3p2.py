import re
data = [[int(n) for n in re.split(",|:|@|x", line.replace('#', ''))] for line in open("input.txt", "r")]

for i in range(0, len(data)):
    countNoOverlap=0
    for j in range(0, len(data)):
        x1, x1End=data[i][1], data[i][1]+data[i][3]
        x2, x2End=data[j][1], data[j][1]+data[j][3]
        y1, y1End=data[i][2], data[i][2]+data[i][4]
        y2, y2End=data[j][2], data[j][2]+data[j][4]
        overlapx=max(x1, x2)
        overlapxLength=min(x1End, x2End)-overlapx
        overlapy=max(y1, y2)
        overlapyLength=min(y1End, y2End)-overlapy
        if overlapxLength<=0 or overlapyLength<=0:
            countNoOverlap+=1
        else: 
            if j != i:
                break
    if countNoOverlap==len(data)-1:
        print(data[i][0])
        exit()

