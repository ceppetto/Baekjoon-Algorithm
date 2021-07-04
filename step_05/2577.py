import sys

n1, n2, n3 = [int(sys.stdin.readline()) for i in range(3)]
strValue = str(n1 * n2 * n3)
listValue = [0 for i in range(10)]

for i in range(len(strValue)):
    x = int(strValue[i])
    listValue[x] += 1

for i in range(10):
    print(listValue[i], end="\n")
