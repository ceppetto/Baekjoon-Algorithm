N = int(input())
primeNumCnt = 0

num = list(map(int, input().split()))
for i in num:
    dividerCnt = 0

    for j in range(1, i + 1):
        if i % j == 0:
            dividerCnt += 1

    if dividerCnt == 2:
        primeNumCnt += 1

print(primeNumCnt)
