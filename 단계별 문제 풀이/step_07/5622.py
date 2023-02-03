s = input()
time = 0

for i in range(len(s)):
    dial = s[i]
    if dial == "A" or dial == "B" or dial == "C":
        time += 3
    if dial == "D" or dial == "E" or dial == "F":
        time += 4
    if dial == "G" or dial == "H" or dial == "I":
        time += 5
    if dial == "J" or dial == "K" or dial == "L":
        time += 6
    if dial == "M" or dial == "N" or dial == "O":
        time += 7
    if dial == "P" or dial == "Q" or dial == "R" or dial == "S":
        time += 8
    if dial == "T" or dial == "U" or dial == "V":
        time += 9
    if dial == "W" or dial == "X" or dial == "Y" or dial == "Z":
        time += 10
print(time)