T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    f = [i for i in range(1, n+1)]
    for j in range(k):
        for k in range(1, n):
            f[k] += f[k-1]

    print(f[-1])