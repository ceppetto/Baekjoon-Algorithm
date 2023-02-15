n = int(input())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))

a_array.sort()
b_array.sort(reverse=True)

sum = 0
for i in range(n):
    sum += a_array[i] * b_array[i]
    
print(sum)
