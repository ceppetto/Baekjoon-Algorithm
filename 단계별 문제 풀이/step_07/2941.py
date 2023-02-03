alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()

for a in alpha:
    s = s.replace(a, "*")

print(len(s))
