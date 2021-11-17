def partOne():
    with open("input.txt", "r") as inputFile:
        numOfRecipies = int(inputFile.readlines()[0])
        elf1 = 0
        elf2 = 1
        recipe = '37'
        maxLoopSize = 1000000
        for _ in range(maxLoopSize):
            recipe += str(int(recipe[elf1])+int(recipe[elf2]))
            elf1 = (elf1 + int(recipe[elf1]) + 1)%len(recipe)
            elf2 = (elf2 + int(recipe[elf2]) + 1)%len(recipe)
            if(len(recipe) == numOfRecipies + 10):
                return recipe[-10:]


def partTwo():
    with open("input.txt", "r") as inputFile:
        recipeInput = inputFile.readlines()[0].strip()
        elf1 = 0
        elf2 = 1
        recipe = '37'
        while True:
            newRec = str(int(recipe[elf1])+int(recipe[elf2]))
            recipe += newRec
            elf1 = (elf1 + int(recipe[elf1]) + 1)%len(recipe)
            elf2 = (elf2 + int(recipe[elf2]) + 1)%len(recipe)
            if recipeInput in (recipe[-(len(recipeInput) + len(newRec)):]):
                return recipe.index(recipeInput)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
