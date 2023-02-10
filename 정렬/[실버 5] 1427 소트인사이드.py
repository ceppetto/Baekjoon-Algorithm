n = list(map(int, input()))
n.sort(reverse=True)
n = list(map(str, n))
print(''.join(n))
