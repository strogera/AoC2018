freq=0
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        freq+=int(line)
print(freq)

