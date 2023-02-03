import sys
avgRatio = []

testNum = int(input())

for i in range(testNum):
    avgScore = 0
    overAvgNum = 0
    studentNum, *scoreList = map(int, sys.stdin.readline().split())
    avgScore = sum(scoreList) / len(scoreList)
    for score in scoreList:
        if score > avgScore:
            overAvgNum += 1
    avgScore = 100*(overAvgNum / studentNum)
    print(str('{:.3f}'.format(avgScore)) + "%")

