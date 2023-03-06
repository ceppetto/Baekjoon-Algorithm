import sys
n = int(sys.stdin.readline().rstrip())
solution = list(map(int, sys.stdin.readline().rstrip().split()))

result = (0, 0)
start = 0
end = n - 1
value = 1999999999
while start < end:
    tmp = solution[start] + solution[end]
    
    # 특성값이 0인 경우
    if tmp == 0:
        result = (solution[start], solution[end])
        break
    
    # 기존보다 0에 가까운 경우
    if abs(tmp) <= value:
            result = (solution[start], solution[end])
            value = abs(tmp)
            
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])   
