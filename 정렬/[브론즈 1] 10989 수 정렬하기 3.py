import sys
n = int(sys.stdin.readline().rstrip())
count = [0] * 10001

for i in range(n):
    index = int(sys.stdin.readline().rstrip())
    count[index] += 1

for i in range(len(count)):
    if count[i] == 0:
        continue
    for j in range(count[i]):
        print(i)
