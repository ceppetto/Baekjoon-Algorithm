import sys
N = int(input())
score = list(map(int, (sys.stdin.readline().split())))
M = max(score)
sumScore = 0
for i in range(N):
    sumScore += score[i] / M * 100

print(sumScore / N)