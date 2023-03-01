t = int(input())
for i in range(t):
    score = list(map(int, input().split()))
    score.sort()
    score.remove(score[0])
    score.remove(score[-1])
    total = sum(score)
    
    if score[-1] - score[0] >= 4:
        print("KIN")
    else:
        print(total)
    
