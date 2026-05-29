# 투포인터로 풀어보기

N, M = map(int, input().split())
arr = []
arr.extend(list(map(int, input().split())))
arr.extend(list(map(int, input().split())))
arr.sort()
print(*arr)