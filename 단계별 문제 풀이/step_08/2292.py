N = int(input())
pos = 1
shellNum = 1

while N > pos:
    pos += 6 * shellNum
    shellNum += 1

print(shellNum)