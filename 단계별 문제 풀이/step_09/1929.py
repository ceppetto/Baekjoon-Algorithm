M, N = list(map(int, input().split()))


def is_prime(n):
    if n == 1:
        return False
    else:
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                return False
        return True


for i in range(M, N + 1):
    if is_prime(i):
        print(i)
