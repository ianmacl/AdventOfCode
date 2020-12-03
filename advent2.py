import re

with open("advent2.txt", "r") as fhandle:
    lines = [x.strip() for x in fhandle.readlines()]

regex = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'

validPasswords = 0
for line in lines:
    match = re.search(regex, line)
    minNum = int(match.group(1))
    maxNum = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    results = re.findall(letter, password)
    numResults = len(results)
    print minNum
    print maxNum
    print numResults
    print ""
    if numResults >= minNum and numResults <= maxNum:
        print "added"
        validPasswords += 1

print validPasswords

validPasswords = 0

for line in lines:
    match = re.search(regex, line)
    minNum = int(match.group(1))
    maxNum = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    numMatching = 0
    if password[minNum - 1] == letter:
        numMatching += 1
    if password[maxNum - 1] == letter:
        numMatching += 1

    if numMatching == 1:
        validPasswords += 1

print validPasswords