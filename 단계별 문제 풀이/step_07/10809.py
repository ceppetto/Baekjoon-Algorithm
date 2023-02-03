s = input()
cnt = 0
alpha = [-1 for _ in range(26)]

for c in s:
    index = ord(c) - 97
    if alpha[index] == -1:
        alpha[index] = cnt
    cnt += 1

for i in range(26):
    print(alpha[i], end=" ")