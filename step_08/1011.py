T = int(input())

for _ in range(T):
    maxDistance = 1
    count = 0

    coordinates = list(map(int, input().split()))
    x = coordinates[0]
    y = coordinates[1]

    distance = y - x

    while distance > 0:
        if distance >= maxDistance * 2:
            count += 2
            distance -= maxDistance * 2
            maxDistance += 1
        else:
            count += 1
            distance -= maxDistance

    print(count)