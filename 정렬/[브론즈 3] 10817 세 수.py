num = list(map(int, input().split()))
# 선택 정렬로 풀기
for i in range(3):
    min_index = i
    for j in range(i + 1, 3):
        if num[min_index] > num[j]:
            min_index = j
    num[i], num[min_index] = num[min_index], num[i]

print(num[1])