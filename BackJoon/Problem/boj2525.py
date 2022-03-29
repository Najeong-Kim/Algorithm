H, M = map(int, input().split())
time = int(input())
now = (H * 60 + M + time) % 3600
print((now // 60) % 24, now % 60)
