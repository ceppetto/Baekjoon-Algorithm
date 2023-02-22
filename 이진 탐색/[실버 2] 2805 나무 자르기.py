n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
result = 0

while start <= end:
    sum = 0
    cutter = (start + end) // 2
    for i in tree:
        if i > cutter:
            sum += i - cutter
    if sum < m:
        end = cutter - 1
    else:
        result = cutter
        start = cutter + 1
            
print(result)
