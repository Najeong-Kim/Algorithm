import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    scores = list(map(int, input().split()))
    average = sum(scores[1:])/scores[0]
    count = 0
    for j in range(1, len(scores)):
        if scores[j] > average:
            count += 1
    print(format(count/(len(scores)-1) * 100, ".3f") + '%')
