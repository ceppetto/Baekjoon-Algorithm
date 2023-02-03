maxNum = 0
maxNum_index = 0

for i in range(9):
    n = int(input())
    if n > maxNum:
        maxNum = n
        maxNum_index = i + 1

print(maxNum)
print(maxNum_index)