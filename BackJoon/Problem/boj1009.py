import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  a, b = map(int, input().split())
  start = a % 10
  array = [start]

  while True:
    now = (start * a) % 10
    if now in array:
      break
    array.append(now)
    start = now

  index = (b % len(array)) - 1
  
  if array[index] == 0:
    print(10)
  else:
    print(array[index])
    