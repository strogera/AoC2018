def phase1(string):
    charStack=[]
    for c in string.strip():
        if not charStack:
            charStack.append(c)
        else:
            if c!=charStack[-1] and c.lower()==charStack[-1].lower():
                charStack.pop(-1)
            else:
                charStack.append(c)
    return(len(charStack))

    
with open("input.txt", "r") as inputFile:
    string=inputFile.read()
charStack=[]

letters=set()
for c in string.strip():
    letters.add(c.lower())

minLength=-1
curLength=0
for l in letters:
    curString=string.replace(l, '').replace(l.upper(), '')
    curLength=phase1(curString)
    if minLength==-1:
        minLength=curLength
    else:
        minLength=min(minLength, curLength)
print(minLength)

