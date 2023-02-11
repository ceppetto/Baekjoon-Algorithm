n = int(input())
coord = []
for i in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))
    
coord.sort(key=lambda x: (x[0], x[1]))

for i in range(len(coord)):
    print(coord[i][0], end=' ')
    print(coord[i][1])
