import math

num = list(map(int, input().split()))
num.sort()

while num[0] != 0 and num[1] != 0 and num[2] != 0:
    if math.sqrt(num[0] * num[0] + num[1] * num[1]) == num[2]:
        print("right")
    else:
        print("wrong")

    num = list(map(int, input().split()))
    num.sort()
