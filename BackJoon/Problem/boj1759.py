import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
array = list(map(str, input().split()))
sorted_array = sorted(array)

array_com = list(combinations(sorted_array, L))

first = ['a', 'e', 'i', 'o', 'u']

for i in array_com:
    count = 0
    for j in i:
        if j in first:
            count += 1
    if count >= 1 and (L - count) >= 2:
        print(''.join(i))
