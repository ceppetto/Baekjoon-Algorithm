import sys

hansooCnt = 0
num = int(sys.stdin.readline())

for i in range(1, num+1):
    if len(str(i)) == 1:
        hansooCnt += 1
    if len(str(i)) == 2:
        hansooCnt += 1
    if len(str(i)) == 3:
        firstNum = int(i / 100)
        secondNum = int((i / 10) % 10)
        thirdNum = int((i % 100) % 10)
        if (secondNum - firstNum) == (thirdNum - secondNum):
            hansooCnt += 1

print(hansooCnt)