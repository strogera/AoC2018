from copy import deepcopy

class Group():
    def __init__(self, mode, numOfUnits, hp, attDmg, initiative):
        self.numOfUnits = numOfUnits
        self.hp = hp
        self.attDmg = attDmg
        self.initiative = initiative
        self.weaknesses = []
        self.immunities = []
        self.mode = mode
        self.damageType = None

    def effectivePower(self):
        if self.numOfUnits <= 0:
            return 0
        return self.numOfUnits * self.attDmg

    def addWeakness(self, weakness):
        self.weaknesses.append(weakness)

    def addImmunity(self, immunity):
        self.immunities.append(immunity)

    def setDamageType(self, ttype):
        self.damageType = ttype

    def getsAttacked(self, dmg):
        if dmg == 0:
            return
        self.numOfUnits -= dmg//self.hp
        if self.numOfUnits < 0 :
            self.numOfUnits = 0

def calcDamage(attackingGroup, defendingGroup):
    if attackingGroup.damageType in defendingGroup.immunities:
        return 0
    damage = attackingGroup.effectivePower()
    if attackingGroup.damageType in defendingGroup.weaknesses:
        return 2 * damage
    return damage


def partOne():
    with open("input.txt", "r") as inputFile:
        immuneSystemGroupList = []
        infectionGroupList = []
        mode = None
        for line in inputFile:
            nums = [int(s) for s in line.split() if s.isdigit()]
            if nums:
                assert(mode != None)
                groupList = immuneSystemGroupList if mode == 0 else infectionGroupList
                groupList.append(Group(mode, *nums))
                for ll in (line[line.find("(")+1:line.find(")")]).split(';'):
                        ll = ll.strip()
                        if 'weak' in ll.lower():
                            for ttype in ll[len('weak to '):].split(', '):
                                groupList[-1].addWeakness(ttype)
                        else:
                            for ttype in ll[len('immune to '):].split(', '):
                                groupList[-1].addImmunity(ttype)
                groupList[-1].setDamageType(line.split(' ')[-5])
            else:
                if 'infection:' in line.lower():
                    mode = 1
                elif 'system:' in line.lower():
                    mode = 0

        while immuneSystemGroupList and infectionGroupList:
            fightPairs = []
            matched = set()
            for attacker in sorted(immuneSystemGroupList + infectionGroupList, key = lambda k: (k.effectivePower(),  - k.initiative), reverse=True):
                if attacker.mode == 0:
                    targets =  set(infectionGroupList) - matched
                else:
                    targets = set(immuneSystemGroupList) - matched
                if len(targets) == 0:
                    continue
                target = max(targets, key = lambda defender: (calcDamage(attacker, defender), defender.effectivePower(), - defender.initiative))
                if calcDamage(attacker, target) > 0:
                    fightPairs.append((attacker, target))
                    matched.add(target)
            for attacker, defender in sorted(fightPairs, key = lambda k: (k[0].initiative), reverse=True):
                if attacker.numOfUnits <= 0  or defender.numOfUnits <= 0:
                    continue
                defender.getsAttacked(calcDamage(attacker, defender))
                if defender.numOfUnits <= 0:
                    if defender.mode == 1:
                        if defender in infectionGroupList:
                            infectionGroupList.remove(defender)
                    else:
                        if defender in immuneSystemGroupList:
                            immuneSystemGroupList.remove(defender)
        return sum(map(lambda k: k.numOfUnits, immuneSystemGroupList)) if immuneSystemGroupList else sum(map(lambda k: k.numOfUnits, infectionGroupList))


def partTwo():
    with open("input.txt", "r") as inputFile:
        immuneSystemGroupList = []
        infectionGroupList = []
        mode = None
        for line in inputFile:
            nums = [int(s) for s in line.split() if s.isdigit()]
            if nums:
                assert(mode != None)
                groupList = immuneSystemGroupList if mode == 0 else infectionGroupList
                groupList.append(Group(mode, *nums))
                for ll in (line[line.find("(")+1:line.find(")")]).split(';'):
                        ll = ll.strip()
                        if 'weak' in ll.lower():
                            for ttype in ll[len('weak to '):].split(', '):
                                groupList[-1].addWeakness(ttype)
                        else:
                            for ttype in ll[len('immune to '):].split(', '):
                                groupList[-1].addImmunity(ttype)
                groupList[-1].setDamageType(line.split(' ')[-5])
            else:
                if 'infection:' in line.lower():
                    mode = 1
                elif 'system:' in line.lower():
                    mode = 0

        origImmuneList = deepcopy(immuneSystemGroupList)
        origInfList = deepcopy(infectionGroupList)
        boost = 1
        while True:
            boost += 1
            immuneSystemGroupList = deepcopy(origImmuneList)
            if immuneSystemGroupList == []:
                return
            infectionGroupList = deepcopy(origInfList)
            for imm in immuneSystemGroupList:
                imm.attDmg += boost
            while immuneSystemGroupList and infectionGroupList:
                fightPairs = []
                matched = set()
                immuneSum = sum(map(lambda k: k.numOfUnits, immuneSystemGroupList))
                infSum = sum(map(lambda k: k.numOfUnits, infectionGroupList))
                for attacker in sorted(immuneSystemGroupList + infectionGroupList, key = lambda k: (k.effectivePower(),  - k.initiative), reverse=True):
                    if attacker.mode == 0:
                        targets =  set(infectionGroupList) - matched
                    else:
                        targets = set(immuneSystemGroupList) - matched
                    if len(targets) == 0:
                        continue
                    target = max(targets, key = lambda defender: (calcDamage(attacker, defender), defender.effectivePower(), - defender.initiative))
                    if calcDamage(attacker, target) > 0:
                        fightPairs.append((attacker, target))
                        matched.add(target)
                for attacker, defender in sorted(fightPairs, key = lambda k: (k[0].initiative), reverse=True):
                    if attacker.numOfUnits <= 0  or defender.numOfUnits <= 0:
                        continue
                    defender.getsAttacked(calcDamage(attacker, defender))
                    if defender.numOfUnits <= 0:
                        if defender.mode == 1:
                            if defender in infectionGroupList:
                                infectionGroupList.remove(defender)
                        else:
                            if defender in immuneSystemGroupList:
                                immuneSystemGroupList.remove(defender)
                if immuneSum == sum(map(lambda k:k.numOfUnits, immuneSystemGroupList)) and infSum == sum(map(lambda k : k.numOfUnits, infectionGroupList)):
                    break
            if not infectionGroupList and immuneSystemGroupList:
                return sum(map(lambda k: k.numOfUnits, immuneSystemGroupList))

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
