n = int(input())

start = 1
end = n
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid * mid == n:
        result = mid
        break
    elif mid * mid < n:
        start = mid + 1
    else:
        end = mid - 1

print(result)
