n = int(input())
minValue = 1000000
maxValue = -1000000

input_num = list(map(int, input().split()))

for i in range(n):
    if input_num[i] < minValue:
        minValue = input_num[i]
    if input_num[i] > maxValue:
        maxValue = input_num[i]

print(minValue, maxValue)
