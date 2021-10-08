with open("input.txt", "r") as inputFile:
    string=inputFile.read()

charStack=[]
for c in string.strip():
    if not charStack:
        charStack.append(c)
    else:
        if c!=charStack[-1] and c.lower()==charStack[-1].lower():
            charStack.pop(-1)
        else:
            charStack.append(c)
print(len(charStack))

   
