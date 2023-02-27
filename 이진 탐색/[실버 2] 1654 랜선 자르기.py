import sys
k, n = map(int, sys.stdin.readline().rstrip().split())
have = []
for i in range(k):
    have.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(have)

while start <= end:
    tmp = 0
    mid = (start + end) // 2
    for i in have:
        tmp += i // mid
    if tmp >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
