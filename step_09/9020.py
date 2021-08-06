import sys
import math

T = int(sys.stdin.readline())

all_num = list(range(2, 10000))
prime_num = []


def prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


for i in all_num:
    if prime(i):
        prime_num.append(i)

for _ in range(T):
    n1 = 0
    n2 = 0
    num = int(sys.stdin.readline())
    for k in prime_num:
        if k <= num / 2:
            if num - k in prime_num:
                n1 = k
                n2 = num - k
        else:
            break
    print(n1, n2)
