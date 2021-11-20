import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
for j in range(N):
    heapq.heappush(heap, int(input()))

result = 0

for _ in range(N-1):
    first, second = heapq.heappop(heap), heapq.heappop(heap)
    now = first + second
    heapq.heappush(heap, now)
    result += now

print(result)
