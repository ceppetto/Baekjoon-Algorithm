n = int(input())
people = list(map(int, input().split()))
people.sort()

result = 0
for i in range(len(people)):
    if i == 0:
        result += people[i]
    else:
        tmp = people[0:i]
        result = sum(tmp) + people[i] + result
    
print(result)
