n = int(input())

result = 0
start = 1
end = n
while start <= end:
    mid = (start + end) // 2
    if mid * mid >= n:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
