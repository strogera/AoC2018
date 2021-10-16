def getWithoutTrailingDots(state):
    stateWithout = ""
    removeDots = True
    for i in range(len(state)):
        if removeDots and state[i] == ".":
            continue
        removeDots = False
        stateWithout += state[i]
    for i in range(len(state)-1, 0, -1):
        if state[i] == ".":
            stateWithout = stateWithout[:-1]
        else:
            break
    return stateWithout

def getCount(state, ptr):
    count = 0
    for i in range(len(state)):
        if state[i] == '#':
            count += i - ptr
    return count

def partOne(gens = 20):
    with open("input.txt", "r") as inputFile:
        rules = {}
        state = ""
        for line in inputFile:
            if "initial" in line:
                state = line.split()[-1].strip()
            elif "=>" in line:
                tmp = line.split()
                before = tmp[0].strip()
                to = tmp[-1].strip()
                rules[before] = to
        ptr = 0
        for j in range(gens):
            ptrPrev = ptr
            if state[:3] != "...":
                state = "..." + state 
                ptr += 3
            if state[:-3] != "...":
                state += "..."

            newState = "" 

            for i in range(len(state)):
                if state[i-2:i+3] in rules:
                    newState += rules[state[i-2:i+3]]
                else:
                    newState += "."

            if getWithoutTrailingDots(state) == getWithoutTrailingDots(newState):
                # there's a pattern that keeps happening and won't change after that
                # the count becomes linaer so we can just calculate it
                # for the remaining repetitions
                multiplier = gens - j 
                oldCount = getCount(state, ptrPrev)
                newCount = getCount(newState, ptr)
                return oldCount + (newCount - oldCount)*multiplier
            state = newState 
        return getCount(state, ptr) 

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partOne(50000000000))
