T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = H
    else:
        floor = N % H
    if (N - floor) == 0:
        roomNum = 1
    else:
        roomNum = int((N - floor) / H) + 1
    print(str(floor) + str(roomNum).zfill(2))
