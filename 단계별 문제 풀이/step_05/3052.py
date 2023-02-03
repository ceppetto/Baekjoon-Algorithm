n = list(map(int, [input() for i in range(10)]))
r = [0 for i in range(1000)]

for i in range(10):
    x = n[i] % 42
    r[x] += 1

cnt = 0
for i in range(1000):
    if r[i] == 10:
        cnt = 1
        break
    if r[i] > 0:
        cnt += 1

print(cnt)