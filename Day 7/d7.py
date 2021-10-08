from collections import defaultdict
import string

def partOne():
    with open("input.txt", "r") as inputFile:
        orderRestrictionsDict = defaultdict(list)
        orderRestrictionsReverseDict = defaultdict(list)

        for line in inputFile:
            orderRestrictionsDict[line[5]].append(line[36])
            orderRestrictionsReverseDict[line[36]].append(line[5])

        available = set(orderRestrictionsDict) - set(orderRestrictionsReverseDict)
        correctOrder = []
        while(len(orderRestrictionsReverseDict) > 0):
            if len(available) == 0:
                break
            current = sorted(list(available))[0]
            correctOrder.append(current)
            available.remove(current)
            if current in orderRestrictionsReverseDict:
                del orderRestrictionsReverseDict[current]
            for key in orderRestrictionsReverseDict:
                if(current in orderRestrictionsReverseDict[key]):
                    orderRestrictionsReverseDict[key].remove(current)
            for key in orderRestrictionsReverseDict:
                if len(orderRestrictionsReverseDict[key]) == 0:
                    available.add(key)
        return ''.join(correctOrder)


class Worker:
    timer = 0
    task = ""

    def assign(self, task, duration):
        self.task = task
        self.timer = duration

    def reset(self):
        self.timer = 0
        self.task = ""
    
    def click(self):
            self.timer -= 1 if self.timer > 0 else 0

    def taskEnded(self):
        return self.timer == 0 and self.task != ""

    def isAvailable(self):
        return self.timer == 0 and self.task == ""


def partTwo(workersNumber):
    with open("input.txt", "r") as inputFile:
        orderRestrictionsDict = defaultdict(list)
        orderRestrictionsReverseDict = defaultdict(list)

        for line in inputFile:
            orderRestrictionsDict[line[5]].append(line[36])
            orderRestrictionsReverseDict[line[36]].append(line[5])

        available = set(orderRestrictionsDict) - set(orderRestrictionsReverseDict)
        second = 0 
        workers = [Worker() for _ in range(workersNumber)] 

        assigned = set()
        while available:
            for worker in workers:
                worker.click()
                if worker.taskEnded():
                    current = worker.task
                    available.remove(current)
                    worker.reset()
                    assigned.remove(current)
                    if current in orderRestrictionsReverseDict:
                        del orderRestrictionsReverseDict[current]
                    for key in orderRestrictionsReverseDict:
                        if(current in orderRestrictionsReverseDict[key]):
                            orderRestrictionsReverseDict[key].remove(current)
                    for key in orderRestrictionsReverseDict:
                        if len(orderRestrictionsReverseDict[key]) == 0:
                            available.add(key)
                if worker.isAvailable():
                    for current in sorted(available):
                        if current not in assigned:
                            worker.assign(current, 60 + string.ascii_lowercase.index(current.lower()) + 1)
                            assigned.add(current)
                            break
            second += 1
        return second - 1

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo(5))
