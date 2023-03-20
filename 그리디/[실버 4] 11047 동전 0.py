import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))
num.sort(reverse=True)
count = 0

for i in num:
    if k >= i:
        count += k // i
        k %= i

print(count)
