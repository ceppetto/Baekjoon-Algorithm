import sys

n = int(input())
student = []
for i in range(n):
    name, kor, eng, math = sys.stdin.readline().rstrip().split()
    student.append((name, int(kor), int(eng), int(math)))

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(student[i][0])
