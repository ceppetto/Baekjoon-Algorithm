import sys
import math
num = int(sys.stdin.readline())
num_list = list(range(2, 123456 * 2))
prime_list = []

def prime(n):
    if n == 1:
        return False
    else:
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                return False
        return True


for i in num_list:
    if prime(i):
        prime_list.append(i)

while num != 0:
    count = 0
    for i in prime_list:
        if num < i <= num * 2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())
