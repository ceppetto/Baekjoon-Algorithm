import sys
n = int(sys.stdin.readline().rstrip())
solution = list(map(int, sys.stdin.readline().rstrip().split()))

result = (0, 0)
value = 1999999999
for i in range(n - 1):
    current = solution[i]
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        tmp = current + solution[mid]
        # 특성값이 0인 경우
        if tmp == 0:
            result = (current, solution[mid])
            break
        
        # 기존보다 0에 가까운 경우
        if abs(tmp) <= value:
                result = (current, solution[mid])
                value = abs(tmp)
                
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(result[0], result[1])   
