with open("input.txt", "r") as inputFile:
    inputD=[x for x in inputFile]
inputD.sort()
guardId=int()
guardsDic={}
for line in inputD:
    logTime=int(line[15:17])
    if line[19]=='G':
        getId=line[19:].split(' ')
        guardId=int(getId[1][1:])
    elif line[19]=='f':
        sleepTimeStarts=logTime
    elif line[19]=='w':
        sleepTimeEnds=logTime-1
        sleepTime=sleepTimeEnds-sleepTimeStarts
        if guardId in guardsDic:
            guardsDic[guardId]+=sleepTime
        else:
            guardsDic[guardId]=sleepTime
maxAsleepId=max(guardsDic.keys(), key=lambda k:guardsDic[k])

minuteDic={}
for line in inputD:
    logTime=int(line[15:17])
    if line[19]=='G':
        getId=line[19:].split(' ')
        guardId=int(getId[1][1:])
    elif line[19]=='f':
        sleepTimeStarts=logTime
    elif line[19]=='w':
        if guardId==maxAsleepId:
            for x in range(sleepTimeStarts, logTime):
                if x in minuteDic:
                    minuteDic[x]+=1
                else:
                    minuteDic[x]=1
maxTimesMinuteAsleep=max(minuteDic.keys(), key=lambda k:minuteDic[k])
print(maxTimesMinuteAsleep*maxAsleepId)

