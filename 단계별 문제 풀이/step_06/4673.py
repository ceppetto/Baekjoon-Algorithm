d = [0 for i in range(100000)]
for i in range(1, 10000):
    numLen = len(str(i))
    if numLen == 1:
        selfNum = i + int(i % 10)
        d[selfNum] = 1
    if numLen == 2:
        selfNum = i + int(i % 10) + int(i / 10)
        d[selfNum] = 1
    if numLen == 3:
        selfNum = i + int(i % 10) + int((i / 10) % 10) + int((i / 10) / 10)
        d[selfNum] = 1
    if numLen == 4:
        selfNum = i + int(i % 10) + int(((i / 10) % 100) % 10) + int(((i / 10) % 100) / 10) + int(i / 1000)
        d[selfNum] = 1

for i in range(1, 10000):
    if d[i] == 0:
        print(i)
