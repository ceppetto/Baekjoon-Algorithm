X = int(input())

lineNum = []
line = 1
passedBox = 1

while X > passedBox:
    line += 1
    passedBox += line

passedBox -= line

if line % 2 == 0:
    k = line
    for i in range(1, line+1):
        lineNum.append(str(i)+"/"+str(k))
        k -= 1

if line % 2 == 1:
    k = line
    for i in range(1, line+1):
        lineNum.append(str(k)+"/"+str(i))
        k -= 1


print(lineNum[X-passedBox-1])
