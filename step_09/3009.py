x = [0 for _ in range(0, 1000)]
y = [0 for _ in range(0, 1000)]

for i in range(3):
    coordinates = list(map(int, input().split()))
    x[coordinates[0] - 1] += 1
    y[coordinates[1] - 1] += 1

for i in range(1000):
    if x[i] == 1:
        print(i + 1, end=" ")

for j in range(1000):
    if y[j] == 1:
        print(j + 1)