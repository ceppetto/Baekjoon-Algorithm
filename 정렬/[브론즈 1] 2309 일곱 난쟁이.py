import itertools

h = []
for _ in range(9):
    h.append(int(input()))
    
nCr = itertools.combinations(h, 7)
nCr = list(nCr)

for i in range(len(nCr)):
    if sum(nCr[i]) == 100:
        res = list(nCr[i])
        res.sort()
        for j in res:
            print(j)
        break
