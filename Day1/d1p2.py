calcFrequences={0}
curFreq=0
freqList=[]
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        freqList.append(int(line))
while True:
    for freq in freqList:
        curFreq+=freq
        if curFreq in calcFrequences:
            print(curFreq)
            exit()
        else:
            calcFrequences.add(curFreq)

