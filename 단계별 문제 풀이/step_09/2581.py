M = int(input())
N = int(input())
prime = []

for i in range(M, N + 1):
    dividerCnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            dividerCnt += 1
            if dividerCnt > 2:
                break

    if dividerCnt == 2:
        prime.append(i)

if len(prime) == 0:
    print("-1")
else:
    print(sum(prime))
    print(min(prime))