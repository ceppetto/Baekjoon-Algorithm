def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
x = list(map(int, input().split()))
for i in x:
    res = binary_search(num, i, 0, n - 1)
    if res == None:
        print('0')
    else:
        print('1')
    
