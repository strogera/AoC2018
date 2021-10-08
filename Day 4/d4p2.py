with open("input.txt", "r") as inputFile:
    inputD=[x for x in inputFile]
inputD.sort()
d={}
for line in inputD:
    logTime=int(line[15:17])
    if line[19]=='G':
        getId=line[19:].split(' ')
        guardId=int(getId[1][1:])
    elif line[19]=='f':
        sleepTimeStarts=logTime
    elif line[19]=='w':
        for x in range(sleepTimeStarts, logTime):
            if (guardId, x) in d:
                d[(guardId, x)]+=1
            else:
                d[(guardId, x)]=1
z=max(d.keys(), key=lambda k:d[k])
print(z[0]*z[1])

