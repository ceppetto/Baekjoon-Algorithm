s = input().lower()
cnt = 0
mostUsed = 0
alpha = [0 for _ in range(26)]

for c in s:
    alpha[ord(c)-97] += 1

for i in range(26):
    if max(alpha) == alpha[i]:
        mostUsed = i
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(mostUsed+97).upper())
