import sys

x, y = map(int, input().split())
z = (y * 100) // x

start = 1
end = 1000000000

# 승률이 99%인 경우, 절대 100%가 될 수 없음을 고려해야 함
if x == y or z == 99:
    print('-1')
else:
    play = 0
    while start <= end:
        mid = (start + end) // 2
        new_z = ((y + mid) * 100) // (x + mid)
        if new_z > z:
            end = mid - 1
            play = mid
        else:
            start = mid + 1
    print(play)    
