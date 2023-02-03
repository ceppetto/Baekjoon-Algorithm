n = int(input())
inputStr = [input() for i in range(n)]

for s in inputStr:
    iterNum, iterC = s.split()
    for c in iterC:
        print(c * int(iterNum), end="")
    print()