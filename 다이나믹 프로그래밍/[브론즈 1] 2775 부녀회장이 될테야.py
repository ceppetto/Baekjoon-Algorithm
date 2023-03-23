apt = []
for i in range(15):
    floor = []
    for j in range(15):
        if i == 0:
            floor.append(j)
        else:
            floor.append(0)
    apt.append(floor)
    
for i in range(1, 15):
    for j in range(1, 15):
        apt[i][j] = apt[i - 1][j] + apt[i][j - 1]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    print(apt[k][n])
