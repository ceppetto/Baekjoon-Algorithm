n = int(input())
member = []
for i in range(n):
    age, name = input().split()
    member.append((int(age), name))

member.sort(key=lambda x: x[0])

for i in member:
    age, name = i
    print(age, end=" ")
    print(name)
