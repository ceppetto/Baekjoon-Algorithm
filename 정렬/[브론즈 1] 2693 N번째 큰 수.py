n = int(input())
for i in range(n):
    num = list(map(int, input().split()))
    num.sort(reverse=True)
    print(num[2])
