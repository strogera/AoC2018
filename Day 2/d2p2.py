def compareStrings(s1, s2):
    diff=0
    for i in range(0, len(s1)):
        if s1[i]!=s2[i]:
            diff+=1
    return diff

data=[]
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        data.append(line[:-1])
for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        diffs=compareStrings(data[i], data[j])
        if diffs==1:
            print(''.join([x for x, y in zip(data[i], data[j]) if x==y]))
            exit()


                
