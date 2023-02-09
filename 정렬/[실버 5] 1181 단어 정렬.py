n = int(input())
word = []

for i in range(n):
    s = input()
    if s not in word:
        word.append(s)

word.sort(key=lambda x: (len(x), x))

for w in word:
    print(w)
