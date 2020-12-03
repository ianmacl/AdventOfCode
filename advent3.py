with open("advent3.txt", "r") as fhandle:
    lines = [x.strip() for x in fhandle.readlines()]

regex = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

treeCounts = []
for (x, y) in slopes:
    currentX = 0
    currentY = 0
    numTrees = 0

    while currentY < len(lines):
        xCoord = currentX % len(lines[0])
        if lines[currentY][xCoord] is '#':
            numTrees += 1

        currentX += x
        currentY += y

    treeCounts.append(numTrees)

result = 1
for treeCount in treeCounts:
    result *= treeCount

print result