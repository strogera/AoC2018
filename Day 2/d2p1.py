dic={}
countTwoTimes=0
countThreeTimes=0
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        dic.clear()
        for letter in line:
            if letter=='\n':
                continue
            if letter in dic:
                dic[letter]+=1
            else:
                dic[letter]=1
        twoFlag=True
        threeFlag=True
        for key, value in dic.items():
            if value==2 and twoFlag:
                countTwoTimes+=1
                twoFlag=False
            if value==3 and threeFlag:
                countThreeTimes+=1
                threeFlag=False
print(countTwoTimes*countThreeTimes)

