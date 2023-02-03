import sys
n = int(input())
resScore = [sys.stdin.readline() for _ in range(n)]

sumScore = 0 # 총점을 위한 변수
cnt = 1 # O의 개수를 세기 위한 변수

for i in range(n):
    strValue = resScore[i]
    for j in range(len(strValue)):
        if 'O' == strValue[j]:
            sumScore += cnt
            cnt += 1
        else:
            cnt = 1
    resScore[i] = str(sumScore)
    sumScore = 0

for i in range(n):
    print(int(resScore[i]))
