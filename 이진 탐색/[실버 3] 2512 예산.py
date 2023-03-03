import sys

n = int(sys.stdin.readline().rstrip())
money = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

if sum(money) <= m:
    print(max(money))
else:
    result = 0
    start = 0
    end = m
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in money:
            if i > mid:
                tmp += mid
            else:
                tmp += i
        if tmp == m:
            result = mid
            break
        elif tmp < m:
            if result < mid:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
            
    print(result)
