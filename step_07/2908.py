n1, n2 = input().split()
reversedN1 = int(n1[::-1])
reversedN2 = int(n2[::-1])

if reversedN1 > reversedN2:
    print(reversedN1)
else:
    print(reversedN2)