n = int(input())
num = []
for i in range(n):
  num.append(int(input()))

# 선택 정렬로 풀기
for i in range(n):
  min_index = i
  for j in range(i + 1, n):
    if num[min_index] > num[j]:
      min_index = j
  num[i], num[min_index] = num[min_index], num[i]

for i in num:
  print(i)