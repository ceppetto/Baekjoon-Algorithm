import sys
n = int(sys.stdin.readline().rstrip())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))
    
print(round(sum(num) / n))
num.sort()
print(num[len(num) // 2])

count = {}
for i in num:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

max_value = max(count.values())
most_often = 0
for key, value in count.items():
    if value == max_value:
        if most_often == 0:
            most_often = key
        else:
            most_often = key
            break
print(most_often)
print(max(num) - min(num))
