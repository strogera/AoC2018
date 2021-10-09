class TreeNode:
    childs = []
    metadata = []

    def __init__(self, childs, metadata):
        self.childs = childs
        self.metadata = [int(x) for x in metadata]

    def metaDataSum(self):
        return sum(self.metadata)

def makeTree(elems):
    if elems == []:
        return None
    childCount = elems.pop(0)
    metaDataCount = elems.pop(0)
    childs = []
    for _ in range(int(childCount)):
        childs.append(makeTree(elems))
    metadata = []
    for _ in range(int(metaDataCount)):
        metadata.append(elems.pop(0))
    return TreeNode(childs, metadata)
    
def getSumOfTree(root):
    if root == None:
        return 0
    return root.metaDataSum() + sum([getSumOfTree(child) for child in root.childs])


def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            elems=line.strip().split()
        treeRoot = makeTree(elems)
        return getSumOfTree(treeRoot)

def numOfNode(node):
    if node == None:
        return 0
    if len(node.childs) == 0:
        return node.metaDataSum()
    summ = 0
    for index in node.metadata:
        if index - 1 not in range(len(node.childs)):
            continue
        summ += numOfNode(node.childs[index - 1])
    return summ

def partTwo():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            elems=line.strip().split()
        treeRoot = makeTree(elems)
        return numOfNode(treeRoot)

print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
