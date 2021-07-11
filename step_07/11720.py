import sys
n = sys.stdin.readline()
nList = list(sys.stdin.readline())
totalSum = 0
for i in nList:
    if i != '\n':
        totalSum += int(i)

print(totalSum)